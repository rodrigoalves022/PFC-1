# Planejamento Tecnico - PFC 1

## Problema a resolver

O projeto busca estabelecer uma base computacional para analisar dados de consumo de energia eletrica em edificacoes e, futuramente, produzir interpretacoes automatizadas com suporte de modelos de linguagem. No PFC 1, o problema central e estruturar corretamente essa base: definir arquitetura, fluxo de dados, organizacao do repositorio e estudo inicial do dataset.

## Recorte adotado no PFC 1

- estudo de caso com o dataset UCI Household Electric Power Consumption;
- foco em edificacao residencial como instancia inicial do problema;
- preparacao para evolucao futura para outras tipologias de edificacoes;
- sem implementacao completa de agente LLM, RAG ou sistema final de recomendacao.

## Modulos do sistema

### 1. Ingestao de dados

Responsabilidade:
carregar dados brutos, validar existencia de arquivo, padronizar schema minimo e preparar a entrada para processamento.

Entradas:
- arquivo texto bruto do dataset UCI;
- configuracoes de caminho e schema esperado.

Saidas:
- `DataFrame` carregado com tipagem inicial;
- mensagens de erro claras em caso de arquivo ausente ou schema invalido.

### 2. Processamento

Responsabilidade:
realizar limpeza basica, criacao do campo temporal consolidado, coercao numerica e ordenacao cronologica.

Entradas:
- dados brutos ingeridos.

Saidas:
- dados limpos e prontos para analise;
- base consistente para extracao de indicadores.

### 3. Analise

Responsabilidade:
gerar estatisticas descritivas, diagnostico de faltantes, agregacoes temporais e visualizacoes iniciais.

Entradas:
- dados processados.

Saidas:
- metricas exploratorias;
- graficos de consumo e correlacao;
- insumos para interpretacao tecnica.

### 4. Interpretacao por LLM

Responsabilidade:
modulo futuro para traduzir resultados analiticos em texto tecnico interpretavel.

Entradas:
- indicadores numericos;
- resumos estatisticos;
- regras de negocio e contexto de edificacoes.

Saidas:
- rascunhos de diagnostico;
- explicacoes em linguagem natural;
- base para relatorio automatizado.

Observacao:
no PFC 1 este modulo sera apenas especificado arquiteturalmente.

### 5. Geracao de relatorio tecnico

Responsabilidade:
organizar resultados analiticos e, futuramente, interpretacoes em uma estrutura de relatorio.

Entradas:
- resultados da analise;
- interpretacoes textuais;
- metadados do estudo.

Saidas:
- estrutura serializavel de relatorio;
- base para exportacao futura em Markdown, PDF ou interface web.

## Arquitetura inicial proposta

Fluxo principal:

1. `dados/ingestao.py` carrega e valida o dataset.
2. `processamento/limpeza.py` executa limpeza e padronizacao.
3. `analise/exploratoria.py` produz metricas e graficos iniciais.
4. `relatorios/relatorio_tecnico.py` organiza os resultados.
5. `interpretacao_llm/contratos.py` define interfaces futuras para interpretacao assistida.

Essa arquitetura favorece:

- simplicidade academica;
- separacao clara de responsabilidades;
- reuso entre notebook, scripts e futuras APIs;
- evolucao natural para o PFC 2.

## Tecnologias escolhidas

- Python: linguagem principal do projeto
- pandas: manipulacao tabular e temporal
- numpy: operacoes numericas
- matplotlib e seaborn: visualizacao inicial
- scikit-learn: suporte futuro a modelagem e pre-processamento
- Jupyter Notebook: exploracao e documentacao experimental
- Git: versionamento
- ambiente virtual (`venv`): isolamento de dependencias

## Entradas e saidas principais

### Entrada atual

- `data/household_power_consumption.txt`

### Saidas atuais

- tabelas descritivas em memoria;
- graficos exploratorios exibidos em notebook ou script;
- sumario tecnico inicial para futura interpretacao textual.

### Saidas futuras

- base processada persistida;
- indicadores consolidados por periodo;
- diagnosticos em linguagem natural;
- relatorios tecnicos automatizados.

## Limitacoes atuais

- o dataset representa uma residencia e nao cobre toda a diversidade de edificacoes;
- nao ha, nesta etapa, dados contextuais como clima, ocupacao ou tarifa;
- a interpretacao automatizada por LLM ainda nao foi implementada;
- a analise atual e exploratoria e nao deve ser tratada como conclusao definitiva.

## Proximos passos

1. consolidar a exploracao inicial do dataset e registrar achados relevantes;
2. definir schema interno minimo para dados de consumo;
3. decidir formato de persistencia para dados processados;
4. estruturar um conjunto inicial de indicadores energeticos;
5. especificar o contrato de entrada e saida do futuro modulo LLM/RAG;
6. alinhar a arquitetura com os objetivos textuais do PFC 1.
