class ExtratorAgumentosURL:
    def __init__(self, url):
        if self.string_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        return f"\nURL: {self.url} \nValor: {self.extrai_valor()} \nMoeda Origem: {moeda_origem} \nMoeda Destino: {moeda_destino} \n"

    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url

    @staticmethod
    def string_eh_valida(url):
        if (url and url.startswith("https://www.bytebank.com.br")):
            return True
        else:
            return False

    def extrai_argumentos(self):
        busca_moeda_origem = "moedaorigem=".lower()
        busca_moeda_destino = "moedadestino=".lower()

        inicio_substring_moeda_origem = self.encontra_inicio_substring(busca_moeda_origem)
        final_subtring_moeda_origem = self.url.find("&")
        moeda_origem = self.url[inicio_substring_moeda_origem:final_subtring_moeda_origem]

        if (moeda_origem == "moedadestino"):
            self.troca_moeda_origem()

            inicio_substring_moeda_origem = self.encontra_inicio_substring(busca_moeda_origem)
            final_subtring_moeda_origem = self.url.find("&")
            moeda_origem = self.url[inicio_substring_moeda_origem:final_subtring_moeda_origem]

        inicio_substring_moeda_destino = self.encontra_inicio_substring(busca_moeda_destino)
        final_subtring_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[inicio_substring_moeda_destino:final_subtring_moeda_destino]

        return moeda_origem, moeda_destino

    def encontra_inicio_substring(self, moeda_ou_valor):
        return self.url.find(moeda_ou_valor) + len(moeda_ou_valor)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extrai_valor(self):
        busca_valor = "valor=".lower()

        inicio_substring_valor = self.encontra_inicio_substring(busca_valor)
        return self.url[inicio_substring_valor:]