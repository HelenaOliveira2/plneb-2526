import re
import json

f = open("dicionario_medico.xml", encoding="utf-8")
texto = f.read()


texto=re.sub(r"</?text.*?>", "", texto) #substituir tudo o que está entre text por vazio 
#marcar conceitos

texto=re.sub(r"</?page.*?>", "", texto) 

conceitos=re.findall(r'<b>(.*)</b>\n([^<]+)',texto) 

res = {}
for termo, desc in conceitos:
    res[termo] = desc.strip()

f_out = open("conceitos.json", "w", encoding="utf-8")
json.dump(res, f_out, indent=4, ensure_ascii=False)
f_out.close()


print(conceitos)

#print(texto)

#\s apanha espaços, tabs e \n