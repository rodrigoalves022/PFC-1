# Roteiro de Analises para o PFC 1

Este documento organiza, em formato mais executavel, as ideias iniciais de analise do projeto. O foco aqui e separar o que cabe agora no PFC 1, o que pode entrar como extensao planejada e o que deve ficar explicitamente para etapas futuras.

## 1. Leitura geral do material

O arquivo original apresenta uma linha de raciocinio muito boa para o projeto, especialmente por conectar:

- serie temporal;
- engenharia de atributos;
- identificacao de regimes;
- deteccao de anomalias;
- futura interpretacao por LLM.

O ponto mais importante e que ele ja sugere um pipeline completo. Para o PFC 1, porem, esse pipeline precisa ser reduzido a uma versao metodologicamente defensavel e implementavel dentro do escopo atual.

## 2. O que vale seguir agora no PFC 1

Estas trilhas estao muito alinhadas com a fase atual do projeto e podem virar parte do estudo tecnico e da analise inicial:

### 2.1 Pre-processamento e consistencia dos dados

- tratamento de valores ausentes;
- validacao da consistencia temporal;
- criacao de atributos derivados de data e hora;
- organizacao do dataset para exploracao e relatorio.

### 2.2 Analise temporal descritiva

- consumo medio por hora;
- consumo medio por dia da semana;
- consumo medio por mes;
- comparacao entre periodos do dia;
- identificacao de horarios de maior e menor consumo.

### 2.3 Estatistica descritiva ampliada

- media, mediana, desvio padrao, minimo, maximo e quartis;
- distribuicao das variaveis principais;
- analise das submetragens;
- correlacao entre potencia, tensao, corrente e submetragens.

### 2.4 Criacao de indicadores simples

- consumo total observado;
- soma das submetragens;
- estimativa de consumo nao coberto pelas submetragens;
- variacao temporal simples;
- medias moveis.

### 2.5 Estruturacao para interpretacao futura por LLM

- definir quais tabelas e indicadores seriam bons insumos textuais;
- pensar na forma do resumo tecnico que o sistema devera gerar;
- registrar limitacoes e cuidados de interpretacao.

## 3. O que cabe como aprofundamento controlado

Estas ideias sao boas, mas devem ser tratadas com moderacao no PFC 1. Elas podem aparecer como proposta metodologica, prova de conceito simples ou extensao planejada.

### 3.1 Regimes de consumo

Vale a pena seguir, desde que com abordagem simples:

- baixo consumo;
- consumo moderado;
- alto consumo;
- pico.

Sugestao:
usar quantis ou thresholds simples antes de pensar em clustering mais sofisticado.

### 3.2 Deteccao de anomalias

Tambem e viavel, mas de forma inicial:

- Z-score;
- IQR;
- identificacao visual de picos e quedas abruptas.

Sugestao:
evitar comecar por `Isolation Forest` ou `Local Outlier Factor`, pois isso ja aproxima demais o trabalho de uma etapa mais avancada de modelagem.

### 3.3 Autocorrelacao e sazonalidade

E uma trilha interessante para dar mais profundidade a analise temporal. Pode ser incluida se houver tempo, mas nao precisa ser o primeiro foco.

## 4. O que eu deixaria para depois

Estas ideias sao validas, mas provavelmente grandes demais para a etapa atual se tentarmos implementa-las de forma completa:

- previsao de consumo;
- classificacao de tipo de edificacao;
- deteccao automatica de equipamentos;
- integracao com IoT;
- sistema de recomendacao energetica;
- clustering completo com comparacao entre varios algoritmos;
- pipeline completo de interpretacao automatica por LLM ja operacional.

No PFC 1, essas partes funcionam melhor como:

- visao de continuidade;
- proposta para o PFC 2;
- justificativa de arquitetura modular.

## 5. Cuidados importantes com algumas ideias do arquivo

### 5.1 "Padroes industriais vs residenciais"

Isso nao combina bem com o dataset atual, porque a base e residencial. No maximo, pode-se falar em "padroes de carga mais intensos ou mais estaveis", sem sugerir classificacao industrial.

### 5.2 "Motores ligados" e "equipamentos pesados"

Essas leituras podem ser usadas como hipotese interpretativa, nunca como conclusao direta. O dataset nao mede equipamento individual.

### 5.3 "Consumo nao medido"

Essa ideia e muito boa, mas precisa de cuidado com unidade e formulacao. Como o dataset mistura potencia global e submetragens em escalas diferentes, sera preciso padronizar corretamente antes de calcular esse indicador.

### 5.4 "Interpretacao via LLM"

Isso deve entrar no PFC 1 como especificacao de fluxo e contrato de entrada e saida, nao como modulo final ja concluido.

## 6. Melhor sequencia de execucao

Se eu fosse transformar suas ideias em trilha de trabalho, seguiria nesta ordem:

1. limpeza e enriquecimento temporal do dataset;
2. analise descritiva por hora, dia da semana e mes;
3. criacao de indicadores derivados simples;
4. tabelas e visualizacoes mais interpretaveis;
5. definicao simples de regimes de consumo;
6. deteccao inicial de anomalias;
7. desenho do formato de saida para futura interpretacao por LLM.

## 7. Proposta objetiva do que seguir agora

As tres frentes mais fortes para o proximo ciclo sao:

### Frente A. Analise temporal

- hora do dia;
- dia da semana;
- mes;
- periodos do dia.

### Frente B. Indicadores derivados

- soma das submetragens;
- diferenca entre consumo total e submetido;
- variacao temporal;
- media movel.

### Frente C. Regimes e eventos

- classificacao simples em faixas de consumo;
- picos;
- quedas abruptas;
- eventos que possam virar texto tecnico no futuro.

## 8. Conclusao pratica

As ideias iniciais de analise funcionam melhor como fonte para um recorte metodologico mais enxuto. A melhor estrategia agora nao e tentar executar tudo, mas priorizar o que sustenta o PFC 1 com clareza.

Se formos seguir com consistencia no PFC 1, o melhor caminho e:

- aprofundar a analise temporal;
- criar indicadores interpretaveis;
- testar uma classificacao simples de regimes;
- deixar clustering avancado, previsao e LLM completo para etapa posterior.
