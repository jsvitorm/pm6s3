class Recinto:
    def __init__(self, estado_cuidado='bem'):
        self.animais = []
        self.estado_cuidado = estado_cuidado

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, animal):
        if animal in self.animais:
            self.animais.remove(animal)

    def alterar_estado_cuidado(self, estado):
        self.estado_cuidado = estado
