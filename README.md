# Sistema Inteligente para Analise e Interpretacao de Consumo de Energia Eletrica em Edificacoes

Projeto de PFC 1 em Engenharia de Computacao na UFG com foco na fundamentacao teorica, definicao da arquitetura inicial, especificacao tecnica e preparacao do estudo de caso com o dataset **UCI Household Electric Power Consumption**.

## Objetivo do PFC 1

Construir a base tecnica do projeto que, em etapas futuras, dara suporte a um sistema capaz de:

1. ingerir dados de consumo de energia de edificacoes;
2. processar e analisar series temporais de consumo;
3. interpretar resultados com apoio de modelos de linguagem;
4. gerar diagnosticos e relatorios tecnicos automatizados.

Nesta etapa, o escopo esta limitado a:

- organizacao da base de codigo;
- definicao da arquitetura inicial;
- ingestao e limpeza do dataset UCI;
- analise exploratoria inicial;
- preparacao para futura integracao com LLM/RAG.

## Como a estrutura foi organizada

A raiz do projeto guarda os materiais do trabalho:

- `data/`: arquivos de dados do projeto
- `docs/`: documentacao do PFC, organizada em planejamento, arquitetura, notas e documentos institucionais
- `notebooks/`: exploracao interativa
- `scripts/`: scripts executaveis
- `src/`: codigo-fonte Python
- `tests/`: preparacao para testes automatizados

Cada uma dessas pastas agora possui um `README.md` proprio para facilitar a navegacao.

Dentro de `src/`:

```text
src/
 |-- projeto_energia/
    |-- dados/               # Codigo de ingestao e validacao de dados
    |-- processamento/       # Limpeza e transformacoes
    |-- analise/             # Analise exploratoria e indicadores
    |-- interpretacao_llm/   # Contratos para futura camada com LLM
    |-- relatorios/          # Estruturas para relatorios tecnicos
```

## Dataset inicial

O estudo de caso usa o arquivo:

`data/household_power_consumption.txt`

Se o arquivo nao estiver presente, ele deve ser colocado exatamente nesse caminho para que os scripts e notebooks funcionem sem ajustes.

## Ambiente sugerido

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Como executar a analise inicial

Script:

```powershell
python scripts/executar_analise_inicial.py
```

Analise consolidada com indicadores interpretaveis:

```powershell
python scripts/executar_analise_consolidada.py
```

Execucao pelo pacote em `src/`:

```powershell
$env:PYTHONPATH="src"
python -m projeto_energia
```

Notebook principal de estudo:

`notebooks/analise_consumo_energia_edificacoes.ipynb`

## Documentacao academica

O indice da documentacao fica em:

`docs/README.md`

Arquivos principais:

- `docs/planejamento_tecnico_pfc1.md`
- `docs/arquitetura_do_repositorio.md`
- `docs/notas/briefing_inicial_projeto.md`
- `docs/notas/ideias_de_analise.md`
- `docs/analises/interpretacao_resultados_analise_consumo.md`
- `docs/guias/aula_termos_estatisticos_e_analiticos.md`


