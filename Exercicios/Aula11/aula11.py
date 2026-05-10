
import spacy
import math


collection = ["The sky is blue",
              "The sun is bright",
              "The sun in the sky"]


nlp=spacy.load("en_core_web_sm") 


def pre_processamento():
    new_collection = []
    for doc in collection:
        s_doc = nlp(doc)
        ... #TPC - spacy for token in doc e depois ver se é uma stop word. se for nao meto se nao for meto

    new_collection = [["sky", "blue"], 
                      ["sun", "bright"], 
                      ["sun", "sky"]]
    
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
    unique_terms = set([term for d in collection for term in d])  #criar uma lista para cada documento na colecao e para cada termo em cada documento e tira os repetidos
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
    res=[] 
    for doc in collection:
        doc_tf_idf = []  
        tf_values = tf(doc)
        for term in tf_values:
            tf_idf = tf_values[term] * idf_values[term]
            doc_tf_idf.append(tf_idf)
        res.append(doc_tf_idf)

    return res # TPC apareca os 0 tambem das palavras que o docuemtno nao tem

# TPC - query do ppt "The bright sun", calcular tf da query e multiplicar pelo idf do corpus, fazer o vetor dela e calcular os cossenos. descobrir o documento mais relevante
# seguir os slides e chegar ao ranking