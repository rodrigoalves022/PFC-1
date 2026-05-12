from dataclasses import dataclass


@dataclass
class ResumoAnalise:
    """Estrutura minima para futuro envio de resultados analiticos a um LLM."""

    inicio_periodo: str
    fim_periodo: str
    principais_achados: list[str]
    limitacoes: list[str]


def montar_contexto_interpretacao(resumo: ResumoAnalise) -> dict:
    """Retorna um payload simples para futura camada de interpretacao."""
    return {
        "inicio_periodo": resumo.inicio_periodo,
        "fim_periodo": resumo.fim_periodo,
        "principais_achados": resumo.principais_achados,
        "limitacoes": resumo.limitacoes,
    }
