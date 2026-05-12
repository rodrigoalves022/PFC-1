from pathlib import Path

import pandas as pd


COLUNAS_ESPERADAS = [
    "Date",
    "Time",
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3",
]


def carregar_dataset_uci(caminho_dataset: str | Path) -> pd.DataFrame:
    """Carrega o dataset UCI Household Electric Power Consumption."""
    caminho = Path(caminho_dataset)

    if not caminho.exists():
        raise FileNotFoundError(
            f"Dataset nao encontrado em: {caminho.resolve()}. "
            "Coloque o arquivo household_power_consumption.txt em data/."
        )

    df = pd.read_csv(caminho, sep=";", na_values="?", low_memory=False)

    colunas_ausentes = [coluna for coluna in COLUNAS_ESPERADAS if coluna not in df.columns]
    if colunas_ausentes:
        raise ValueError(
            "O dataset nao possui o schema esperado. "
            f"Colunas ausentes: {colunas_ausentes}"
        )

    return df
