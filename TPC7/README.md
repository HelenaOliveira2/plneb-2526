# TPC7

Este repositório contém uma aplicação web desenvolvida em Python (utilizando a framework Flask) que serve como um Dicionário Médico interativo. A aplicação permite a pesquisa rápida de termos clínicos e a navegação num índice alfabético completo (A-Z). O design é totalmente responsivo, construído com [Bootstrap 5](https://getbootstrap.com/).

## Estrutura do Projeto

### `web.py`
É o motor principal da aplicação (Backend). Este script em Flask é responsável por:
* Carregar os dados do ficheiro `dicionario_medico.json`.
* Gerir as rotas do site (Página Inicial, Pesquisa, Lista de Conceitos e Página Individual de cada conceito).
* Implementar a lógica de pesquisa *case-insensitive* (ignora maiúsculas e minúsculas).

### `layout.html`
O template base da aplicação (Frontend). Utiliza o motor Jinja2 para servir de "esqueleto" a todas as outras páginas. Contém:
* A importação dos ficheiros nativos e [ícones](https://icons.getbootstrap.com/) do Bootstrap 5.3.3.
* A barra de navegação superior ([`navbar`](https://getbootstrap.com/docs/5.3/components/navbar/)) estática.
* O rodapé (`footer`) global do site, configurado para ficar sempre fixo no fundo do ecrã.

### `home.html`
A página principal contém:
* Uma secção de destaque ([*Hero*](https://getbootstrap.com/docs/5.3/examples/heroes/)) com uma barra de pesquisa proeminente.
* Uma grelha com 6 "Termos em Destaque", gerados de forma aleatória a cada visita pelo Python.
* Uma secção inferior com os pilares de confiança do portal de saúde.

### `conceitos.html`
O índice completo do Dicionário Médico:
* Apresenta uma barra de navegação alfabética "colada" no topo ([*sticky-top*](https://getbootstrap.com/docs/5.3/helpers/position/#sticky-top)) para saltar rapidamente entre letras.
* Agrupa todos os conceitos presentes no JSON pela sua letra inicial.
* Possui um botão flutuante no canto inferior direito para regressar suavemente ao topo da página.

### `conceito.html`
A página dedicada à definição de um termo médico individual:
* Apresenta o nome do conceito acompanhado de uma etiqueta visual ([Badge](https://getbootstrap.com/docs/5.3/components/badge/)) "Termo Clínico".
* Exibe a descrição do termo dentro de uma caixa com fundo suave.
* Inclui navegação rápida por [*breadcrumbs*](https://getbootstrap.com/docs/5.3/components/breadcrumb/) no topo e botões de retorno no fundo.

### `error.html`
Uma página de erro "404" funcional. Em vez de simplesmente mostrar uma falha técnica ao utilizador:
* É ativada sempre que a pesquisa por um termo não tem correspondência no dicionário.
* Apresenta uma mensagem clara e um ícone de aviso.
* Fornece uma nova barra de pesquisa integrada para que o utilizador tente imediatamente outra palavra.