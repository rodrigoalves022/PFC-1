# Estrutura do Relatório Técnico e Artigo - PFC 1

## 1. Introdução

O consumo de energia elétrica em edificações é um tema relevante tanto do ponto de vista econômico quanto operacional, pois está diretamente relacionado à eficiência energética, qualidade de uso dos ambientes e apoio a tomadas de decisão. Em muitos cenários, os dados de consumo estão disponíveis em grande volume devido ao barateamento de tecnologias IoT (Internet of Things) e medidores inteligentes (smart meters). No entanto, a extração de valor e a interpretação desses dados ainda dependem de análise manual, conhecimento especializado e considerável tempo de avaliação. 

Nesse contexto, o uso de técnicas computacionais e algoritmos de aprendizado de máquina para organizar, analisar e interpretar essas informações torna-se uma alternativa promissora. Este projeto propõe a construção da base técnica de um sistema inteligente voltado à análise e interpretação de consumo de energia elétrica. Como estudo de caso inicial, utiliza-se o dataset *UCI Household Electric Power Consumption*, validando um pipeline completo de ingestão de dados, processamento, detecção de anomalias e clusterização de perfis de consumo.

## 2. Revisão Bibliográfica

Para fundamentar a abordagem proposta, foi realizado um levantamento bibliográfico focado em quatro eixos principais:

### 2.1 Análise de Consumo e o Dataset UCI
A utilização de dados reais é fundamental para validar arquiteturas de análise de consumo. O dataset adotado neste trabalho (Hebrail e Bérard, 2012) é amplamente reconhecido na literatura como um benchmark para estudos de séries temporais energéticas residenciais. Estudos complementares, como os de Makonin et al. (2016), reforçam a importância de bases instrumentadas para a compreensão do comportamento energético.

### 2.2 Eficiência Energética e Modelagem Data-Driven
A transição de métodos puramente físicos para abordagens baseadas em dados (data-driven) tem se mostrado eficaz. Autores como Pérez-Lombard et al. (2008) e Amasyali e El-Gohary (2018) revisaram exaustivamente a literatura e apontaram que algoritmos de aprendizado de máquina superam abordagens tradicionais na predição e classificação de padrões de consumo em edifícios.

### 2.3 Clusterização e Perfis de Carga
A identificação de perfis de consumidores é um passo crucial para a gestão energética. Trabalhos como os de Chicco et al. (2006) e Haben et al. (2016) demonstram a eficácia de algoritmos não supervisionados, especialmente o K-Means, para agrupar comportamentos de demanda utilizando dados de smart meters, permitindo ações direcionadas de eficiência.

### 2.4 Detecção de Anomalias
A identificação de vazamentos energéticos e falhas de equipamento depende de sistemas robustos de detecção de anomalias. Himeur et al. (2021) destacam que métodos como *Isolation Forest* e abordagens baseadas em *Z-score* são amplamente empregados devido à sua capacidade de lidar com a dimensionalidade e a não linearidade das séries temporais energéticas.

## 3. Metodologia

A arquitetura do sistema foi projetada de forma modular, permitindo o processamento eficiente de grandes volumes de dados e facilitando a futura integração de Large Language Models (LLMs). O pipeline desenvolvido é composto pelas seguintes etapas:

1. **Ingestão de Dados:** Módulo responsável por carregar o dataset bruto, validar o schema das colunas e otimizar os tipos de dados para processamento em memória.
2. **Processamento e Limpeza:** Tratamento de valores ausentes (NaN), coerção numérica e estruturação do índice temporal (datetime).
3. **Extração de Indicadores Temporais:** Criação de variáveis de contexto, como hora do dia, dia da semana, mês e classificação por períodos do dia (madrugada, manhã, tarde, noite).
4. **Aprendizado de Máquina Não Supervisionado (Análise Avançada):**
   - *Clusterização:* Implementação do algoritmo K-Means, com padronização via `StandardScaler`, para encontrar perfis típicos de consumo na residência.
   - *Detecção de Anomalias:* Implementação de dupla validação com um método estatístico (Z-score com limiar de 3 desvios padrões) e um método multivariado de aprendizado de máquina (*Isolation Forest*).
5. **Geração Automática de Relatórios:** Módulo que consolida as matrizes de correlação, tabelas de contingência e resultados dos modelos em relatórios técnicos no formato Markdown.

As tecnologias empregadas incluem a linguagem Python, bibliotecas de manipulação de dados (Pandas, Numpy) e algoritmos de Machine Learning (`scikit-learn`).

## 4. Resultados Preliminares

A execução do pipeline analítico consolidado gerou métricas cruciais sobre a edificação analisada. O modelo foi capaz de processar os mais de 2 milhões de registros da série temporal original, retornando os seguintes achados:

- **Clusterização de Perfis:** O algoritmo K-Means identificou **4 clusters distintos**, indicando que o comportamento da residência pode ser categorizado em diferentes réguas de intensidade e duração de uso dos equipamentos.
- **Detecção de Anomalias:** A identificação de pontos fora do padrão (outliers temporais de consumo excessivo ou falhas) registrou 36.160 instâncias suspeitas via método univariado (Z-Score) e 20.753 instâncias anômalas capturadas considerando o comportamento multivariado (Isolation Forest). O contraste entre as metodologias indica a importância de analisar o consumo sob a ótica de múltiplas variáveis.
- **Correlações e Sazonalidade:** Foi observada uma forte correlação entre picos de consumo e horários específicos do dia (predominantemente noite e início da manhã), bem como a influência clara das estações do ano (inverno europeu) na demanda de energia.

## 5. Considerações Finais e Próximos Passos (PFC 2)

O trabalho desenvolvido no PFC 1 estabeleceu uma arquitetura de dados robusta, reprodutível e orientada a metodologias avançadas de análise estatística e Machine Learning. O fluxo de dados opera com eficiência e a separação de responsabilidades (SOLID) foi respeitada, garantindo que o software possa evoluir para as próximas fases.

Para o **PFC 2**, a infraestrutura criada neste semestre servirá como camada de fundação (*Context Builder*) para o módulo de Interpretação com LLMs (Large Language Models). Os indicadores, agrupamentos e anomalias extraídos do K-Means e do Isolation Forest alimentarão um sistema RAG (Retrieval-Augmented Generation), permitindo que o sistema gere diagnósticos em linguagem natural e realize recomendações de eficiência energética de forma completamente autônoma.

---

## 6. Referências Bibliográficas

1. **AMASYALI, K.; EL-GOHARY, N. M.** A review of data-driven building energy consumption prediction studies. *Renewable and Sustainable Energy Reviews*, v. 81, p. 1192–1205, 2018.
2. **CHICCO, G.; NAPOLI, R.; PIGLIONE, F.** Comparisons among clustering techniques for electricity customer classification. *IEEE Transactions on Power Systems*, v. 21, n. 2, p. 933–940, 2006.
3. **HABEN, S.; SINGLETON, C.; GRINDROD, P.** Analysis and clustering of residential customers energy behavioral demand using smart meter data. *IEEE Transactions on Smart Grid*, v. 7, n. 1, p. 136–144, 2016.
4. **HÉBRAIL, G.; BÉRARD, A.** *Individual Household Electric Power Consumption Data Set*. UCI Machine Learning Repository, 2012. Disponível em: https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption.
5. **HIMEUR, Y. et al.** Artificial intelligence based anomaly detection of energy consumption in buildings: A review, current trends and new perspectives. *Applied Energy*, v. 287, 116601, 2021.
6. **MAKONIN, S. et al.** Electricity, water, and natural gas consumption of a residential house in Canada from 2012 to 2014. *Scientific Data*, v. 3, 160037, 2016.
7. **PÉREZ-LOMBARD, L.; ORTIZ, J.; POUT, C.** A review on buildings energy consumption information. *Energy and Buildings*, v. 40, n. 3, p. 394–398, 2008.
