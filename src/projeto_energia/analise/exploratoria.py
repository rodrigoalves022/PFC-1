import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ESTILO_GRAFICOS = "whitegrid"


def resumir_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna um resumo compacto do dataset."""
    return pd.DataFrame(
        [
            {
                "linhas": len(df),
                "colunas": df.shape[1],
                "inicio_periodo": df["datetime"].min(),
                "fim_periodo": df["datetime"].max(),
                "faltantes_datetime": int(df["datetime"].isna().sum()),
            }
        ]
    )


def descrever_valores_ausentes(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula a quantidade e o percentual de valores ausentes."""
    return (
        df.isna()
        .sum()
        .rename("quantidade_ausentes")
        .to_frame()
        .assign(percentual_ausentes=lambda tabela: 100 * tabela["quantidade_ausentes"] / len(df))
        .sort_values("quantidade_ausentes", ascending=False)
    )


def consolidar_consumo_diario(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega a serie temporal em medias diarias."""
    return (
        df.set_index("datetime")
        .resample("D")
        .mean(numeric_only=True)
    )


def calcular_matriz_correlacao(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula a matriz de correlacao das variaveis numericas."""
    return df.drop(columns="datetime").corr(numeric_only=True)


def plotar_valores_ausentes(tabela_ausentes: pd.DataFrame) -> None:
    """Plota o percentual de valores ausentes por coluna."""
    sns.set_theme(style=ESTILO_GRAFICOS)
    tabela_sem_zero = tabela_ausentes[tabela_ausentes["quantidade_ausentes"] > 0]

    if tabela_sem_zero.empty:
        return

    ax = tabela_sem_zero["percentual_ausentes"].plot(
        kind="bar",
        color="#C44E52",
        figsize=(10, 4),
    )
    ax.set_title("Percentual de valores ausentes por coluna")
    ax.set_ylabel("% de ausentes")
    ax.set_xlabel("Coluna")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()


def plotar_potencia_diaria(tabela_diaria: pd.DataFrame) -> None:
    """Plota a evolucao diaria das potencias ativa e reativa."""
    sns.set_theme(style=ESTILO_GRAFICOS)
    tabela_diaria[["Global_active_power", "Global_reactive_power"]].plot(figsize=(12, 5))
    plt.title("Media diaria de potencia ativa e reativa")
    plt.xlabel("Data")
    plt.ylabel("Potencia")
    plt.tight_layout()


def plotar_matriz_correlacao(matriz_correlacao: pd.DataFrame) -> None:
    """Plota um mapa de calor da correlacao entre variaveis numericas."""
    sns.set_theme(style=ESTILO_GRAFICOS)
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_correlacao, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Correlacao entre variaveis numericas")
    plt.tight_layout()
