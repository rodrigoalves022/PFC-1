# Documentacao do Projeto

Esta pasta concentra os documentos de apoio do PFC 1 e foi organizada para separar material academico, notas internas e descricao da arquitetura.

## Estrutura

- `planejamento_tecnico_pfc1.md`: documento principal de planejamento tecnico do PFC 1
- `base_relatorio_pfc1.md`: versao em formato de relatorio academico para reaproveitamento no texto do trabalho
- `arquitetura_do_repositorio.md`: visao curta da organizacao das pastas e do fluxo tecnico do projeto
- `analises/`: leituras comentadas dos resultados produzidos nos notebooks
- `guias/`: materiais didaticos e de apoio ao estudo dos conceitos
- `institucional/`: documentos formais relacionados ao PFC
- `notas/`: rascunhos, briefing inicial e ideias de analise
- `analises/resumo_analise_consolidada.md`: resumo reproduzivel gerado pelo script de analise consolidada

## Como usar esta pasta

- consulte `planejamento_tecnico_pfc1.md` para a visao operacional de problema, modulos e proximos passos;
- consulte `base_relatorio_pfc1.md` quando quiser uma versao mais proxima da redacao academica do PFC;
- consulte `arquitetura_do_repositorio.md` quando quiser entender rapidamente a funcao de cada pasta;
- consulte `notas/roteiro_de_analises_pfc1.md` para um recorte pratico do que vale seguir primeiro nas analises;
- consulte `analises/interpretacao_resultados_analise_consumo.md` para uma leitura comentada dos resultados do notebook principal;
- gere `analises/resumo_analise_consolidada.md` com `python scripts/executar_analise_consolidada.py` quando quiser atualizar os resultados numericos;
- alternativamente, execute pelo pacote com `$env:PYTHONPATH="src"` e `python -m projeto_energia`;
- consulte `guias/aula_termos_estatisticos_e_analiticos.md` para estudar os conceitos usados nas analises;
- mantenha em `notas/` apenas materiais de apoio e ideias em evolucao;
- mantenha em `institucional/` apenas documentos formais do processo academico.
