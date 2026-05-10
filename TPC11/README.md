# TPC 11 

Neste TPC foi implementado um sistema base de Recuperação de Informação (IR) focado no Modelo de Espaço Vetorial, recorrendo ao algoritmo TF-IDF e Similaridade do Cosseno para classificar e ordenar documentos com base numa *query* de pesquisa.

## Funções Base 

Para preparar a coleção de documentos e construir a matriz de pesos, foram implementadas as seguintes funções:

* **`pre_processamento(collection)`:** Utiliza a biblioteca `spaCy` (modelo `en_core_web_sm`) para processar os textos originais. Executa a extração de *tokens*, converte o texto para minúsculas (*lowercasing*) e remove *stop words* e sinais de pontuação através dos atributos `.is_stop` e `.is_punct`.
* **`tf(doc)`:** Calcula a Frequência Relativa (Term Frequency) de cada palavra num documento. Retorna um dicionário onde a contagem absoluta de cada termo é dividida pelo número total de palavras do documento.
* **`idf(collection)`:** Calcula o *Inverse Document Frequency*. Extrai um *set* de termos únicos globais e aplica a fórmula logarítmica `math.log(N/DF)`. Esta função penaliza palavras comuns (peso próximo de 0) e recompensa termos raros e distintivos.
* **`tf_idf(collection)`:** Orquestra as métricas anteriores. Gera um vocabulário global ordenado alfabeticamente e constrói a Matriz TF-IDF (lista de listas), onde cada vetor de documento contém o produto final $TF \times IDF$ para cada termo do espaço dimensional.

---

## Funções Desenvolvidas para a Query e Cosseno

Para implementar o processamento da *query* e o cálculo algébrico do *ranking*, foram criadas as seguintes funções:

* **`calcular_cosseno(vetor_q, vetor_d)`:** Calcula a Similaridade do Cosseno entre dois vetores. Itera pelas posições dos vetores para extrair o Produto Interno (*Dot Product*) e divide-o pelo produto das magnitudes de cada vetor (`math.sqrt()`).
* **`processar_query(query, vocabulario, idf_corpus, matriz_tfidf)`:** Função agregadora do motor de busca. A sua execução divide-se nos seguintes passos:
  1. Aplica o `pre_processamento` à *query*, neste caso "The bright sun".
  2. Calcula o `tf` da *query* e projeta-o no espaço dimensional do vocabulário, cruzando esses valores com o `idf_corpus` previamente calculado para gerar o vetor da *query*.
  3. Compara o vetor gerado com todos os vetores da `matriz_tfidf` chamando a função `calcular_cosseno`.
  4. Ordena os resultados com `.sort(key=lambda x: x[1], reverse=True)` e devolve o *Ranking* Final em formato de lista de tuplos.