"""Deteccao de anomalias em series temporais de consumo energetico."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest


COLUNA_ALVO_PADRAO = "Global_active_power"


@dataclass(frozen=True)
class ResultadoAnomalias:
    """Resultado consolidado de uma rodada de deteccao de anomalias."""

    metodo: str
    quantidade_anomalias: int
    percentual_anomalias: float
    limiar: float | None
    coluna_flag: str


def detectar_anomalias_zscore(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    limiar_zscore: float = 3.0,
    nome_coluna_flag: str = "anomalia_zscore",
    nome_coluna_score: str = "zscore",
) -> tuple[pd.DataFrame, ResultadoAnomalias]:
    """Detecta anomalias por Z-score em uma coluna numerica.

    Valores cujo Z-score absoluto excede o limiar sao marcados como anomalia.
    """
    dados = df.copy()
    media = dados[coluna_alvo].mean()
    desvio = dados[coluna_alvo].std()

    if desvio == 0:
        dados[nome_coluna_score] = 0.0
        dados[nome_coluna_flag] = False
    else:
        dados[nome_coluna_score] = (dados[coluna_alvo] - media) / desvio
        dados[nome_coluna_flag] = dados[nome_coluna_score].abs() > limiar_zscore

    quantidade = int(dados[nome_coluna_flag].sum())
    total = len(dados)

    resultado = ResultadoAnomalias(
        metodo="zscore",
        quantidade_anomalias=quantidade,
        percentual_anomalias=round(100 * quantidade / total, 4) if total > 0 else 0.0,
        limiar=limiar_zscore,
        coluna_flag=nome_coluna_flag,
    )

    return dados, resultado


def detectar_anomalias_isolation_forest(
    df: pd.DataFrame,
    colunas_features: list[str] | None = None,
    contamination: float = 0.01,
    random_state: int = 42,
    nome_coluna_flag: str = "anomalia_iforest",
    nome_coluna_score: str = "score_iforest",
) -> tuple[pd.DataFrame, ResultadoAnomalias]:
    """Detecta anomalias multivariadas com Isolation Forest.

    O modelo opera sobre as colunas indicadas, preenchendo NaN com a mediana
    antes de treinar. Os scores de anomalia sao adicionados ao DataFrame.
    """
    dados = df.copy()

    if colunas_features is None:
        colunas_features = [
            "Global_active_power",
            "Global_reactive_power",
            "Voltage",
            "Global_intensity",
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3",
        ]

    colunas_existentes = [c for c in colunas_features if c in dados.columns]
    if not colunas_existentes:
        raise ValueError("Nenhuma coluna de features encontrada no DataFrame.")

    features = dados[colunas_existentes].copy()
    features = features.fillna(features.median())

    modelo = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_jobs=-1,
    )
    predicoes = modelo.fit_predict(features)
    scores = modelo.decision_function(features)

    dados[nome_coluna_flag] = predicoes == -1
    dados[nome_coluna_score] = scores

    quantidade = int(dados[nome_coluna_flag].sum())
    total = len(dados)

    resultado = ResultadoAnomalias(
        metodo="isolation_forest",
        quantidade_anomalias=quantidade,
        percentual_anomalias=round(100 * quantidade / total, 4) if total > 0 else 0.0,
        limiar=contamination,
        coluna_flag=nome_coluna_flag,
    )

    return dados, resultado


def resumir_anomalias(
    resultados: list[ResultadoAnomalias],
) -> pd.DataFrame:
    """Gera uma tabela comparativa dos metodos de deteccao de anomalias."""
    return pd.DataFrame(
        [
            {
                "metodo": r.metodo,
                "quantidade": r.quantidade_anomalias,
                "percentual": r.percentual_anomalias,
                "limiar": r.limiar,
            }
            for r in resultados
        ]
    )
