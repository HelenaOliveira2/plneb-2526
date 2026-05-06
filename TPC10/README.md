# TPC10

Este repositório contém o desenvolvimento e treino de um modelo de Reconhecimento de Entidades Nomeadas (NER) para a língua portuguesa. O objetivo principal foi utilizar modelos de linguagem pré-treinados e adaptá-los para identificar categorias específicas como Pessoas, Organizações, Locais e Profissões em textos.

## Contexto e Pré-processamento

A fase inicial do projeto focou-se na preparação e exploração dos dados:
- Foi utilizado o dataset `lfcc/portuguese_ner` disponível no Hugging Face, que contém tokens e etiquetas NER específicas para o português.
- Utilizou-se o modelo e o respetivo *tokenizer* `neuralmind/bert-base-portuguese-cased`, um modelo BERT treinado especificamente para o português.
- **Pré-processamento:** Como o *tokenizer* do BERT divide palavras em pedaços mais pequenos (sub-palavras), foi necessário reajustar os dados. Para isso, implementaram-se duas funções principais:
  - `align_labels_with_tokens()`: Função responsável por alinhar as etiquetas (labels) originais com os novos sub-tokens criados. Atribui o valor `-100` a tokens especiais (como `[CLS]` e `[SEP]`) e a pedaços de palavras secundários, garantindo que o modelo os ignora durante a aprendizagem e avalia apenas a primeira parte da palavra.
  - `tokenize_dataset()`: Função que percorre todo o dataset, aplica o *tokenizer* (com um limite máximo de 512 tokens para evitar erros de memória) e junta as novas etiquetas alinhadas a cada frase.
No final deste processo, as listas processadas foram convertidas novamente para o formato `Dataset` da Hugging Face para estarem prontas para a fase de treino.

## Desenvolvimento

A implementação da lógica de treino e a configuração das métricas basearam-se no [guia oficial de Token Classification da Hugging Face](https://huggingface.co/docs/transformers/tasks/token_classification#token-classification), que serviu como referência técnica para o uso da biblioteca `transformers`.

### 1. Preparação Inicial 
- **`label_list`:** Extração das 11 categorias (ex: `B-Pessoa`, `I-Organizacao`) diretamente das *features* do dataset para uso posterior.
- **`DataCollator`:** Utilização do `DataCollatorForTokenClassification`. Agrupa as frases em lotes (*batches*) e aplica o *padding* (preenchimento) dinâmico aos tokens e às respetivas *labels* de forma correta.

### 2. Evaluate (Métricas de Avaliação)
Configurou-se a forma como o modelo seria avaliado durante a sua aprendizagem:
- Carregou-se a métrica `seqeval` através da biblioteca `evaluate`.
- **Função `compute_metrics`:** Desenvolveu-se esta função para comparar as previsões do modelo com as etiquetas reais. A função utiliza a `label_list` para converter as previsões em texto, ignorando propositadamente os tokens de preenchimento (marcados com `-100`), calculando assim valores exatos de Precisão, Recall, F1-Score e Accuracy.

### 3. Train 
Na fase final, foram instanciados o modelo e o motor de treino:
- **Mapeamento de Etiquetas:** Criação manual dos dicionários `id2label` e `label2id` para que o modelo saiba a que texto corresponde cada ID numérico.
- **Carregamento do Modelo:** Instanciação do `AutoModelForTokenClassification` passando os dicionários referidos e o número total de *labels* (11).
- **Parâmetros e Trainer:** Utilizaram-se os `TrainingArguments` com uma taxa de aprendizagem (*learning rate*) de `2e-5`, *weight decay* de `0.01`, ao longo de **3 épocas**. A avaliação foi configurada para ocorrer ao final de cada época (`eval_strategy="epoch"`).
- **Resultados:** A execução do `trainer.train()` decorreu sem problemas e demonstrou uma excelente performance, culminando num **F1-Score de 96.1%** e numa **Precisão global de 98.6%** no conjunto de testes.

## Teste Prático e Resultados

Para validar o modelo treinado, foi utilizada uma `pipeline` de classificação de tokens com a estratégia de agregação `first` (que agrupa automaticamente sub-palavras em entidades completas).

O modelo foi aplicado a um excerto de uma notícia real: [Notícia da CNN Portugal - Greve na Saúde](https://cnnportugal.iol.pt/greve/paralisacao/paralisacao-nacional-na-saude-greve-convocada-para-4-e-5-de-maio-abrange-todos-os-trabalhadores-do-setor/20260429/69f21863d34e28842c837a3e)

### Resultados da Inferência:
O modelo demonstrou uma elevada precisão na extração de informação, identificando com sucesso as seguintes entidades e as suas respetivas categorias:
- **Pessoas:** "José Carlos Martins" (Confiança: 98.5%)
- **Organizações:** "Ministério da Saúde" (Confiança: 79.4%), "SEP" (Confiança: 42.9% a 68.5%)
- **Locais:** "Lisboa" (Confiança: 99.0%), "Campo Pequeno" (Confiança: 87.7%)
- **Datas:** "12 de maio" (Confiança: 97.5%)