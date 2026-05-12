from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


COLUNA_ALVO_PADRAO = "Global_active_power"
COLUNA_DATETIME_PADRAO = "datetime"
COLUNAS_SUBMEDICAO_PADRAO = [
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3",
]


@dataclass(frozen=True)
class ResultadoPicos:
    limiar_kw: float
    quantidade_por_hora: pd.DataFrame
    maiores_picos: pd.DataFrame


def _obter_serie_temporal(
    df: pd.DataFrame,
    coluna_datetime: str = COLUNA_DATETIME_PADRAO,
) -> pd.DataFrame:
    if isinstance(df.index, pd.DatetimeIndex):
        return df.sort_index()

    if coluna_datetime not in df.columns:
        raise ValueError(f"Coluna temporal nao encontrada: {coluna_datetime}")

    dados = df.dropna(subset=[coluna_datetime]).copy()
    return dados.sort_values(coluna_datetime).set_index(coluna_datetime)


def adicionar_atributos_temporais(
    df: pd.DataFrame,
    coluna_datetime: str = COLUNA_DATETIME_PADRAO,
) -> pd.DataFrame:
    """Cria atributos de calendario para analises temporais."""
    dados = df.copy()
    data_hora = (
        pd.Series(dados.index, index=dados.index)
        if isinstance(dados.index, pd.DatetimeIndex)
        else dados[coluna_datetime]
    )

    dados["ano"] = data_hora.dt.year
    dados["mes"] = data_hora.dt.month
    dados["dia"] = data_hora.dt.day
    dados["hora"] = data_hora.dt.hour
    dados["minuto"] = data_hora.dt.minute
    dados["dia_semana"] = data_hora.dt.dayofweek
    dados["nome_dia_semana"] = data_hora.dt.day_name()
    dados["fim_de_semana"] = (dados["dia_semana"] >= 5).astype(int)
    dados["periodo_dia"] = dados["hora"].map(classificar_periodo_dia)

    return dados


def classificar_periodo_dia(hora: int) -> str:
    if 0 <= hora < 6:
        return "madrugada"
    if 6 <= hora < 12:
        return "manha"
    if 12 <= hora < 18:
        return "tarde"
    return "noite"


def adicionar_indicadores_energeticos(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    janela_movel: int = 60,
    colunas_submedicao: list[str] | None = None,
) -> pd.DataFrame:
    """Adiciona indicadores simples de consumo e variacao temporal."""
    dados = df.copy()
    colunas_submedicao = colunas_submedicao or COLUNAS_SUBMEDICAO_PADRAO
    colunas_existentes = [coluna for coluna in colunas_submedicao if coluna in dados.columns]

    if colunas_existentes:
        dados["submedicao_total"] = dados[colunas_existentes].fillna(0).sum(axis=1)

    if coluna_alvo in dados.columns and "submedicao_total" in dados.columns:
        energia_total_minuto_wh = dados[coluna_alvo] * 1000 / 60
        dados["consumo_nao_medido_aprox_wh"] = energia_total_minuto_wh - dados["submedicao_total"]

    if coluna_alvo in dados.columns:
        dados["delta_potencia"] = dados[coluna_alvo].diff()
        dados["taxa_variacao_potencia"] = dados[coluna_alvo].pct_change()
        dados["media_movel_potencia"] = dados[coluna_alvo].rolling(
            janela_movel,
            min_periods=5,
        ).mean()
        dados["desvio_movel_potencia"] = dados[coluna_alvo].rolling(
            janela_movel,
            min_periods=5,
        ).std()

    return dados


def classificar_regimes_consumo(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
) -> pd.DataFrame:
    """Classifica o consumo em baixo, moderado e alto usando quartis."""
    dados = df.copy()
    quartil_1 = dados[coluna_alvo].quantile(0.25)
    quartil_3 = dados[coluna_alvo].quantile(0.75)

    dados["regime_consumo"] = "moderado"
    dados.loc[dados[coluna_alvo] <= quartil_1, "regime_consumo"] = "baixo"
    dados.loc[dados[coluna_alvo] >= quartil_3, "regime_consumo"] = "alto"
    dados.loc[dados[coluna_alvo].isna(), "regime_consumo"] = np.nan

    return dados


def agregar_estatisticas_por_grupo(
    df: pd.DataFrame,
    coluna_grupo: str,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
) -> pd.DataFrame:
    """Resume media, mediana, desvio e extremos por um agrupamento."""
    return df.groupby(coluna_grupo)[coluna_alvo].agg(
        media="mean",
        mediana="median",
        desvio_padrao="std",
        minimo="min",
        maximo="max",
        contagem="count",
    )


def montar_perfis_temporais(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
) -> dict[str, pd.DataFrame]:
    """Gera tabelas de perfil por hora, dia da semana, mes e periodo."""
    return {
        "perfil_por_hora": agregar_estatisticas_por_grupo(df, "hora", coluna_alvo),
        "perfil_por_dia_semana": agregar_estatisticas_por_grupo(
            df,
            "dia_semana",
            coluna_alvo,
        ),
        "perfil_por_mes": agregar_estatisticas_por_grupo(df, "mes", coluna_alvo),
        "perfil_por_periodo": agregar_estatisticas_por_grupo(
            df,
            "periodo_dia",
            coluna_alvo,
        ),
    }


def calcular_consumo_diario(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    coluna_datetime: str = COLUNA_DATETIME_PADRAO,
) -> pd.DataFrame:
    """Calcula energia diaria aproximada a partir de serie minuto a minuto."""
    serie_temporal = _obter_serie_temporal(df, coluna_datetime)
    return pd.DataFrame(
        {
            "energia_diaria_aprox_kwh": serie_temporal[coluna_alvo].resample("D").sum() / 60,
            "potencia_media_diaria_kw": serie_temporal[coluna_alvo].resample("D").mean(),
            "potencia_maxima_diaria_kw": serie_temporal[coluna_alvo].resample("D").max(),
        }
    )


def resumir_regimes_consumo(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
) -> pd.DataFrame:
    return df.groupby("regime_consumo")[coluna_alvo].agg(
        quantidade="count",
        media_kw="mean",
        mediana_kw="median",
        maximo_kw="max",
    )


def identificar_picos_consumo(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    percentil: float = 0.95,
    limite_maiores_picos: int = 15,
) -> ResultadoPicos:
    limiar = float(df[coluna_alvo].quantile(percentil))
    eventos_pico = df[df[coluna_alvo] >= limiar].copy()

    quantidade_por_hora = (
        eventos_pico.groupby("hora")[coluna_alvo]
        .count()
        .rename("quantidade_picos")
        .to_frame()
        .sort_values("quantidade_picos", ascending=False)
    )

    colunas_maiores_picos = [
        coluna
        for coluna in [coluna_alvo, "periodo_dia", "dia_semana", "fim_de_semana"]
        if coluna in eventos_pico.columns
    ]
    maiores_picos = (
        eventos_pico[colunas_maiores_picos]
        .sort_values(coluna_alvo, ascending=False)
        .head(limite_maiores_picos)
    )

    return ResultadoPicos(
        limiar_kw=limiar,
        quantidade_por_hora=quantidade_por_hora,
        maiores_picos=maiores_picos,
    )


def calcular_participacao_submedicoes(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    colunas_submedicao: list[str] | None = None,
) -> pd.DataFrame:
    """Calcula participacao media aproximada das submetragens por periodo."""
    colunas_submedicao = colunas_submedicao or COLUNAS_SUBMEDICAO_PADRAO
    colunas_existentes = [coluna for coluna in colunas_submedicao if coluna in df.columns]
    dados = df.copy()
    energia_total_minuto_wh = dados[coluna_alvo] * 1000 / 60

    colunas_participacao = []
    for coluna in colunas_existentes:
        nome_coluna = f"participacao_{coluna.lower()}_pct"
        dados[nome_coluna] = np.where(
            energia_total_minuto_wh > 0,
            100 * dados[coluna] / energia_total_minuto_wh,
            np.nan,
        )
        colunas_participacao.append(nome_coluna)

    return dados.groupby("periodo_dia")[colunas_participacao].mean()


def resumir_dias_extremos(
    df: pd.DataFrame,
    consumo_diario: pd.DataFrame,
    coluna_datetime: str = COLUNA_DATETIME_PADRAO,
    colunas_submedicao: list[str] | None = None,
) -> pd.DataFrame:
    colunas_submedicao = colunas_submedicao or COLUNAS_SUBMEDICAO_PADRAO
    serie_temporal = _obter_serie_temporal(df, coluna_datetime)
    colunas_existentes = [coluna for coluna in colunas_submedicao if coluna in serie_temporal.columns]
    submedicoes_diarias = serie_temporal[colunas_existentes].resample("D").sum()
    base_diaria = consumo_diario.join(submedicoes_diarias, how="left")

    linhas = []
    for tipo_dia, data_ref in [
        ("maior_consumo", base_diaria["energia_diaria_aprox_kwh"].idxmax()),
        ("menor_consumo", base_diaria["energia_diaria_aprox_kwh"].idxmin()),
    ]:
        linha = base_diaria.loc[data_ref]
        submedicoes_do_dia = linha[colunas_existentes].dropna()

        linhas.append(
            {
                "tipo_dia": tipo_dia,
                "data": data_ref.date(),
                "ano": data_ref.year,
                "mes": data_ref.month,
                "dia": data_ref.day,
                "energia_diaria_aprox_kwh": linha["energia_diaria_aprox_kwh"],
                "potencia_media_diaria_kw": linha["potencia_media_diaria_kw"],
                "potencia_maxima_diaria_kw": linha["potencia_maxima_diaria_kw"],
                "submedicao_maior": submedicoes_do_dia.idxmax(),
                "valor_submedicao_maior_wh": submedicoes_do_dia.max(),
                "submedicao_menor": submedicoes_do_dia.idxmin(),
                "valor_submedicao_menor_wh": submedicoes_do_dia.min(),
            }
        )

    return pd.DataFrame(linhas)


def montar_tabelas_insumo_interpretacao(
    df: pd.DataFrame,
    consumo_diario: pd.DataFrame,
    resultado_picos: ResultadoPicos,
    participacao_submedicoes: pd.DataFrame,
    dias_extremos: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
) -> dict[str, pd.DataFrame]:
    tabelas = montar_perfis_temporais(df, coluna_alvo)
    tabelas.update(
        {
            "regimes_consumo": resumir_regimes_consumo(df, coluna_alvo),
            "consumo_diario": consumo_diario,
            "quantidade_picos_por_hora": resultado_picos.quantidade_por_hora,
            "maiores_picos": resultado_picos.maiores_picos,
            "participacao_submedicoes": participacao_submedicoes,
            "dias_extremos": dias_extremos,
        }
    )
    return tabelas
