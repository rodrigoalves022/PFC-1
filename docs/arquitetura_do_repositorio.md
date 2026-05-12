# Arquitetura do Repositorio

## Objetivo desta organizacao

A estrutura do repositorio foi pensada para o PFC 1, com foco em clareza academica, evolucao incremental e separacao entre:

- dados do estudo;
- documentos do projeto;
- exploracao inicial;
- codigo-fonte reutilizavel.

## Visao geral das pastas

### `data/`

Armazena os arquivos de dados do projeto.

Uso atual:
- `household_power_consumption.txt`, dataset do estudo de caso inicial.

### `docs/`

Reune a documentacao do PFC.

Uso atual:
- planejamento tecnico;
- descricao da arquitetura;
- documentos institucionais;
- notas e ideias de analise.

### `notebooks/`

Espaco para exploracao interativa, testes de hipoteses e registros visuais iniciais.

Uso atual:
- notebook de analise exploratoria do dataset UCI.

### `scripts/`

Contem scripts simples para executar rotinas do projeto sem depender do notebook.

Uso atual:
- script de carga, limpeza e resumo exploratorio inicial.

### `src/`

Contem o codigo-fonte Python do projeto.

O pacote principal e `projeto_energia`, dividido em modulos:

- `dados/`: ingestao e validacao do dataset
- `processamento/`: limpeza e transformacoes
- `analise/`: estatisticas e agregacoes exploratorias
- `interpretacao_llm/`: contratos para futura camada de interpretacao
- `relatorios/`: estruturas para relatorio tecnico

### `tests/`

Reservada para testes automatizados futuros. No PFC 1, essa pasta existe para preparar a evolucao do projeto.

## Fluxo tecnico atual

1. O arquivo bruto e armazenado em `data/`.
2. O modulo `dados/ingestao.py` carrega e valida o arquivo.
3. O modulo `processamento/limpeza.py` padroniza os dados.
4. O modulo `analise/exploratoria.py` produz resumos e agregacoes iniciais.
5. O notebook ou o script em `scripts/` consome esses modulos.

## Decisao de projeto importante

A pasta `data/` da raiz guarda arquivos do dataset.

A pasta `src/projeto_energia/dados/` guarda codigo Python de ingestao.

Essa separacao evita misturar arquivo bruto com regra de negocio e facilita a evolucao para o PFC 2.
