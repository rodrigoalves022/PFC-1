"""Clusterizacao de perfis de consumo energetico."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


COLUNA_ALVO_PADRAO = "Global_active_power"


@dataclass(frozen=True)
class ResultadoClusterizacao:
    """Resultado de uma rodada de clusterizacao."""

    n_clusters: int
    inertia: float
    tamanho_clusters: dict[int, int]
    nome_coluna_cluster: str


def clusterizar_perfis_consumo(
    df: pd.DataFrame,
    colunas_features: list[str] | None = None,
    n_clusters: int = 4,
    random_state: int = 42,
    nome_coluna_cluster: str = "cluster",
) -> tuple[pd.DataFrame, ResultadoClusterizacao, StandardScaler]:
    """Agrupa registros de consumo em perfis usando K-Means com padronizacao.

    Retorna o DataFrame com a coluna de cluster, o resultado estruturado
    e o scaler utilizado para referencia futura.
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

    scaler = StandardScaler()
    features_normalizadas = scaler.fit_transform(features)

    modelo = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10,
    )
    labels = modelo.fit_predict(features_normalizadas)

    dados[nome_coluna_cluster] = labels

    tamanho = {
        int(cluster): int(count)
        for cluster, count in zip(*np.unique(labels, return_counts=True))
    }

    resultado = ResultadoClusterizacao(
        n_clusters=n_clusters,
        inertia=float(modelo.inertia_),
        tamanho_clusters=tamanho,
        nome_coluna_cluster=nome_coluna_cluster,
    )

    return dados, resultado, scaler


def resumir_clusters(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    nome_coluna_cluster: str = "cluster",
) -> pd.DataFrame:
    """Gera estatisticas descritivas por cluster."""
    return df.groupby(nome_coluna_cluster)[coluna_alvo].agg(
        quantidade="count",
        media="mean",
        mediana="median",
        desvio_padrao="std",
        minimo="min",
        maximo="max",
    )


def calcular_perfil_horario_por_cluster(
    df: pd.DataFrame,
    coluna_alvo: str = COLUNA_ALVO_PADRAO,
    nome_coluna_cluster: str = "cluster",
) -> pd.DataFrame:
    """Calcula o consumo medio por hora para cada cluster."""
    if "hora" not in df.columns:
        raise ValueError("Coluna 'hora' nao encontrada. Execute adicionar_atributos_temporais primeiro.")

    return df.groupby([nome_coluna_cluster, "hora"])[coluna_alvo].mean().unstack(level=0)
