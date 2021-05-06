from ExtratorArgumentosURL import ExtratorAgumentosURL

url1 = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=700"
url2 = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=7000"

argumentos_url = ExtratorAgumentosURL(url1)

print(f"\nClasse do objeto: {type(argumentos_url)}")
print(f"\nAs URLs são iguais? {url1 == url2}")
print(argumentos_url)

moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor = argumentos_url.extrai_valor()

print(moeda_origem, moeda_destino, valor)
