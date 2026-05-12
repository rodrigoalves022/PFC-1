"""Geracao automatica de relatorios tecnicos em Markdown."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import pandas as pd


@dataclass
class SecaoRelatorioTecnico:
    """Representa uma secao individual do relatorio."""

    titulo: str
    conteudo: str
    tabelas: list[tuple[str, pd.DataFrame]] = field(default_factory=list)


@dataclass
class MetadadosRelatorio:
    """Metadados do relatorio gerado."""

    titulo: str
    data_geracao: str
    inicio_periodo_dados: str
    fim_periodo_dados: str
    total_registros: int
    fonte_dados: str = "UCI Household Electric Power Consumption"


def _formatar_tabela_markdown(
    tabela: pd.DataFrame,
    casas_decimais: int = 3,
    limite_linhas: int | None = None,
) -> str:
    """Converte um DataFrame em tabela Markdown."""
    tabela_formatada = tabela.head(limite_linhas).copy() if limite_linhas else tabela.copy()
    colunas_numericas = tabela_formatada.select_dtypes(include="number").columns
    tabela_formatada[colunas_numericas] = tabela_formatada[colunas_numericas].round(casas_decimais)
    try:
        return tabela_formatada.to_markdown()
    except ImportError:
        return "```text\n" + tabela_formatada.to_string() + "\n```"


def montar_secoes_a_partir_de_tabelas(
    tabelas_interpretacao: dict[str, pd.DataFrame],
    limiar_pico: float | None = None,
) -> list[SecaoRelatorioTecnico]:
    """Cria secoes do relatorio a partir das tabelas de insumo de interpretacao."""
    secoes = []

    secoes.append(
        SecaoRelatorioTecnico(
            titulo="Contexto do Estudo",
            conteudo=(
                "Este relatorio apresenta os resultados da analise exploratoria "
                "de consumo de energia eletrica residencial, utilizando o dataset "
                "UCI Household Electric Power Consumption como estudo de caso. "
                "Os dados foram processados e analisados pelo pipeline computacional "
                "do projeto."
            ),
        )
    )

    if "perfil_por_hora" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Perfil de Consumo por Hora",
                conteudo="Media, mediana e desvio padrao da potencia ativa agrupados por hora do dia.",
                tabelas=[("Perfil por hora", tabelas_interpretacao["perfil_por_hora"])],
            )
        )

    if "perfil_por_dia_semana" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Perfil de Consumo por Dia da Semana",
                conteudo="Estatisticas de consumo agrupadas por dia da semana (0=segunda, 6=domingo).",
                tabelas=[("Perfil por dia da semana", tabelas_interpretacao["perfil_por_dia_semana"])],
            )
        )

    if "perfil_por_mes" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Perfil de Consumo por Mes",
                conteudo="Variacao sazonal do consumo ao longo dos meses do ano.",
                tabelas=[("Perfil por mes", tabelas_interpretacao["perfil_por_mes"])],
            )
        )

    if "perfil_por_periodo" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Perfil de Consumo por Periodo do Dia",
                conteudo="Comparacao entre madrugada, manha, tarde e noite.",
                tabelas=[("Perfil por periodo", tabelas_interpretacao["perfil_por_periodo"])],
            )
        )

    if "regimes_consumo" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Regimes de Consumo",
                conteudo="Classificacao em baixo, moderado e alto com base nos quartis da potencia ativa.",
                tabelas=[("Regimes", tabelas_interpretacao["regimes_consumo"])],
            )
        )

    if "anomalias" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Deteccao de Anomalias",
                conteudo=(
                    "Comparacao entre a deteccao estatistica por Z-score e a "
                    "deteccao multivariada por Isolation Forest."
                ),
                tabelas=[("Resumo de anomalias", tabelas_interpretacao["anomalias"])],
            )
        )

    if "clusters" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Clusterizacao de Perfis",
                conteudo=(
                    "Resumo dos grupos formados por K-Means a partir das variaveis "
                    "eletricas padronizadas."
                ),
                tabelas=[("Resumo de clusters", tabelas_interpretacao["clusters"])],
            )
        )

    if "quantidade_picos_por_hora" in tabelas_interpretacao:
        descricao_picos = "Distribuicao horaria dos eventos de pico de consumo."
        if limiar_pico is not None:
            descricao_picos += f" Limiar adotado: {limiar_pico:.3f} kW (percentil 95)."
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Picos de Consumo",
                conteudo=descricao_picos,
                tabelas=[("Picos por hora", tabelas_interpretacao["quantidade_picos_por_hora"])],
            )
        )

    if "participacao_submedicoes" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Participacao das Submedicoes",
                conteudo="Participacao media aproximada de cada submetragem por periodo do dia.",
                tabelas=[("Participacao", tabelas_interpretacao["participacao_submedicoes"])],
            )
        )

    if "dias_extremos" in tabelas_interpretacao:
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Dias Extremos de Consumo",
                conteudo="Dias com maior e menor consumo diario registrado.",
                tabelas=[("Dias extremos", tabelas_interpretacao["dias_extremos"])],
            )
        )

    if "consumo_diario" in tabelas_interpretacao:
        consumo = tabelas_interpretacao["consumo_diario"]
        maiores = consumo.sort_values("energia_diaria_aprox_kwh", ascending=False).head(10)
        menores = consumo.sort_values("energia_diaria_aprox_kwh", ascending=True).head(10)
        secoes.append(
            SecaoRelatorioTecnico(
                titulo="Ranking de Consumo Diario",
                conteudo="Os 10 dias com maior e menor consumo energetico estimado.",
                tabelas=[
                    ("Maiores consumos", maiores),
                    ("Menores consumos", menores),
                ],
            )
        )

    secoes.append(
        SecaoRelatorioTecnico(
            titulo="Observacao Metodologica",
            conteudo=(
                "Os resultados apresentados sao exploratorios. As submetragens e o "
                "consumo nao medido foram tratados como indicadores aproximados, e "
                "nao como decomposicao exata do consumo total da residencia. "
                "A analise nao substitui validacao estatistica mais profunda."
            ),
        )
    )

    return secoes


def gerar_relatorio_markdown(
    metadados: MetadadosRelatorio,
    secoes: list[SecaoRelatorioTecnico],
) -> str:
    """Gera o texto completo do relatorio tecnico em Markdown."""
    partes = []

    partes.append(f"# {metadados.titulo}")
    partes.append("")
    partes.append(f"**Data de geracao:** {metadados.data_geracao}")
    partes.append(f"**Fonte dos dados:** {metadados.fonte_dados}")
    partes.append(f"**Periodo dos dados:** {metadados.inicio_periodo_dados} a {metadados.fim_periodo_dados}")
    partes.append(f"**Total de registros:** {metadados.total_registros:,}")
    partes.append("")
    partes.append("---")
    partes.append("")

    for secao in secoes:
        partes.append(f"## {secao.titulo}")
        partes.append("")
        partes.append(secao.conteudo)
        partes.append("")

        for titulo_tabela, tabela in secao.tabelas:
            partes.append(f"### {titulo_tabela}")
            partes.append("")
            partes.append(_formatar_tabela_markdown(tabela))
            partes.append("")

        partes.append("---")
        partes.append("")

    return "\n".join(partes)


def salvar_relatorio(
    conteudo_markdown: str,
    caminho_saida: str | Path,
) -> Path:
    """Salva o relatorio gerado em um arquivo Markdown."""
    caminho = Path(caminho_saida)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(conteudo_markdown, encoding="utf-8")
    return caminho


def gerar_relatorio_completo(
    tabelas_interpretacao: dict[str, pd.DataFrame],
    inicio_periodo: str,
    fim_periodo: str,
    total_registros: int,
    caminho_saida: str | Path,
    limiar_pico: float | None = None,
    titulo: str = "Relatorio Tecnico — Analise de Consumo de Energia Eletrica",
) -> Path:
    """Funcao de conveniencia que gera e salva o relatorio completo."""
    metadados = MetadadosRelatorio(
        titulo=titulo,
        data_geracao=datetime.now().strftime("%Y-%m-%d %H:%M"),
        inicio_periodo_dados=inicio_periodo,
        fim_periodo_dados=fim_periodo,
        total_registros=total_registros,
    )

    secoes = montar_secoes_a_partir_de_tabelas(tabelas_interpretacao, limiar_pico)
    conteudo = gerar_relatorio_markdown(metadados, secoes)
    return salvar_relatorio(conteudo, caminho_saida)
