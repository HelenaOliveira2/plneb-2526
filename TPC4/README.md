# TPC4 - Sunny Haven Villa - Website

Este é o código fonte do website para o **Sunny Haven Villa**, um alojamento em Ponte de Lima, Portugal. O site apresenta informações sobre a propriedade, comodidades, regras da casa, galeria de fotos, avaliações de hóspedes, localização no mapa e contacto.  


## 1. Arquitetura de Conteúdo 

### 1.1. Identidade e Navegação (`<header>`)
O cabeçalho utiliza a propriedade `sticky` para permanecer acessível. A marca e o menu estão encapsulados numa `brand-container`.
 O menu utiliza links internos (`#galeria`, `#comodidades`). Este método melhora a User Experience ao permitir que o utilizador salte para o conteúdo desejado sem recarregar a página.

### 1.2. Galeria de Imagens (`#galeria`)
 A galeria foi implementada com a classe `.photo-gallery`, utilizando o sistema de **CSS Grid**. 
 Cada imagem está dentro de uma `div` `.photo-item`. O uso do atributo `alt` em cada imagem garante a acessibilidade para leitores de ecrã. 

### 1.3. Comodidades e Serviços (`#comodidades`)
Esta secção utiliza a classe `.all-amenities-grid`. O conteúdo é dividido por categorias (`.amenity-category`), cada uma com o seu título `<h4>` e uma lista `<ul>`. Consiste na organização de serviços por categorias (Exterior, Cozinha, Quartos, Essenciais) para facilitar o scanning visual.
Esta organização permite uma leitura rápida. 

### 1.4. Regras da Casa (`#regras`)
Cartões informativos sobre horários de check-in, políticas de ruído e animais.

### 1.5. Sistema de Avaliações (`#avaliacoes`)
Cada `.review-card` contém:
    1. **Metadados:** Tipo de quarto e pontuação.
    2. **Conteúdo:** Título e corpo do texto da avaliação.
    3. **Autoridade:** A `reviewer-info` apresenta o avatar (com iniciais), o nome e o país, conferindo autenticidade.
No final, existe a `booking-cta-box` que apresenta a média global de 9.7, funcionando como o argumento final de venda antes dos botões de reserva.

### 1.6. Mapa (`#mapa`)
Secção final com geolocalização e canais diretos de comunicação e redes sociais.

---

## 2. Lógica de Interatividade (JavaScript)
O comportamento dinâmico do site foi implementado com JavaScript para gerir o sistema de slider de forma leve e eficiente. O script controla a navegação entre imagens através da manipulação de classes, removendo a classe active de todas as fotos e aplicando-a apenas à imagem selecionada pelo slideIndex para garantir um ciclo de visualização infinito.

### 2.1. Variáveis e Seleção de Elementos
O script começa por capturar o estado inicial:
- slideIndex: Variável que guarda a posição da foto atual.
- querySelectorAll: Captura todas as imagens para dentro de uma lista (array)

### 2.2. Função `mostrarSlide(n)`
- Limpeza: O forEach remove a classe active de todas as fotos para evitar sobreposições.
- Loop: Os if garantem que, ao chegar à última foto, o carrossel volte à primeira (e vice-versa).
- Ativação: Adiciona a classe active apenas à foto selecionada, que o CSS se encarrega de mostrar com opacidade.

### 2.3. Função  `mudarSlide(n)`
Funciona como um intermediário. Recebe o valor do clique (1 ou -1), atualiza o índice e pede à função principal para atualizar o ecrã.
