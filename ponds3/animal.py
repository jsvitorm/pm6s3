class Animal:
    def __init__(self, nome, especie, felicidade=50):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade

    def alimentar(self):
        self.felicidade += 10

    def obter_felicidade(self):
        return self.felicidade

    def definir_felicidade(self, felicidade):
        self.felicidade = felicidade
