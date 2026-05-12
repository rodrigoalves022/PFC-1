import pandas as pd


def limpar_dados_consumo_residencial(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza o dataset para a analise exploratoria inicial."""
    dados_limpos = df.copy()

    dados_limpos["datetime"] = pd.to_datetime(
        dados_limpos["Date"] + " " + dados_limpos["Time"],
        format="%d/%m/%Y %H:%M:%S",
        errors="coerce",
    )
    dados_limpos = dados_limpos.drop(columns=["Date", "Time"])

    colunas_numericas = [coluna for coluna in dados_limpos.columns if coluna != "datetime"]
    dados_limpos[colunas_numericas] = dados_limpos[colunas_numericas].apply(
        pd.to_numeric,
        errors="coerce",
    )

    dados_limpos = dados_limpos.sort_values("datetime").reset_index(drop=True)

    return dados_limpos
