"""Estruturas para geracao de relatorios tecnicos."""

from .relatorio_tecnico import (
    MetadadosRelatorio,
    SecaoRelatorioTecnico,
    gerar_relatorio_completo,
    gerar_relatorio_markdown,
    montar_secoes_a_partir_de_tabelas,
    salvar_relatorio,
)

__all__ = [
    "MetadadosRelatorio",
    "SecaoRelatorioTecnico",
    "gerar_relatorio_completo",
    "gerar_relatorio_markdown",
    "montar_secoes_a_partir_de_tabelas",
    "salvar_relatorio",
]
