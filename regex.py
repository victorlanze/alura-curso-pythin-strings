import re

padrao = "[0-9]{4,5}-?[0-9]{4}"
texto = "Meu número para contato é 9633-5723"


retorno = re.findall(padrao, texto)
retorno2 = re.search(padrao, texto)

print(retorno)
print(retorno2.group())