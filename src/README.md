# Pasta de Codigo-Fonte

Esta pasta contem o codigo Python modular do projeto.

Pacote principal:

- `projeto_energia/`

Submodulos:

- `dados/`: ingestao e validacao;
- `processamento/`: limpeza e transformacoes;
- `analise/`: funcoes de analise exploratoria;
- `analise/indicadores.py`: atributos temporais, indicadores energeticos, regimes, picos e tabelas para interpretacao futura;
- `analise/anomalias.py`: deteccao de anomalias por Z-score e Isolation Forest;
- `analise/clusterizacao.py`: agrupamento de perfis por K-Means;
- `interpretacao_llm/`: contratos para integracao futura com LLM;
- `relatorios/`: estruturas iniciais para relatorios tecnicos.
- `pipeline.py`: fluxo consolidado de ingestao, processamento, analise e geracao de relatorio.

Execucao direta pelo pacote:

```powershell
$env:PYTHONPATH="src"
python -m projeto_energia
```
