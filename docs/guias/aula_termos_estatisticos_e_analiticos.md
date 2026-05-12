# Aula de Termos Estatisticos e Analiticos Usados no Notebook

Este material foi escrito como uma aula introdutoria para explicar os termos estatisticos e analiticos usados no notebook de analise de consumo de energia.

O foco aqui e responder quatro perguntas para cada termo:

1. o que significa;
2. como e calculado;
3. qual funcao foi usada no notebook;
4. como interpretar no contexto do projeto.

---

## 1. Estatisticas descritivas

Estatisticas descritivas sao medidas usadas para resumir um conjunto de dados.

Elas ajudam a responder perguntas como:

- qual e o valor tipico?
- os dados variam muito?
- existem valores muito altos ou muito baixos?
- a distribuicao parece equilibrada ou puxada para um lado?

### 1.1 Contagem

O que significa:

- quantidade de valores validos em uma coluna.

Como e calculado:

- conta quantos valores nao sao nulos.

Funcao usada no notebook:

- `serie.count()`

Exemplo simples:

- valores: `2, 4, NaN, 8`
- contagem = `3`

Interpretacao:

- se a contagem e menor que o numero total de linhas, existem faltantes.

### 1.2 Media

O que significa:

- valor medio do conjunto.

Como e calculado:

- soma de todos os valores dividida pela quantidade de valores.

Formula:

```text
media = (x1 + x2 + x3 + ... + xn) / n
```

Funcao usada no notebook:

- `serie.mean()`

Exemplo simples:

- valores: `2, 4, 6`
- media = `(2 + 4 + 6) / 3 = 4`

Interpretacao:

- mostra um valor central, mas pode ser puxada por valores extremos.

### 1.3 Mediana

O que significa:

- valor central do conjunto quando os dados sao colocados em ordem.

Como e calculado:

- primeiro ordena os valores;
- depois pega o valor do meio.

Se houver quantidade impar:

- pega o elemento central.

Se houver quantidade par:

- tira a media dos dois valores centrais.

Funcao usada no notebook:

- `serie.median()`

Exemplo 1:

- valores: `1, 3, 9`
- mediana = `3`

Exemplo 2:

- valores: `1, 3, 5, 9`
- mediana = `(3 + 5) / 2 = 4`

Interpretacao:

- costuma representar melhor o “centro real” quando existem picos extremos.

### 1.4 Desvio padrao

O que significa:

- mede o espalhamento dos dados em relacao a media.

Ideia intuitiva:

- se os valores estao todos proximos da media, o desvio padrao e pequeno;
- se os valores estao muito espalhados, o desvio padrao e grande.

Como e calculado, em ideia:

1. calcula a media;
2. mede a distancia de cada valor ate a media;
3. eleva essas distancias ao quadrado;
4. tira a media dessas distancias;
5. tira a raiz quadrada.

Funcao usada no notebook:

- `serie.std()`

Interpretacao:

- ajuda a entender estabilidade ou variacao do consumo.

### 1.5 Minimo

O que significa:

- menor valor observado.

Funcao usada no notebook:

- `serie.min()`

Interpretacao:

- mostra o ponto mais baixo da serie.

### 1.6 Maximo

O que significa:

- maior valor observado.

Funcao usada no notebook:

- `serie.max()`

Interpretacao:

- ajuda a localizar picos de consumo.

### 1.7 Quartil 25%

O que significa:

- valor abaixo do qual estao 25% dos dados.

Funcao usada no notebook:

- `serie.quantile(0.25)`

Interpretacao:

- ajuda a entender a distribuicao dos valores mais baixos.

### 1.8 Quartil 75%

O que significa:

- valor abaixo do qual estao 75% dos dados.

Funcao usada no notebook:

- `serie.quantile(0.75)`

Interpretacao:

- ajuda a entender onde estao os valores mais altos, sem usar o maximo.

### 1.9 Como entender os quartis com um exemplo

Imagine os valores ordenados:

```text
1, 2, 3, 4, 5, 6, 7, 8
```

Em ideia:

- quartil 25% fica perto da parte onde um quarto dos dados ja apareceu;
- quartil 75% fica perto da parte onde tres quartos dos dados ja apareceram.

Na pratica, o software faz esse calculo com regras internas de interpolacao, especialmente quando a posicao exata nao cai em um valor inteiro da lista.

### 1.10 Assimetria

O que significa:

- mostra se a distribuicao puxa mais para a esquerda ou para a direita.

Funcao usada no notebook:

- `serie.skew()`

Interpretacao:

- valor positivo: muitos valores baixos e alguns muito altos;
- valor negativo: muitos valores altos e alguns muito baixos;
- perto de zero: distribuicao mais equilibrada.

No seu dataset, a potencia ativa teve assimetria positiva.

Isso quer dizer:

- muitos consumos mais baixos;
- alguns picos altos puxando a distribuicao para a direita.

### 1.11 Curtose

O que significa:

- indica o peso das caudas da distribuicao e a presenca de extremos.

Funcao usada no notebook:

- `serie.kurtosis()`

Interpretacao intuitiva:

- curtose maior sugere maior presenca de extremos;
- curtose menor sugere distribuicao menos concentrada em extremos.

---

## 2. Tipos de media usados no notebook

### 2.1 Media simples

O que e:

- a media comum de uma coluna inteira.

Funcao:

- `mean()`

Exemplo no notebook:

- media da `Potencia ativa global (kW)` em toda a base.

### 2.2 Media por grupo

O que e:

- media calculada dentro de grupos.

Exemplo:

- media por hora;
- media por dia da semana;
- media por mes;
- media por periodo do dia.

Funcoes usadas:

- `groupby(...)`
- `agg(...)`
- `mean()`

Exemplo de ideia:

```python
dados.groupby("hora")[COLUNA_ALVO].mean()
```

Isso significa:

- junta todos os registros da mesma hora;
- calcula a media do consumo para cada hora.

### 2.3 Media movel

O que e:

- media calculada numa janela que vai andando ao longo da serie temporal.

Exemplo de ideia:

- em vez de olhar um ponto isolado, voce olha os ultimos 60 pontos e calcula a media deles.

Funcao usada:

- `rolling(...).mean()`

Exemplo do notebook:

```python
dados["media_movel_potencia"] = dados[COLUNA_ALVO].rolling(JANELA_MOVEL, min_periods=5).mean()
```

Interpretacao:

- suaviza a serie;
- ajuda a ver tendencia.

### 2.4 Media por hora para imputacao

O que e:

- preenchimento de faltantes usando a media dos valores daquela mesma hora.

Exemplo:

- se falta um valor as 18h, o notebook pode preencher usando a media dos valores observados as 18h em outros dias.

Funcao usada:

- `groupby("hora")[coluna].transform("mean")`

Interpretacao:

- e uma forma mais contextual de imputacao do que usar a media global.

---

## 3. Agrupamentos estatisticos

No notebook, foram feitos agrupamentos por:

- hora
- dia da semana
- mes
- periodo do dia
- regime de consumo

### Como funciona um agrupamento

Exemplo:

```python
perfil_por_hora = dados.groupby("hora")[COLUNA_ALVO].agg(["mean", "median", "std", "min", "max", "count"])
```

O que isso faz:

1. separa os dados em grupos de mesma hora;
2. para cada grupo, calcula:
   - media
   - mediana
   - desvio padrao
   - minimo
   - maximo
   - contagem

Interpretacao:

- isso transforma a serie completa em um resumo por hora.

---

## 4. Analise temporal

### 4.1 Delta

O que significa:

- diferenca entre o valor atual e o valor anterior.

Formula:

```text
delta = valor_atual - valor_anterior
```

Funcao usada:

- `diff()`

Exemplo:

- se a potencia era `1,2` e passou para `1,5`
- delta = `0,3`

Interpretacao:

- positivo = aumento;
- negativo = queda.

### 4.2 Taxa de variacao

O que significa:

- variacao relativa em relacao ao valor anterior.

Formula:

```text
taxa = (valor_atual - valor_anterior) / valor_anterior
```

Funcao usada:

- `pct_change()`

Interpretacao:

- mostra o quanto o valor cresceu ou caiu proporcionalmente.

### 4.3 Defasagem (lag)

O que significa:

- comparar o valor atual com valores do passado.

Exemplo:

- lag 1 = valor anterior;
- lag 5 = valor de 5 registros antes;
- lag 60 = valor de 60 registros antes.

Funcao usada:

- `shift(lag)`

Exemplo do notebook:

```python
dados[f"potencia_ativa_defasagem_{defasagem}"] = dados[COLUNA_ALVO].shift(defasagem)
```

Interpretacao:

- ajuda a estudar memoria temporal da serie.

### 4.4 Janela movel

O que significa:

- bloco de observacoes recentes usado para calculos locais.

No notebook:

- janela de 60 observacoes.

Funcoes usadas:

- `rolling(...).mean()`
- `rolling(...).std()`
- `rolling(...).max()`
- `rolling(...).min()`

Interpretacao:

- mostra comportamento recente, nao global.

---

## 5. Correlacao

### 5.1 Correlacao de Pearson

O que significa:

- mede relacao linear entre duas variaveis.

Faixa:

- `1`: relacao positiva forte
- `-1`: relacao negativa forte
- `0`: pouca relacao linear

Funcao usada:

- `corr(method="pearson")`

Exemplo:

- se corrente e potencia sobem juntas, a correlacao tende a ser alta e positiva.

Interpretacao:

- positiva: sobem juntas;
- negativa: uma sobe quando a outra desce;
- perto de zero: relacao linear fraca.

### 5.2 Correlacao entre variaveis eletricas

O notebook calculou:

- correlacao entre potencia, tensao, corrente e submetragens.

Funcao:

- `dados.select_dtypes(include=[np.number]).corr(method="pearson")`

### 5.3 Correlacao entre submetragens e consumo total

O notebook usou:

- tabela de correlacao entre `Sub_metering_1`, `Sub_metering_2`, `Sub_metering_3` e `Global_active_power`.

### 5.4 Correlacao com defasagens

O notebook comparou:

- consumo atual
- consumo com lag 1
- consumo com lag 5
- consumo com lag 15
- consumo com lag 60

Interpretacao:

- quanto maior a correlacao com defasagens curtas, maior a dependencia temporal imediata.

---

## 6. Tratamento de valores ausentes

### 6.1 `drop`

O que faz:

- remove linhas com faltantes.

Funcao:

- `dropna()`

Risco:

- pode perder muitos dados.

### 6.2 `ffill`

O que faz:

- preenche usando o valor anterior.

Funcao:

- `ffill()`

Interpretacao:

- assume continuidade local.

### 6.3 `bfill`

O que faz:

- preenche usando o valor seguinte.

Funcao:

- `bfill()`

### 6.4 `interpolate`

O que faz:

- cria um valor intermediario estimado entre pontos conhecidos.

Funcao:

- `interpolate(method="time")`

Interpretacao:

- bom para series temporais quando se quer suavidade entre observacoes.

### 6.5 `mean_by_hour`

O que faz:

- preenche faltantes com a media daquela mesma hora.

Base de calculo:

- usa o grupo da coluna `hora`.

Interpretacao:

- tenta respeitar o padrao horario da serie.

---

## 7. Anomalias

### 7.1 Z-score

O que significa:

- quantos desvios padrao um valor esta distante da media.

Formula conceitual:

```text
z = (valor - media) / desvio_padrao
```

No notebook:

- foi usado o valor absoluto;
- valores acima do limiar foram marcados como anomalia.

Funcao usada:

- `stats.zscore(...)`

### 7.2 Limiar

O que e:

- valor de corte usado para decidir o que sera considerado anomalia.

No notebook:

- `3.0`

Interpretacao:

- se um ponto estiver mais de 3 desvios padrao longe da media, ele entra como anomalia.

### 7.3 Isolation Forest

O que e:

- metodo de aprendizado de maquina para detectar observacoes raras.

Ideia intuitiva:

- pontos muito diferentes dos demais sao mais faceis de “isolar”.

Funcao usada:

- `IsolationForest(...)`

Interpretacao:

- olha varias variaveis ao mesmo tempo;
- por isso, detecta anomalias multivariadas.

---

## 8. Segmentacao de consumo

### 8.1 Quartis para criar regimes

O notebook dividiu a potencia ativa em:

- baixo
- moderado
- alto

Como foi feito:

- ate o quartil 25% = baixo;
- acima do quartil 75% = alto;
- entre eles = moderado.

Interpretacao:

- isso nao representa uma classificacao fisica da casa;
- e uma segmentacao estatistica da distribuicao dos dados.

---

## 9. Clusterizacao

### 9.1 KMeans

O que e:

- algoritmo que agrupa observacoes parecidas.

Ideia:

- cada grupo tenta reunir pontos com comportamento semelhante.

Funcao usada:

- `KMeans(...)`

### 9.2 Padronizacao

O que e:

- colocar as variaveis em escala comparavel.

Por que isso importa:

- uma coluna em volts pode ter valores muito maiores do que uma coluna em kvar;
- sem padronizar, variaveis com numeros maiores dominam o agrupamento.

Funcao usada:

- `StandardScaler()`

### 9.3 PCA

O que e:

- tecnica de reducao de dimensionalidade.

Ideia:

- pega varias variaveis e as resume em poucos eixos principais.

Funcao usada:

- `PCA(n_components=2)`

Interpretacao:

- serve para visualizar grupos em 2D;
- nao substitui os dados originais, apenas resume visualmente a estrutura.

---

## 10. Novos termos usados nas analises adicionadas depois

### 10.1 Curva de carga

O que e:

- grafico ou tabela que mostra como o consumo medio varia ao longo das horas do dia.

Como foi calculada no notebook:

- agrupando os dados por `hora`;
- e, em uma analise mais nova, por `hora` e `fim_de_semana`.

Interpretacao:

- permite enxergar a rotina energetica da residencia;
- mostra em quais horarios a carga costuma ser maior ou menor.

### 10.2 Tipo de dia

No notebook:

- `dia util`
- `fim de semana`

Como foi definido:

- usando a coluna `fim_de_semana`, em que:
  - `0` = dia util
  - `1` = fim de semana

Interpretacao:

- ajuda a verificar se o comportamento da residencia muda conforme o tipo de dia.

### 10.3 Energia diaria aproximada

O que e:

- uma estimativa da energia consumida ao longo de um dia.

Como foi calculada no notebook:

```python
dados[COLUNA_ALVO].resample("D").sum() / 60
```

Explicacao:

- o notebook somou os valores de potencia ativa do dia;
- depois dividiu por `60` para obter uma aproximacao em `kWh`, considerando a resolucao temporal da base.

Interpretacao:

- serve para comparar dias inteiros entre si;
- e diferente de olhar apenas um pico instantaneo.

### 10.4 Potencia media diaria

O que e:

- media da potencia ativa ao longo de um dia.

Funcao usada:

- `resample("D").mean()`

Interpretacao:

- resume o nivel medio de carga do dia.

### 10.5 Potencia maxima diaria

O que e:

- maior valor instantaneo de potencia observado naquele dia.

Funcao usada:

- `resample("D").max()`

Interpretacao:

- ajuda a identificar se o dia teve um pico muito intenso.

### 10.6 Ranking de dias

O que e:

- ordenacao dos dias do maior para o menor consumo, ou do menor para o maior.

Funcao usada:

- `sort_values(...)`

Interpretacao:

- ajuda a descobrir os dias mais pesados e os dias mais leves do periodo analisado.

### 10.7 Percentil

O que e:

- valor abaixo do qual esta uma certa porcentagem dos dados.

Exemplo:

- percentil 95 = valor abaixo do qual estao 95% dos dados.

Funcao usada:

- `quantile(0.95)`

Interpretacao:

- se um ponto fica acima do percentil 95, ele esta entre os 5% maiores valores da serie.

### 10.8 Limiar de pico

O que e:

- valor de corte usado para separar eventos normais de eventos considerados pico.

No notebook:

- foi usado o percentil 95 da potencia ativa.

Interpretacao:

- qualquer ponto acima desse limiar foi tratado como evento de pico.

### 10.9 Quantidade de picos por hora

O que e:

- contagem de quantos eventos de pico ocorreram em cada hora do dia.

Como foi calculada:

- depois de selecionar os pontos acima do limiar de pico;
- o notebook agrupou esses eventos por `hora` e contou quantos havia em cada grupo.

Interpretacao:

- mostra em quais horarios os picos tendem a se concentrar.

### 10.10 Participacao percentual aproximada

O que e:

- estimativa da participacao de cada submedicao no consumo total do instante.

Como foi calculada no notebook:

```text
participacao (%) = 100 * submedicao / energia_total_estimativa_do_instante
```

Interpretacao:

- ajuda a comparar o peso relativo das submetragens;
- e uma medida aproximada, nao uma decomposicao exata.

### 10.11 Resample diario

O que e:

- agregacao dos dados por dia.

Funcao usada:

- `resample("D")`

Interpretacao:

- transforma a serie em blocos diarios;
- permite calcular soma, media e maximo por dia.

### 10.12 Dia de maior consumo e dia de menor consumo

O que e:

- comparacao entre os extremos da serie diaria.

Como foi calculado:

- depois de montar a tabela diaria, o notebook procurou:
  - o maior valor de `energia_diaria_aprox_kwh`;
  - o menor valor de `energia_diaria_aprox_kwh`.

Funcoes usadas:

- `idxmax()`
- `idxmin()`

Interpretacao:

- isso ajuda a localizar os dias mais intensos e os dias mais leves do periodo analisado.

### 10.13 Submedicao de maior valor no dia

O que e:

- entre as submetragens do dia, qual teve a maior soma.

Como foi calculado:

- o notebook somou as submetragens por dia;
- depois usou a maior entre elas.

Funcao usada:

- `idxmax()`

Interpretacao:

- ajuda a identificar qual parte medida da residencia pareceu mais ativa naquele dia extremo.

### 10.14 Submedicao de menor valor no dia

O que e:

- entre as submetragens do dia, qual teve a menor soma.

Funcao usada:

- `idxmin()`

Interpretacao:

- ajuda a identificar qual submedicao teve menor presenca naquele dia.

---

## 11. Funcoes principais usadas no notebook

Aqui vai um resumo rapido das funcoes mais importantes:

- `count()` = conta valores validos
- `mean()` = calcula media
- `median()` = calcula mediana
- `std()` = calcula desvio padrao
- `min()` = menor valor
- `max()` = maior valor
- `quantile()` = calcula quartis ou outros percentis
- `skew()` = calcula assimetria
- `kurtosis()` = calcula curtose
- `groupby()` = agrupa dados
- `agg()` = aplica varias estatisticas de uma vez
- `diff()` = calcula diferenca entre valores consecutivos
- `pct_change()` = calcula taxa de variacao
- `shift()` = cria defasagens
- `rolling()` = cria janela movel
- `corr()` = calcula correlacao
- `resample()` = agrega a serie temporal por periodo, como dia ou mes
- `dropna()` = remove faltantes
- `ffill()` = preenche com valor anterior
- `bfill()` = preenche com valor seguinte
- `interpolate()` = interpola faltantes
- `stats.zscore()` = calcula z-score
- `IsolationForest()` = detecta anomalias multivariadas
- `KMeans()` = faz clusterizacao
- `StandardScaler()` = padroniza variaveis
- `PCA()` = reduz dimensoes para visualizacao
- `idxmax()` = localiza o indice do maior valor
- `idxmin()` = localiza o indice do menor valor

---

## 12. Resumo final da aula

O notebook usou:

- estatisticas descritivas para resumir as variaveis;
- agrupamentos para estudar comportamento por tempo e por regime;
- analise temporal para medir variacao e memoria da serie;
- correlacao para entender associacoes entre variaveis;
- curva de carga e agregacoes diarias para entender rotina e intensidade de uso;
- tratamento de faltantes para manter a base consistente;
- deteccao de anomalias para encontrar pontos raros;
- clusterizacao para identificar perfis de consumo semelhantes.

Em termos simples:

- ele nao apenas mostrou graficos;
- ele calculou varias medidas para transformar os dados brutos em informacao interpret?vel.

Esse e exatamente o tipo de base analitica que depois pode ser usada por um modulo de interpretacao automatica com LLM.
