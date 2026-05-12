"""Permite executar o projeto com `python -m projeto_energia`."""

from __future__ import annotations

from projeto_energia.pipeline import executar_pipeline_consolidado


def main() -> None:
    print("Iniciando pipeline de analise...")
    resultado = executar_pipeline_consolidado()
    print("Analise consolidada concluida com sucesso.")
    print(f"Relatorio gerado em: {resultado.caminho_relatorio}")
    print(f"Total de registros: {resultado.total_registros}")
    print(f"Limiar de pico: {resultado.limiar_pico_kw:.3f} kW")
    print(f"Anomalias Z-score: {resultado.quantidade_anomalias_zscore}")
    print(
        "Anomalias Isolation Forest: "
        f"{resultado.quantidade_anomalias_isolation_forest}"
    )
    print(f"Clusters formados: {resultado.quantidade_clusters}")
    print("Perfil por periodo do dia:")
    print(resultado.perfil_por_periodo.round(3).to_string())


if __name__ == "__main__":
    main()
