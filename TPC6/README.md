# TPC6

Este repositório contém um script em Python que extrai personagens de Harry Potter e a Pedra Filosofal e analisa as suas relações com base na coocorrência em frases, usando spaCy. Os resultados são guardados em JSON, ordenados pela frequência de interações.

## 1. Leitura e Pré-processamento de Texto

O script lê o ficheiro `.txt` do livro e substitui as quebras de linha (`\n`) e as quebras de página (`\f`) por espaços, evitando que o spaCy quebre frases indevidamente e garantindo uma análise contínua do documento (`doc`).

## 2. Reconhecimento de Entidades Nomeadas (NER)

Utilizando o modelo `pt_core_news_lg`, o script divide o texto em frases (`doc.sents`). Em cada frase, procura por entidades classificadas explicitamente como Pessoa (`entity.label_ == "PER"`). O nome detetado é limpo de espaços extra (`strip()`) e validado, garantindo que letras soltas (tamanho `<= 1`) identificadas por engano pelo modelo são ignoradas.

Durante a execução, verifiquei que o modelo de NER por vezes identifica incorretamente palavras que não são nomes de personagens (como substantivos comuns, palavras isoladas ou até verbos) como sendo entidades do tipo Pessoa.

Exemplos observados no output incluem entradas como: `"Ilustrações"`,`"Baixelivros.org"`,`"Deitado"`,...

Estas ocorrências resultam de limitações do modelo `pt_core_news_lg` podendo introduzir ruído nos resultados.

## 3. Extração de Relações (Co-ocorrência)

As personagens de cada frase são guardadas numa lista (`personagens_frase`), evitando duplicados. Se houver mais de uma, o script usa dois ciclos `for` para criar pares e registar ou incrementar a coocorrência entre elas num dicionário.

## 4. Estrutura de Dados, Ordenação e Apresentação

Os dados são guardados num dicionário de dicionários (`amigos`). No final, as relações de cada personagem são ordenadas por frequência (`reverse=True`) e armazenadas em `amigos_ordenados`. Os resultados são exportados para o ficheiro `HarryFriends.json` com `json.dump`.

---

### Resumo do funcionamento do Script

1. O script carrega o texto completo do livro e remove quebras de linha (`\n`) e quebras de página (`\f`) para manter a integridade estrutural das frases.

2. O texto é processado pelo modelo `pt_core_news_lg` do spaCy, que o divide em frases e identifica automaticamente as Entidades Nomeadas.

3. Para cada frase:
- Procura entidades do tipo Pessoa (`PER`).
- Armazena os nomes válidos (com mais de um caractere) numa lista temporária, garantindo que não existem entradas duplicadas na mesma frase.
- Gera combinações cruzadas entre todos os nomes únicos encontrados nessa frase.
- Regista e atualiza a co-ocorrência no dicionário global `amigos`.

4. Terminado o processamento, as interações de cada personagem são ordenadas da mais frequente para a menos frequente.

5. A estrutura final (`amigos_ordenados`) é exportada para o ficheiro `HarryFriends.json`, num formato estruturado e legível.