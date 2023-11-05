from recinto import Recinto

class Zoologico:
    def __init__(self):
        self.recintos = []
        self.visitantes = 0

    def criar_recinto(self, estado_cuidado):
        recinto = Recinto(estado_cuidado)
        self.recintos.append(recinto)

    def adicionar_animal_ao_recinto(self, animal, recinto):
        recinto.adicionar_animal(animal)

    def alimentar_animal(self, animal):
        animal.alimentar()

    def calcular_receita(self):
        visitantes_total = sum(len(recinto.animais) for recinto in self.recintos)
        receita = visitantes_total * 10
        return receita
