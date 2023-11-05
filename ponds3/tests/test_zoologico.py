import unittest
from zoologico import Zoologico
from recinto import Recinto
from animal import Animal

class TestZoologico(unittest.TestCase):
    def test_adicionar_animal_ao_recinto(self):
        zoo = Zoologico()
        recinto = Recinto(estado_cuidado="bem")
        leao = Animal("Leão", "Felino")
        zoo.adicionar_animal_ao_recinto(leao, recinto)
        self.assertIn(leao, recinto.animais)

    def test_calcular_receita(self):
        zoo = Zoologico()
        recinto = Recinto(estado_cuidado="bem")
        leao = Animal("Leão", "Felino")
        tigre = Animal("Tigre", "Felino")
        recinto.adicionar_animal(leao)
        recinto.adicionar_animal(tigre)
        zoo.criar_recinto("bem")
        zoo.adicionar_animal_ao_recinto(leao, zoo.recintos[0])
        zoo.adicionar_animal_ao_recinto(tigre, zoo.recintos[0])
        receita = zoo.calcular_receita()
        self.assertEqual(receita, 20) 

if __name__ == '__main__':
    unittest.main()
