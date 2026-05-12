"""Analise exploratoria e extracao de indicadores iniciais."""

from .anomalias import (
    ResultadoAnomalias,
    detectar_anomalias_isolation_forest,
    detectar_anomalias_zscore,
    resumir_anomalias,
)
from .clusterizacao import (
    ResultadoClusterizacao,
    calcular_perfil_horario_por_cluster,
    clusterizar_perfis_consumo,
    resumir_clusters,
)
from .exploratoria import (
    calcular_matriz_correlacao,
    descrever_valores_ausentes,
    resumir_dataset,
)
from .indicadores import (
    ResultadoPicos,
    adicionar_atributos_temporais,
    adicionar_indicadores_energeticos,
    agregar_estatisticas_por_grupo,
    calcular_consumo_diario,
    calcular_participacao_submedicoes,
    classificar_periodo_dia,
    classificar_regimes_consumo,
    identificar_picos_consumo,
    montar_perfis_temporais,
    montar_tabelas_insumo_interpretacao,
    resumir_dias_extremos,
    resumir_regimes_consumo,
)

__all__ = [
    # Exploratoria
    "calcular_matriz_correlacao",
    "descrever_valores_ausentes",
    "resumir_dataset",
    
    # Indicadores
    "ResultadoPicos",
    "adicionar_atributos_temporais",
    "adicionar_indicadores_energeticos",
    "agregar_estatisticas_por_grupo",
    "calcular_consumo_diario",
    "calcular_participacao_submedicoes",
    "classificar_periodo_dia",
    "classificar_regimes_consumo",
    "identificar_picos_consumo",
    "montar_perfis_temporais",
    "montar_tabelas_insumo_interpretacao",
    "resumir_dias_extremos",
    "resumir_regimes_consumo",
    
    # Anomalias
    "ResultadoAnomalias",
    "detectar_anomalias_isolation_forest",
    "detectar_anomalias_zscore",
    "resumir_anomalias",
    
    # Clusterizacao
    "ResultadoClusterizacao",
    "calcular_perfil_horario_por_cluster",
    "clusterizar_perfis_consumo",
    "resumir_clusters",
]
