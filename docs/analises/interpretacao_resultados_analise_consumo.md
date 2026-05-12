# Interpretacao Didatica dos Resultados do Notebook de Analise de Consumo

Este documento foi feito para ajudar na leitura do notebook `notebooks/analise_consumo_energia_edificacoes.ipynb` de forma mais didatica.

A ideia aqui e explicar:

- o que significa cada coluna principal;
- o que significam os termos estatisticos usados;
- como os calculos foram feitos;
- o que os resultados representam na pratica;
- o que pode ou nao pode ser concluido a partir deles.

Este texto assume que voce ainda esta consolidando a base de estatistica e analise de dados.

## 1. O que e este dataset

O arquivo usado no projeto e o `household_power_consumption.txt`, um dataset da UCI com medidas de consumo eletrico de uma residencia ao longo do tempo.

Cada linha representa uma observacao em um instante de tempo.

No dataset original, as principais colunas sao:

- `Date`: data do registro;
- `Time`: horario do registro;
- `Global_active_power`: potencia ativa global;
- `Global_reactive_power`: potencia reativa global;
- `Voltage`: tensao eletrica;
- `Global_intensity`: corrente eletrica;
- `Sub_metering_1`: submedicao 1;
- `Sub_metering_2`: submedicao 2;
- `Sub_metering_3`: submedicao 3.

No notebook, essas colunas continuam existindo para os calculos, mas varios nomes foram traduzidos para facilitar a leitura dos graficos e tabelas.

## 2. O que significa cada coluna principal

### `Global_active_power`

Nome de exibicao:

- `Potencia ativa global (kW)`

O que significa:

- e a potencia realmente consumida pela residencia;
- representa o uso efetivo de energia pelos equipamentos.

Unidade:

- `kW` (quilowatts)

Interpretacao simples:

- quanto maior esse valor, maior o consumo instantaneo util da residencia.

### `Global_reactive_power`

Nome de exibicao:

- `Potencia reativa global (kvar)`

O que significa:

- e uma componente eletrica associada ao funcionamento de certas cargas, especialmente cargas indutivas ou capacitivas;
- nao representa diretamente “consumo util” no mesmo sentido da potencia ativa.

Interpretacao simples:

- ajuda a entender o comportamento eletrico da instalacao, mas costuma ser menos intuitiva que a potencia ativa.

### `Voltage`

Nome de exibicao:

- `Tensao (V)`

O que significa:

- e a tensao eletrica da rede.

Unidade:

- `V` (volts)

Interpretacao simples:

- e como se fosse a “pressao eletrica” disponivel no sistema.

### `Global_intensity`

Nome de exibicao:

- `Corrente global (A)`

O que significa:

- e a corrente eletrica total consumida.

Unidade:

- `A` (ampere)

Interpretacao simples:

- mostra quanta corrente esta circulando;
- em geral, quando o consumo aumenta, a corrente tambem tende a aumentar.

### `Sub_metering_1`, `Sub_metering_2` e `Sub_metering_3`

Nomes de exibicao:

- `Submedicao 1 - cozinha (Wh)`
- `Submedicao 2 - lavanderia (Wh)`
- `Submedicao 3 - aquecimento/climatizacao (Wh)`

O que significam:

- sao medidas parciais de partes especificas da residencia;
- ajudam a observar como alguns subconjuntos de cargas contribuem para o consumo.

Interpretacao simples:

- se uma submedicao aumenta muito em certos momentos, isso sugere participacao importante daquele conjunto de equipamentos.

Importante:

- as tres submetragens nao cobrem necessariamente toda a residencia;
- por isso, parte do consumo pode ficar fora delas.

## 3. Colunas criadas no notebook

O notebook criou varias colunas novas para enriquecer a analise.

### `data_hora`

O que e:

- junção de `Date` com `Time`.

Para que serve:

- permitir ordenar corretamente a serie temporal;
- facilitar agrupamentos por hora, dia, mes e periodo do dia.

### `ano`, `mes`, `dia`, `hora`, `minuto`

O que sao:

- recortes temporais extraidos da coluna `data_hora`.

Para que servem:

- responder perguntas como:
  - em qual hora se consome mais?
  - em qual mes se consome menos?
  - qual o comportamento por dia da semana?

### `dia_semana`

O que e:

- numero do dia da semana.

No notebook:

- `0` = segunda-feira
- `1` = terca-feira
- ...
- `6` = domingo

### `nome_dia_semana`

O que e:

- nome do dia da semana em texto.

### `fim_de_semana`

O que e:

- indicador binario:
  - `0` = nao e fim de semana
  - `1` = e fim de semana

### `periodo_dia`

O que e:

- classificacao do horario em faixas:
  - madrugada
  - manha
  - tarde
  - noite

Como foi definido:

- `0` a `5` horas = madrugada
- `6` a `11` = manha
- `12` a `17` = tarde
- `18` em diante = noite

### `submedicao_total`

O que e:

- soma das tres submetragens.

Como foi calculado:

`Sub_metering_1 + Sub_metering_2 + Sub_metering_3`

Para que serve:

- dar uma ideia do quanto dessas tres areas ou grupos de equipamentos explicam o consumo observado.

### `consumo_nao_medido_aprox`

O que e:

- estimativa aproximada do consumo que nao aparece nas tres submetragens.

Como foi calculado no notebook:

`Global_active_power - submedicao_total / 1000`

Interpretacao:

- tenta aproximar a parte do consumo total que nao esta coberta pelas submetragens.

Importante:

- esse indicador e util para estudo exploratorio;
- ele nao deve ser tratado como medicao exata sem mais validacao.

### `delta_potencia`

O que e:

- diferenca entre a potencia ativa atual e a potencia ativa do instante anterior.

Como foi calculado:

`valor atual - valor anterior`

Interpretacao:

- positivo: o consumo aumentou;
- negativo: o consumo diminuiu;
- perto de zero: pouca mudanca.

### `taxa_variacao_potencia`

O que e:

- variacao relativa da potencia ativa em relacao ao instante anterior.

Interpretacao:

- mede crescimento ou queda em termos proporcionais, nao apenas absolutos.

### `media_movel_potencia`

O que e:

- media da potencia ativa em uma janela de observacoes anteriores.

Como foi calculado no notebook:

- janela de `60` registros

Interpretacao:

- suaviza a serie;
- ajuda a enxergar tendencia, sem tanto ruido ponto a ponto.

### `desvio_movel_potencia`

O que e:

- desvio padrao da potencia ativa dentro da janela movel.

Interpretacao:

- mostra se o consumo esta mais estavel ou mais variavel naquele trecho.

### `maximo_movel_potencia` e `minimo_movel_potencia`

O que sao:

- maior e menor valor da potencia ativa dentro da janela movel.

Interpretacao:

- ajudam a ver faixa recente de variacao.

### `regime_consumo`

O que e:

- classificacao simples do consumo em tres categorias:
  - baixo
  - moderado
  - alto

Como foi calculado:

- com base nos quartis da potencia ativa.

Interpretacao:

- nao e uma classificacao “oficial” da residencia;
- e apenas uma forma simples de separar niveis de consumo.

## 4. O que significam os termos estatisticos usados

### Media

O que e:

- a soma de todos os valores dividida pela quantidade de valores.

Exemplo simples:

- valores: `2, 4, 6`
- media = `(2 + 4 + 6) / 3 = 4`

No projeto:

- quando o notebook fala “consumo medio por hora”, ele soma todos os consumos daquela hora ao longo da base e divide pela quantidade de registros daquela hora.

### Mediana

O que e:

- o valor central quando os dados sao colocados em ordem.

Interpretacao:

- e menos sensivel a picos extremos do que a media.

### Desvio padrao

O que e:

- medida de dispersao.

Interpretacao simples:

- baixo desvio padrao = valores mais concentrados;
- alto desvio padrao = valores mais espalhados.

### Minimo e maximo

O que sao:

- menor valor observado;
- maior valor observado.

### Quartil 25 e quartil 75

O que sao:

- `quartil 25`: ponto abaixo do qual estao 25% dos dados;
- `quartil 75`: ponto abaixo do qual estao 75% dos dados.

Interpretacao:

- ajudam a entender distribuicao sem depender apenas da media.

### Assimetria

O que e:

- medida de quanto a distribuicao puxa mais para um lado.

Interpretacao simples:

- assimetria positiva: muitos valores baixos e alguns muito altos;
- assimetria negativa: muitos valores altos e alguns muito baixos.

### Curtose

O que e:

- medida relacionada ao peso das caudas e presenca de extremos.

Interpretacao simples:

- ajuda a perceber se existem muitos valores extremos em comparacao com uma distribuicao mais regular.

### Correlacao

O que e:

- medida de associacao entre duas variaveis.

Faixa:

- vai de `-1` a `1`

Interpretacao:

- perto de `1`: quando uma sobe, a outra tende a subir;
- perto de `-1`: quando uma sobe, a outra tende a cair;
- perto de `0`: pouca relacao linear.

Importante:

- correlacao nao prova causa;
- ela indica associacao, nao explicacao definitiva.

### Z-score

O que e:

- medida de quantos desvios padrao um valor esta distante da media.

Interpretacao:

- z-score alto sugere um valor incomum;
- no notebook, valores acima do limiar definido foram marcados como anomalias.

## 5. O que o notebook fez em cada etapa

## 5.1 Carga e limpeza

O notebook:

- leu o arquivo bruto;
- converteu data e hora em uma coluna temporal;
- transformou as colunas numericas em numeros de fato;
- ordenou os dados no tempo;
- tratou valores ausentes;
- criou variaveis novas para analise.

Resultado:

- base inicial: `2.075.259` linhas e `9` colunas;
- base enriquecida: `2.075.259` linhas e `27` colunas.

Interpretacao:

- houve ganho de informacao analitica sem perda relevante de dados.

## 5.2 Qualidade dos dados

O notebook mostrou a quantidade e o percentual de valores ausentes por coluna.

O que apareceu:

- as colunas principais ficaram completas;
- os poucos faltantes remanescentes ficaram nas colunas derivadas de diferenca e janela movel.

Por que isso acontece:

- a primeira diferenca precisa de um valor anterior;
- a media movel precisa de uma quantidade minima de registros anteriores.

O notebook tambem verificou:

- se o indice temporal esta em ordem;
- se ha timestamps repetidos.

Resultados:

- indice crescente: `True`
- duplicatas: `0`

Interpretacao:

- a base esta adequada para analises temporais.

## 5.3 Estatistica descritiva

### Potencia ativa global

Resultados:

- media: `1,090`
- mediana: `0,614`
- maximo: `11,122`

Interpretacao:

- como a media e maior que a mediana, ha assimetria para a direita;
- isso quer dizer que a maior parte do tempo o consumo fica mais baixo, mas existem picos altos puxando a media para cima.

### Potencia reativa global

Resultados:

- media: `0,124`
- mediana: `0,100`

Interpretacao:

- valores geralmente baixos;
- ha alguma variacao, mas sem o mesmo peso da potencia ativa.

### Tensao

Resultados:

- media: `240,833 V`
- mediana: `241,0 V`
- minimo: `223,2 V`
- maximo: `254,15 V`

Interpretacao:

- a tensao se manteve relativamente estavel;
- houve variacao, mas sem comportamento caotico.

### Corrente global

Resultados:

- media: `4,621 A`
- mediana: `2,752 A`
- maximo: `48,4 A`

Interpretacao:

- ha momentos de corrente muito alta;
- isso acompanha o fato de haver picos de consumo.

### Submedicoes

Resultados:

- submedicao 1: media `1,109`, mediana `0`
- submedicao 2: media `1,289`, mediana `0`
- submedicao 3: media `6,442`, mediana `1`

Interpretacao:

- as duas primeiras submetragens passam muito tempo em zero ou perto disso;
- a terceira aparece mais ativa e parece ter peso maior no perfil da residencia.

## 5.4 Sazonalidade

### Por hora

Como foi calculado:

- o notebook agrupou todos os registros da mesma hora;
- depois calculou media, mediana, desvio, minimo, maximo e contagem.

Exemplo:

- para a hora `20`, ele juntou todos os registros feitos em 20h ao longo de todo o periodo;
- em seguida calculou a media desses valores.

Resultado resumido:

- hora de maior consumo medio: `20`
- hora de menor consumo medio: `4`

Interpretacao:

- o periodo noturno concentra mais consumo;
- a madrugada concentra menos consumo.

### Por dia da semana

Como foi calculado:

- o notebook agrupou os registros por `dia_semana`;
- depois aplicou os mesmos calculos de resumo.

Resultado:

- sabado e domingo tiveram medias maiores que a maior parte dos dias uteis.

Interpretacao:

- pode haver mais uso da residencia nos fins de semana.

### Por mes

Como foi calculado:

- agrupamento por `mes`;
- calculo da media e outras estatisticas dentro de cada mes.

Resultado:

- meses como janeiro e fevereiro tiveram medias mais altas;
- julho e agosto tiveram medias menores.

Interpretacao:

- existe variacao sazonal no ano;
- ainda nao se pode afirmar a causa sem contexto adicional.

### Por periodo do dia

Resultado:

- madrugada: `0,510`
- manha: `1,261`
- tarde: `1,071`
- noite: `1,520`

Interpretacao:

- a noite e o periodo mais intenso;
- a madrugada e o mais baixo;
- manha e tarde ficam em niveis intermediarios.

## 5.5 Regimes de consumo

Como foi calculado:

- o notebook pegou os quartis da potencia ativa;
- valores ate o quartil inferior foram rotulados como `baixo`;
- valores acima do quartil superior foram rotulados como `alto`;
- o restante ficou como `moderado`.

Resultado:

- baixo: `524.833` registros
- moderado: `1.030.622`
- alto: `519.804`

Interpretacao:

- isso nao significa tres modos fisicos absolutos da casa;
- e apenas uma forma simples de dividir a serie em faixas de intensidade.

## 5.6 Correlacoes

### Com o consumo total

O notebook calculou a correlacao entre a potencia ativa e outras variaveis numericas.

Resultados mais altos:

- consumo nao medido aproximado: `0,999979`
- corrente global: `0,998887`
- submedicao total: `0,847112`

Interpretacao:

- a corrente global praticamente acompanha a potencia ativa;
- isso faz sentido fisico;
- a soma das submetragens tambem acompanha fortemente o consumo total.

### Com as submetragens

Resultados:

- submedicao 3: `0,639`
- submedicao 1: `0,484`
- submedicao 2: `0,434`

Interpretacao:

- a submedicao 3 e a mais associada ao consumo total;
- isso sugere participacao relevante desse conjunto de cargas.

### Com a tensao

Resultado:

- correlacao: `-0,396`

Interpretacao:

- quando o consumo aumenta, a tensao tende a cair um pouco;
- isso e compatível com comportamento eletrico esperado em muitos cenarios.

### Correlacao com defasagens

Como foi calculado:

- o notebook criou colunas com o valor da potencia ativa deslocado no tempo;
- por exemplo:
  - defasagem 1 = valor do instante anterior;
  - defasagem 5 = valor de 5 registros antes;
  - defasagem 60 = valor de 60 registros antes.

Resultados:

- defasagem 1: `0,968`
- defasagem 5: `0,870`
- defasagem 15: `0,728`
- defasagem 60: `0,495`

Interpretacao:

- o consumo atual se parece muito com o consumo dos instantes imediatamente anteriores;
- isso indica forte dependencia temporal de curto prazo.

## 5.7 Anomalias

### Z-score

Como foi calculado:

- para cada valor da potencia ativa, o notebook mediu quantos desvios padrao ele estava distante da media;
- valores acima do limiar definido foram marcados como anomalia.

Resultado:

- `36.671` anomalias

Interpretacao:

- o metodo encontrou varios picos altos;
- como a distribuicao e assimetrica, nem todo ponto marcado deve ser tratado automaticamente como erro ou evento critico.

### Isolation Forest

Como foi calculado:

- o notebook usou varias colunas ao mesmo tempo;
- o modelo tenta separar comportamentos comuns de comportamentos raros.

Resultado:

- `20.753` anomalias multivariadas

Interpretacao:

- esse metodo olha para o comportamento conjunto das variaveis;
- por isso, pode capturar eventos incomuns que nao aparecem apenas olhando um valor isolado.

## 5.8 Clusterizacao

Como foi calculado:

- o notebook pegou um conjunto de atributos eletricos;
- padronizou os dados;
- aplicou `KMeans` com `4` grupos.

O que isso significa:

- o algoritmo tentou dividir os registros em quatro perfis semelhantes entre si.

Interpretacao dos grupos:

- grupo 0: perfil de consumo mais baixo;
- grupo 2: perfil intermediario;
- grupos 1 e 3: perfis mais intensos.

Importante:

- grupo nao e a mesma coisa que categoria fisica confirmada;
- e uma divisao matematica baseada em semelhanca.

## 5.9 Curva de carga por tipo de dia

O notebook passou a comparar duas curvas medias:

- `dia util`
- `fim de semana`

Como foi calculado:

- primeiro os dados foram agrupados por `fim_de_semana` e `hora`;
- depois foi calculada a media da potencia ativa em cada combinacao.

Em termos simples:

- para cada hora do dia, o notebook calculou uma media para dias uteis e outra para fins de semana.

O que apareceu:

- em varias horas, principalmente no periodo noturno, o fim de semana apresentou consumo medio maior;
- por exemplo, as `20h` ficaram perto de `2,020 kW` no fim de semana contra cerca de `1,838 kW` em dia util.

Interpretacao:

- o uso da residencia parece mudar conforme o tipo de dia;
- fins de semana podem concentrar mais permanencia na casa e mais uso de cargas domesticas.

## 5.10 Consumo diario e ranking de dias

O notebook criou uma tabela diaria com:

- `energia_diaria_aprox_kwh`
- `potencia_media_diaria_kw`
- `potencia_maxima_diaria_kw`

### O que significa cada coluna

`energia_diaria_aprox_kwh`

- representa uma estimativa da energia diaria consumida;
- foi calculada somando a potencia ativa ao longo do dia e dividindo por `60`, considerando a granularidade temporal da base.

`potencia_media_diaria_kw`

- media da potencia ativa naquele dia.

`potencia_maxima_diaria_kw`

- maior valor instantaneo de potencia ativa observado naquele dia.

O que apareceu:

- o dia com maior energia diaria aproximada foi `2006-12-23`;
- alguns dias de agosto de 2008 apareceram entre os menores consumos diarios.

Interpretacao:

- essa tabela ajuda a comparar dias inteiros, e nao apenas minutos isolados;
- ela e util para descobrir dias muito pesados, dias muito leves e variacao global da rotina da residencia.

## 5.11 Dias extremos de consumo e submetragens

O notebook passou a resumir explicitamente:

- o dia de maior consumo diario;
- o dia de menor consumo diario;
- qual submedicao teve o maior valor nesses dias;
- qual submedicao teve o menor valor nesses dias.

Como foi calculado:

1. a tabela diaria completa foi montada com energia aproximada, potencia media e potencia maxima;
2. as submetragens foram agregadas por dia;
3. o notebook localizou:
   - o dia com maior `energia_diaria_aprox_kwh`;
   - o dia com menor `energia_diaria_aprox_kwh`;
4. dentro de cada um desses dias, identificou:
   - a submedicao com maior soma diaria;
   - a submedicao com menor soma diaria.

Por que isso e valido:

- porque conecta o consumo extremo do dia com a estrutura interna do consumo observado;
- em vez de olhar apenas “qual dia gastou mais”, passa a olhar “qual parte medida da residencia mais apareceu nesse dia”.

O que essa analise permite responder:

- em que data ocorreu o maior e o menor consumo;
- em que mes e ano isso aconteceu;
- qual submedicao pareceu mais relevante no dia extremo;
- qual submedicao apareceu menos nesse mesmo dia.

Interpretacao:

- esse tipo de leitura e muito coerente com o tema do PFC, porque ajuda a transformar um numero bruto de consumo em uma leitura mais estruturada do comportamento energetico da edificacao;
- ela continua exploratoria, mas ja se aproxima de um raciocinio diagnostico.

## 5.12 Picos de consumo

O notebook criou uma analise simples de picos.

Como foi calculado:

- foi adotado como pico todo valor acima do percentil `95%` da potencia ativa;
- esse limiar ficou em `3,246 kW`.

O que isso quer dizer:

- se um ponto esta entre os 5% maiores valores da serie, ele passa a ser tratado como evento de pico.

O notebook tambem calculou:

- quantos picos ocorreram em cada hora;
- quais foram os maiores picos registrados.

O que apareceu:

- as horas com mais picos foram `20h`, `21h` e `19h`;
- varios dos maiores picos ocorreram no periodo noturno;
- alguns picos muito altos apareceram tambem em tardes e madrugadas especificas.

Interpretacao:

- os picos nao estao distribuídos de maneira uniforme ao longo do dia;
- existe concentracao de eventos de alta carga no periodo da noite;
- isso reforca a leitura de que a residencia entra em momentos de maior demanda em horarios bem definidos.

## 5.13 Participacao aproximada das submetragens

O notebook criou uma medida de participacao percentual aproximada das submetragens em relacao ao consumo do instante.

Como foi calculado:

1. a potencia ativa foi convertida aproximadamente para energia por minuto;
2. cada submedicao foi dividida por esse valor total estimado;
3. o resultado foi multiplicado por `100`, gerando um percentual aproximado.

Depois disso, o notebook calculou a media desses percentuais por `periodo_dia`.

Resultados medios aproximados:

- madrugada:
  - submedicao 1: `0,35%`
  - submedicao 2: `5,47%`
  - submedicao 3: `14,96%`
- manha:
  - submedicao 1: `1,78%`
  - submedicao 2: `4,41%`
  - submedicao 3: `39,97%`
- tarde:
  - submedicao 1: `2,40%`
  - submedicao 2: `7,28%`
  - submedicao 3: `28,40%`
- noite:
  - submedicao 1: `3,56%`
  - submedicao 2: `5,01%`
  - submedicao 3: `20,63%`

Interpretacao:

- a submedicao 3 se destacou de novo, especialmente pela manha e pela tarde;
- isso sugere que ela tem participacao importante em varios trechos da rotina energetica;
- a submedicao 2 aparece com participacao mais discreta, mas ainda relevante;
- a submedicao 1 tem peso medio menor, embora possa aparecer em eventos especificos.

Importante:

- essa participacao e aproximada e deve ser lida como indicador exploratorio;
- nao e uma decomposicao energetica exata do consumo total.

## 6. O que os resultados dizem sobre a residencia

De forma geral, o notebook sugere que:

- o consumo tem padrao claramente temporal;
- a noite e o principal periodo de carga;
- a madrugada apresenta consumo basal;
- fins de semana mostram maior atividade media;
- a curva de carga muda entre dia util e fim de semana;
- ha sazonalidade no ano;
- ha dias muito mais pesados do que outros quando se olha a energia diaria;
- os dias extremos podem ser descritos tambem pelas submetragens de maior e menor peso;
- existem picos importantes de demanda;
- a submedicao 3 parece desempenhar papel relevante em varios momentos de maior carga.

## 7. O que ainda nao pode ser afirmado com seguranca

Mesmo com todos esses resultados, ainda nao e correto afirmar diretamente:

- qual equipamento especifico estava ligado em cada pico;
- a causa exata das variacoes sazonais;
- que um comportamento corresponde a uma categoria de edificacao diferente;
- que toda anomalia e necessariamente um problema real.

Essas leituras precisam de contexto adicional ou de validacao complementar.

## 8. Como este documento pode te ajudar

Voce pode usar este arquivo de tres formas:

### 1. Para estudar o notebook

Abra o notebook e leia este documento em paralelo.

### 2. Para entender os termos

Quando aparecer um termo como media, mediana, quartil, correlacao ou z-score, consulte a secao correspondente aqui.

### 3. Para escrever o PFC

Este texto pode servir como base para redigir a parte interpretativa da analise exploratoria, depois adaptando a linguagem para um tom mais academico.

## 9. Resumo final em linguagem simples

Se fosse explicar o notebook em poucas frases:

- ele pega os dados brutos de consumo da residencia;
- organiza esses dados no tempo;
- cria variaveis novas para estudar o comportamento ao longo do dia, da semana e do ano;
- mede como as variaveis se relacionam;
- identifica niveis de consumo, picos e comportamentos raros;
- e prepara tabelas que no futuro podem ser interpretadas automaticamente por um LLM.

Se quiser, no proximo passo eu posso fazer uma segunda versao deste arquivo em formato de apostila curta, com exemplos visuais e um glossario final ainda mais simples. 
