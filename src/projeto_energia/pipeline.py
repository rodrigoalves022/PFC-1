"""Pipeline principal do projeto de analise de consumo de energia."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from projeto_energia.analise.anomalias import (
    detectar_anomalias_isolation_forest,
    detectar_anomalias_zscore,
    resumir_anomalias,
)
from projeto_energia.analise.clusterizacao import (
    clusterizar_perfis_consumo,
    resumir_clusters,
)
from projeto_energia.analise.exploratoria import (
    calcular_matriz_correlacao,
    descrever_valores_ausentes,
    resumir_dataset,
)
from projeto_energia.analise.indicadores import (
    adicionar_atributos_temporais,
    adicionar_indicadores_energeticos,
    calcular_consumo_diario,
    calcular_participacao_submedicoes,
    classificar_regimes_consumo,
    identificar_picos_consumo,
    montar_perfis_temporais,
    montar_tabelas_insumo_interpretacao,
    resumir_dias_extremos,
    resumir_regimes_consumo,
)
from projeto_energia.configuracoes import CAMINHO_DATASET_PADRAO, RAIZ_PROJETO
from projeto_energia.dados.ingestao import carregar_dataset_uci
from projeto_energia.processamento.limpeza import limpar_dados_consumo_residencial
from projeto_energia.relatorios import gerar_relatorio_completo


CAMINHO_RELATORIO_PADRAO = RAIZ_PROJETO / "docs" / "analises" / "resumo_analise_consolidada.md"


@dataclass(frozen=True)
class ResultadoPipeline:
    """Resumo dos principais artefatos gerados pelo pipeline."""

    caminho_relatorio: Path
    total_registros: int
    limiar_pico_kw: float
    quantidade_anomalias_zscore: int
    quantidade_anomalias_isolation_forest: int
    quantidade_clusters: int
    perfil_por_periodo: pd.DataFrame


def executar_pipeline_consolidado(
    caminho_dataset: str | Path = CAMINHO_DATASET_PADRAO,
    caminho_relatorio: str | Path = CAMINHO_RELATORIO_PADRAO,
) -> ResultadoPipeline:
    """Executa o fluxo completo de ingestao, analise e relatorio."""
    dados_brutos = carregar_dataset_uci(caminho_dataset)
    dados_limpos = limpar_dados_consumo_residencial(dados_brutos)

    dados_indicadores = adicionar_atributos_temporais(dados_limpos)
    dados_indicadores = adicionar_indicadores_energeticos(dados_indicadores)
    dados_indicadores = classificar_regimes_consumo(dados_indicadores)

    dados_indicadores, res_zscore = detectar_anomalias_zscore(dados_indicadores)
    dados_indicadores, res_iforest = detectar_anomalias_isolation_forest(dados_indicadores)
    resumo_anomalias_df = resumir_anomalias([res_zscore, res_iforest])

    dados_indicadores, res_clusters, _ = clusterizar_perfis_consumo(dados_indicadores)
    resumo_clusters_df = resumir_clusters(dados_indicadores)

    resumo_dataset = resumir_dataset(dados_indicadores)
    valores_ausentes = descrever_valores_ausentes(dados_indicadores)
    colunas_correlacao = [
        "datetime",
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3",
        "submedicao_total",
        "consumo_nao_medido_aprox_wh",
    ]
    correlacao = calcular_matriz_correlacao(dados_indicadores[colunas_correlacao])

    perfis_temporais = montar_perfis_temporais(dados_indicadores)
    consumo_diario = calcular_consumo_diario(dados_indicadores)
    regimes = resumir_regimes_consumo(dados_indicadores)
    resultado_picos = identificar_picos_consumo(dados_indicadores)
    participacao_submedicoes = calcular_participacao_submedicoes(dados_indicadores)
    dias_extremos = resumir_dias_extremos(dados_indicadores, consumo_diario)

    tabelas_interpretacao = montar_tabelas_insumo_interpretacao(
        dados_indicadores,
        consumo_diario,
        resultado_picos,
        participacao_submedicoes,
        dias_extremos,
    )
    tabelas_interpretacao["resumo_dataset"] = resumo_dataset
    tabelas_interpretacao["valores_ausentes"] = valores_ausentes
    tabelas_interpretacao["correlacao"] = correlacao
    tabelas_interpretacao["regimes"] = regimes
    tabelas_interpretacao["anomalias"] = resumo_anomalias_df
    tabelas_interpretacao["clusters"] = resumo_clusters_df

    inicio_periodo = dados_indicadores["datetime"].min().strftime("%Y-%m-%d")
    fim_periodo = dados_indicadores["datetime"].max().strftime("%Y-%m-%d")
    total_registros = len(dados_indicadores)
    caminho_relatorio = Path(caminho_relatorio)

    gerar_relatorio_completo(
        tabelas_interpretacao=tabelas_interpretacao,
        inicio_periodo=inicio_periodo,
        fim_periodo=fim_periodo,
        total_registros=total_registros,
        caminho_saida=caminho_relatorio,
        limiar_pico=resultado_picos.limiar_kw,
    )

    return ResultadoPipeline(
        caminho_relatorio=caminho_relatorio,
        total_registros=total_registros,
        limiar_pico_kw=resultado_picos.limiar_kw,
        quantidade_anomalias_zscore=res_zscore.quantidade_anomalias,
        quantidade_anomalias_isolation_forest=res_iforest.quantidade_anomalias,
        quantidade_clusters=res_clusters.n_clusters,
        perfil_por_periodo=perfis_temporais["perfil_por_periodo"],
    )
