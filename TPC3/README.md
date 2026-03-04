# TPC3

Este trabalho teve como objetivo corrigir o código desenvolvido em contexto de aula para o processamento de um dicionário médico (dicionario_medico.txt). O processo envolveu a extração, limpeza e estruturação dos dados, com o intuito de contabilizar o número exato de conceitos e exportar a informação para os formatos JSON e HTML.

O processo iniciou-se com a leitura do ficheiro e a aplicação de expressões regulares (através do módulo `re`) para contornar inconsistências de formatação do texto original. Para estruturar corretamente a extração da informação, o texto foi submetido a um conjunto de transformações sequenciais:

- `texto = re.sub(r'\n\n', '\n\n@', texto)`
Nesta primeira fase, marcou-se cada potencial novo conceito. A instrução introduz um caráter `@` sempre que surgem duas quebras de linha consecutivas (`\n\n`), assinalando o que se pressupõe ser a fronteira entre diferentes blocos de texto.

- `texto = re.sub(r'\f', '\n', texto)`
Para lidar com as mudanças de página que interrompiam o fluxo natural da leitura, o caráter (`\f`)  foi substituído por uma nova linha simples (`\n`), unindo partes do texto que tinham ficado separadas na transição entre páginas do PDF original.

Durante a análise do documento, verificou-se que a formatação original gerava quebras indevidas, pelo que foram aplicadas expressões regulares para corrigir dois problemas específicos:

- `texto = re.sub(r'\n\n@\n([A-ZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÇ])', r'\n\1', texto)`
Correção de quebras entre a designação e a descrição: Quando a dupla quebra de linha com o marcador `@` era imediatamente seguida por uma letra maiúscula (acentuada ou não), o programa assumiu que ambas as partes pertenciam ao mesmo conceito (ou seja, não se tratava de um novo termo). Nesses casos, a quebra e o marcador foram substituídos apenas por uma nova linha (`\n\1`), unindo a designação à sua definição.

- `texto = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])', r'\1 \2', texto)`
União de linhas quebradas a meio da descrição: Quando o marcador separava duas letras minúsculas (indicando uma frase que foi interrompida a meio devido à formatação da página), esta expressão regular eliminou a quebra, juntando as duas partes com um espaço (`\1 \2`). Isto garantiu a continuidade sintática do texto da descrição.

- `texto = re.sub(r'@', '', texto)`
Após estas correções estruturais, procedeu-se a uma limpeza final, removendo todos os marcadores `@` residuais, visto que já tinham cumprido a sua função de análise.

- `conceitos = re.split(r"\n\n", texto)`
Por fim, com o texto devidamente tratado, o conteúdo completo foi segmentado numa lista designada conceitos. A divisão foi feita utilizando as duplas quebras de linha (`\n\n`) como delimitador, resultando em blocos de texto isolados para cada termo médico.