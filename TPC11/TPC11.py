import spacy
import math

collection = ["The sky is blue",
              "The sun is bright",
              "The sun in the sky"]

nlp=spacy.load("en_core_web_sm") 

def pre_processamento(collection):
    new_collection = []
    for doc in collection:
        s_doc = nlp(doc)
        tokens = []
        for token in s_doc:
            if not token.is_stop and not token.is_punct: #Verificar se nao é uma stop word e nao é pontuação
                tokens.append(token.text.lower())
        new_collection.append(tokens)
                
    """new_collection = [["sky", "blue"], 
                      ["sun", "bright"], 
                      ["sun", "sky"]]"""
    
    return new_collection

#tf(t,d)=count(t)/total_words(d)
def tf(doc):
    N=len(doc)
    res = {}
    for term in doc:
        if term in res:
            res[term] += 1
        else:
            res[term] = 1

    res = {k:v/N for k,v in res.items()}
    return res  # {"termo": freq}

#idf(t,D) = log(N/df)
def idf(collection):
    res = {}
    N = len(collection)
    unique_terms = set([term for d in collection for term in d])  # Criar set de todos os termos únicos na coleção global
    for term in unique_terms:
        counter = 0
        for d in collection:
            if term in d:
                counter += 1
        rarity = math.log(N/counter,10)
        res[term] = rarity

    return res # {"termo":rarity}

#tf_idf(t,d,D) = tf(t,d) * idf(t,D)
def tf_idf(collection):
    idf_values = idf(collection)
    vocabulario = sorted(list(idf_values.keys()))
    res=[] 
    for doc in collection:
        doc_tf_idf = []  #Vetor deste documento específico
        tf_values = tf(doc)
        for term in vocabulario:
            if term in tf_values:
                tf_idf = tf_values[term] * idf_values[term]
            else:
                tf_idf = 0
            doc_tf_idf.append(tf_idf)
        res.append(doc_tf_idf)

    return res

# Slide 16
# Sim(Q,D) = (Q * D) / (|Q| * |D|)
def calcular_cosseno(vetor_q, vetor_d):
    dot_product = 0
    soma_quadrados_q = 0
    soma_quadrados_d = 0
    
    # Percorrer cada posição do vetor
    for i in range(len(vetor_q)):
        
        # Produto Interno (Q * D): Multiplicar os valores na mesma posição
        dot_product += vetor_q[i] * vetor_d[i]
        
        # Magnitudes: Elevar cada valor ao quadrado e somar
        soma_quadrados_q += vetor_q[i] ** 2
        soma_quadrados_d += vetor_d[i] ** 2
        
    # Magnitudes (||Q|| e ||D||): Aplicar a raiz quadrada às somas
    mag_q = math.sqrt(soma_quadrados_q)
    mag_d = math.sqrt(soma_quadrados_d)
        
    similaridade = dot_product / (mag_q * mag_d)
    return similaridade

def processar_query(query, vocabulario, idf_corpus, matriz_tfidf):
    # Slide 14: Pré-processamento
    query_limpa = pre_processamento([query])[0] # Resultado: ['bright', 'sun']

    # Slide 15: Vetorização da query
    tf_query = tf(query_limpa)
    vetor_q = []
    for term in vocabulario:
        if term in tf_query:
            tf_idf = tf_query[term] * idf_corpus[term]
        else:
            tf_idf = 0
        vetor_q.append(tf_idf)
    
    print(f"Vetor da query: {vetor_q}")
    
    # Slides 16-19: Calcular cosseno e ranking
    ranking = []
    for i in range(len(matriz_tfidf)):
        vetor_d = matriz_tfidf[i]
        sim = calcular_cosseno(vetor_q, vetor_d)
        ranking.append((f"D{i+1}", sim))
        
    ranking.sort(key=lambda x: x[1], reverse=True)
        
    return ranking  # [(doc, ranking)]


colecao_limpa = pre_processamento(collection)
valores_idf = idf(colecao_limpa)
matriz_tfidf = tf_idf(colecao_limpa)
vocabulario = sorted(list(valores_idf.keys()))

print("--- Coleção ---")
print(colecao_limpa)
print("\n--- Matriz TF-IDF ---")
print(matriz_tfidf)

print("\n--- Resultado da query ---")
query = "The bright sun"
print(query)
resultados = processar_query(query, vocabulario, valores_idf, matriz_tfidf)
print(f"Ranking:{resultados}")

