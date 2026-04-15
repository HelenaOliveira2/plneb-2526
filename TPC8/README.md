# TPC8 

Neste TPC foi implementado um sistema de pesquisa avançada com recurso a Expressões Regulares (módulo `re` do Python), permitindo uma filtragem precisa dos conceitos médicos.

## Funcionalidades Implementadas

* **Pesquisa Parcial:** Permite encontrar o termo pesquisado mesmo que este faça parte de outra palavra (ex: pesquisar por "teste" devolve também "testemunho").
* **Pesquisa de Palavra Exata:** Através de uma *checkbox*, é possível forçar o motor de busca a procurar estritamente pela palavra exata isolada (recorrendo ao regex `\b` para definir os limites da palavra).
* **Sensibilidade a Maiúsculas/Minúsculas (*Case Sensitive*):** Opção no formulário que permite ao utilizador decidir se a pesquisa deve, ou não, distinguir letras maiúsculas de minúsculas.
* **Destaque Visual Dinâmico:** O termo exato pesquisado é realçado a **negrito** nos resultados apresentados, tanto na designação como na descrição da doença.

## Ficheiros Desenvolvidos

* **`TPC8.py`:** Criação da rota `/pesquisar` (método GET). Capta os parâmetros do URL, processa a lógica de filtragem usando as funções `re.search` e injeta dinamicamente as tags HTML `<b>` através de `re.sub`.
* **`templates/pesquisar.html`:** Criação do interface de pesquisa com o formulário (input de texto e *checkboxes*) e a estrutura de apresentação dos resultados. A renderização do texto em negrito é garantida através da aplicação do filtro `| safe` do Jinja2.