# Pasta de Scripts

Esta pasta reune scripts executaveis sem depender do notebook.

Uso atual:

- `executar_analise_inicial.py`: roda uma analise exploratoria inicial do dataset.
- `executar_analise_consolidada.py`: chama o pipeline principal em `src/projeto_energia/pipeline.py` e gera o relatorio tecnico consolidado.

Objetivo:

- facilitar execucoes reprodutiveis;
- evitar que toda analise dependa do ambiente do Jupyter.
