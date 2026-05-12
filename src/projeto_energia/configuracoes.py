from pathlib import Path


RAIZ_PROJETO = Path(__file__).resolve().parents[2]
PASTA_DADOS = RAIZ_PROJETO / "data"
CAMINHO_DATASET_PADRAO = PASTA_DADOS / "household_power_consumption.txt"
