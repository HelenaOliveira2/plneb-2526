# TPC5
Este repositório contém o script em Python desenvolvido para extrair um dicionário completo de doenças do portal [Atlas da Saúde](https://www.atlasdasaude.pt/doencasaaz/).
O objetivo principal do TPC5 foi extrair informações sobre doenças, criando um dataset em formato JSON com **nome da doença**, **descrição curta** e **descrição completa**.

1. Gestão de URLs e Concatenagem

O script define uma `base_url` (`"https://www.atlasdasaude.pt"`) e uma `url` para o índice de doenças. Esta distinção é importante porque os links encontrados no HTML, através do atributo `href`, são relativos (por exemplo: `/doencas/gripe`). Ao concatenar a `base_url` com o `href`, o script gera o URL completo, permitindo aceder corretamente à página detalhada de cada doença.

2. Função `extrair_fulldesc`

Foi criada a função `extrair_fulldesc(link)` para obter a descrição completa de cada doença:
- Recebe o link da página individual da doença, faz um pedido HTTP usando `requests.get` para obter o HTML, e depois utiliza o BeautifulSoup para analisar a página;
- Localiza o conteúdo dentro do `<div>` com a classe `"field field-name-body field-type-text-with-summary field-label-hidden"`, que contém todo o texto detalhado da doença, incluindo sintomas, causas e tratamentos;
- Extrai este conteúdo e retorna apenas o texto limpo, sem tags HTML, permitindo modularizar o código e separar a extração da lista de doenças (A-Z) da extração detalhada de cada página individual.

3. Função `extrair_pagina`

Esta função extrai a informação para cada letra do alfabeto:
- Localiza todos os blocos de doenças na página (identificados pela classe `"views-row"`);
- Percorre o caminho de etiquetas `div.div.h3.a` para atravessar os "contentores" HTML do site até chegar ao título (`h3`) e ao link (`a`), extraindo daí o nome da doença (`designacao`) e o resumo inicial (`shortdesc`);
- Para cada doença encontrada, identifica o elemento `<a>` no título para obter o atributo `href`. Ao combinar este caminho com a `base_url`, a função consegue invocar a `extrair_fulldesc(link)` para obter os detalhes completos sem "perder" o contexto da listagem;
- Organiza a informação, onde cada doença é um objeto com as duas variantes de descrição.

4. Iteração Alfabética Automática

Para cobrir todo o portal, o script utiliza `string.ascii_lowercase` para percorrer as letras de 'a' a 'z'. Em cada iteração, concatena a letra à URL base (`url+letra`) permitindo assim construir dinamicamente os URLs das páginas de índice (ex: `.../doencasaaz/a`), automatizando a navegação por todo o catálogo alfabético do site.

5. Estrutura de Dados (JSON)

Os dados são organizados num dicionário onde cada chave é o nome da doença, mapeada para um objeto com dois campos:
- `shortdesc`: O resumo extraído da listagem principal;
- `fulldesc`: O conteúdo detalhado extraído da página individual.

--- 

### Resumo do funcionamento do Script

1. O script percorre todas as letras de A a Z, para aceder a cada página de índice de doenças.
2. Para cada letra, recolhe todas as doenças listadas na página (cada doença está dentro de um `<div>` com a classe `"views-row"`)
3. Para cada doença:
- Recolhe a descrição curta (`shortdesc`) presente na listagem principal.
- Acede à página individual da doença através do link (`<a href>`) encontrado no título.
- Recolhe a descrição completa (`fulldesc`) dentro do `<div>` com a classe `"field field-name-body field-type-text-with-summary field-label-hidden"`, que contém todos os detalhes da doença, incluindo sintomas, causas e tratamentos
4. Cada doença é armazenada como um objeto no dicionário Python, com os campos `shortdesc` e `fulldesc`.
5. Os dados são finalmente exportados para um ficheiro `doencas_tudo.json` utilizando `json.dump`, preservando os caracteres UTF-8 e organizando o JSON com indentação para facilitar a leitura.