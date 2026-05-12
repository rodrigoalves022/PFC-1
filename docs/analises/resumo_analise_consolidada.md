# Relatorio Tecnico — Analise de Consumo de Energia Eletrica

**Data de geracao:** 2026-05-12 10:30
**Fonte dos dados:** UCI Household Electric Power Consumption
**Periodo dos dados:** 2006-12-16 a 2010-11-26
**Total de registros:** 2,075,259

---

## Contexto do Estudo

Este relatorio apresenta os resultados da analise exploratoria de consumo de energia eletrica residencial, utilizando o dataset UCI Household Electric Power Consumption como estudo de caso. Os dados foram processados e analisados pelo pipeline computacional do projeto.

---

## Perfil de Consumo por Hora

Media, mediana e desvio padrao da potencia ativa agrupados por hora do dia.

### Perfil por hora

```text
      media  mediana  desvio_padrao  minimo  maximo  contagem
hora                                                         
0     0.659    0.366          0.718   0.078   7.698     85491
1     0.539    0.328          0.586   0.078  10.290     85440
2     0.481    0.320          0.489   0.078   6.248     85439
3     0.445    0.314          0.430   0.078   4.426     85428
4     0.444    0.312          0.425   0.078   4.796     85317
5     0.454    0.310          0.446   0.078   6.376     85260
6     0.792    0.350          0.929   0.078   8.310     85259
7     1.502    1.502          1.082   0.078   9.486     85284
8     1.461    1.410          0.950   0.078   8.126     85295
9     1.332    1.360          0.856   0.078   7.732     85316
10    1.261    1.342          0.906   0.078   9.078     85248
11    1.246    1.316          1.004   0.078   8.504     85248
12    1.207    1.264          1.067   0.078   9.224     85317
13    1.145    0.876          1.049   0.078   9.590     85340
14    1.083    0.606          1.029   0.078   8.418     85405
15    0.991    0.500          1.002   0.078   8.848     85378
16    0.949    0.496          0.956   0.078   8.446     85335
17    1.055    0.602          1.038   0.078  11.122     85334
18    1.326    0.978          1.205   0.078   9.724     85347
19    1.733    1.502          1.350   0.076  10.670     85542
20    1.899    1.668          1.380   0.076  10.348     85615
21    1.878    1.682          1.292   0.076   9.410     85529
22    1.413    1.208          1.097   0.078   9.272     85553
23    0.902    0.484          0.882   0.078   8.746     85560
```

---

## Perfil de Consumo por Dia da Semana

Estatisticas de consumo agrupadas por dia da semana (0=segunda, 6=domingo).

### Perfil por dia da semana

```text
            media  mediana  desvio_padrao  minimo  maximo  contagem
dia_semana                                                         
0           1.000    0.508          0.956   0.078   9.486    293868
1           1.070    0.606          1.019   0.076   9.732    294730
2           1.083    0.606          1.027   0.078   8.974    293659
3           0.982    0.492          0.959   0.076   9.410    293158
4           1.043    0.616          0.971   0.078   9.590    295013
5           1.248    0.854          1.191   0.078   9.724    288823
6           1.220    0.666          1.219   0.078  11.122    290029
```

---

## Perfil de Consumo por Mes

Variacao sazonal do consumo ao longo dos meses do ano.

### Perfil por mes

```text
     media  mediana  desvio_padrao  minimo  maximo  contagem
mes                                                         
1    1.462    1.372          1.223   0.198  10.162    175425
2    1.300    1.262          1.164   0.198  11.122    162649
3    1.231    0.940          1.103   0.196  10.670    176529
4    1.047    0.534          0.977   0.104   9.482    169074
5    1.030    0.590          0.939   0.106   8.944    178553
6    0.909    0.464          0.895   0.082   8.760    169449
7    0.700    0.354          0.732   0.098   7.240    178422
8    0.573    0.262          0.722   0.076   8.694    170419
9    0.976    0.516          0.953   0.098   8.110    167558
10   1.137    0.680          1.054   0.122  10.290    178513
11   1.292    1.156          1.139   0.194  10.348    166851
12   1.490    1.378          1.238   0.194   9.686    155838
```

---

## Perfil de Consumo por Periodo do Dia

Comparacao entre madrugada, manha, tarde e noite.

### Perfil por periodo

```text
             media  mediana  desvio_padrao  minimo  maximo  contagem
periodo_dia                                                         
madrugada    0.504    0.322          0.532   0.078  10.290    512375
manha        1.266    1.326          0.985   0.078   9.486    511650
noite        1.525    1.314          1.263   0.076  10.670    513146
tarde        1.072    0.620          1.028   0.078  11.122    512109
```

---

## Regimes de Consumo

Classificacao em baixo, moderado e alto com base nos quartis da potencia ativa.

### Regimes

```text
                quantidade  media_kw  mediana_kw  maximo_kw
regime_consumo                                             
alto                513426     2.538       2.220     11.122
baixo               513890     0.228       0.234      0.308
moderado           1021964     0.799       0.602      1.526
```

---

## Deteccao de Anomalias

Comparacao entre a deteccao estatistica por Z-score e a deteccao multivariada por Isolation Forest.

### Resumo de anomalias

```text
             metodo  quantidade  percentual  limiar
0            zscore       36160       1.742    3.00
1  isolation_forest       20753       1.000    0.01
```

---

## Clusterizacao de Perfis

Resumo dos grupos formados por K-Means a partir das variaveis eletricas padronizadas.

### Resumo de clusters

```text
         quantidade  media  mediana  desvio_padrao  minimo  maximo
cluster                                                           
0            695218  1.839    1.588          0.666   0.548   7.756
1           1250421  0.446    0.334          0.332   0.076   2.578
2             55874  3.991    3.824          1.075   1.498  10.162
3             47767  3.715    3.588          1.225   1.356  11.122
```

---

## Picos de Consumo

Distribuicao horaria dos eventos de pico de consumo. Limiar adotado: 3.264 kW (percentil 95).

### Picos por hora

```text
      quantidade_picos
hora                  
20               12568
21               11214
19               11025
18                6536
22                5830
7                 5149
12                5055
8                 5053
11                4747
13                4653
14                4546
9                 4286
15                3858
17                3846
10                3686
16                3121
6                 2527
23                2344
0                 1229
1                  643
2                  269
5                  112
4                   92
3                   89
```

---

## Participacao das Submedicoes

Participacao media aproximada de cada submetragem por periodo do dia.

### Participacao

```text
             participacao_sub_metering_1_pct  participacao_sub_metering_2_pct  participacao_sub_metering_3_pct
periodo_dia                                                                                                   
madrugada                              0.353                            5.484                           14.840
manha                                  1.798                            4.420                           40.204
noite                                  3.592                            5.019                           20.576
tarde                                  2.428                            7.326                           28.469
```

---

## Dias Extremos de Consumo

Dias com maior e menor consumo diario registrado.

### Dias extremos

```text
        tipo_dia        data   ano  mes  dia  energia_diaria_aprox_kwh  potencia_media_diaria_kw  potencia_maxima_diaria_kw submedicao_maior  valor_submedicao_maior_wh submedicao_menor  valor_submedicao_menor_wh
0  maior_consumo  2006-12-23  2006   12   23                    79.556                     3.315                      8.698   Sub_metering_3                    14726.0   Sub_metering_2                      425.0
1  menor_consumo  2007-04-29  2007    4   29                     0.000                       NaN                        NaN   Sub_metering_1                        0.0   Sub_metering_1                        0.0
```

---

## Ranking de Consumo Diario

Os 10 dias com maior e menor consumo energetico estimado.

### Maiores consumos

```text
            energia_diaria_aprox_kwh  potencia_media_diaria_kw  potencia_maxima_diaria_kw
datetime                                                                                 
2006-12-23                    79.556                     3.315                      8.698
2007-02-03                    67.162                     2.798                      7.904
2006-12-26                    65.568                     2.732                      6.496
2007-02-18                    63.829                     2.660                      7.160
2007-02-04                    59.932                     2.497                      7.698
2007-02-11                    59.520                     2.480                      7.426
2007-03-31                    58.492                     2.437                      7.098
2006-12-31                    58.237                     2.427                      6.722
2007-03-11                    58.011                     2.417                      7.142
2007-01-21                    56.788                     2.366                      8.018
```

### Menores consumos

```text
            energia_diaria_aprox_kwh  potencia_media_diaria_kw  potencia_maxima_diaria_kw
datetime                                                                                 
2010-09-27                     0.000                       NaN                        NaN
2010-09-26                     0.000                       NaN                        NaN
2010-08-19                     0.000                       NaN                        NaN
2010-08-18                     0.000                       NaN                        NaN
2010-08-21                     0.000                       NaN                        NaN
2010-08-20                     0.000                       NaN                        NaN
2009-06-14                     0.000                       NaN                        NaN
2007-04-29                     0.000                       NaN                        NaN
2010-01-13                     0.000                       NaN                        NaN
2009-06-13                     0.237                     0.474                       0.99
```

---

## Observacao Metodologica

Os resultados apresentados sao exploratorios. As submetragens e o consumo nao medido foram tratados como indicadores aproximados, e nao como decomposicao exata do consumo total da residencia. A analise nao substitui validacao estatistica mais profunda.

---
