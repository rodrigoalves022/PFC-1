from pathlib import Path
import sys

RAIZ_PROJETO = Path(__file__).resolve().parents[1]
PASTA_SRC = RAIZ_PROJETO / "src"

if str(PASTA_SRC) not in sys.path:
    sys.path.insert(0, str(PASTA_SRC))

from projeto_energia.analise.exploratoria import (
    calcular_matriz_correlacao,
    consolidar_consumo_diario,
    descrever_valores_ausentes,
    resumir_dataset,
)
from projeto_energia.dados.ingestao import carregar_dataset_uci
from projeto_energia.processamento.limpeza import limpar_dados_consumo_residencial


def main() -> None:
    caminho_dataset = RAIZ_PROJETO / "data" / "household_power_consumption.txt"

    dados_brutos = carregar_dataset_uci(caminho_dataset)
    dados_limpos = limpar_dados_consumo_residencial(dados_brutos)

    print("Resumo do dataset")
    print(resumir_dataset(dados_limpos).to_string(index=False))
    print()

    print("Valores ausentes")
    print(descrever_valores_ausentes(dados_limpos).to_string())
    print()

    print("Correlacao")
    print(calcular_matriz_correlacao(dados_limpos).round(3).to_string())
    print()

    consumo_diario = consolidar_consumo_diario(dados_limpos)
    print("Amostra da media diaria")
    print(consumo_diario.head().to_string())


if __name__ == "__main__":
    main()
