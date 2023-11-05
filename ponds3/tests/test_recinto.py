import unittest
from recinto import Recinto
from animal import Animal

class TestRecinto(unittest.TestCase):
    def test_adicionar_animal(self):
        recinto = Recinto(estado_cuidado="Felino")
        leao = Animal("Leão", "Felino")
        recinto.adicionar_animal(leao)
        self.assertIn(leao, recinto.animais)

    def test_remover_animal(self):
        recinto = Recinto(estado_cuidado="Felino")
        leao = Animal("Leão", "Felino")
        recinto.adicionar_animal(leao)
        recinto.remover_animal(leao)
        self.assertNotIn(leao, recinto.animais)  

    def test_alterar_estado_cuidado(self):
        recinto = Recinto(estado_cuidado="bem")
        recinto.alterar_estado_cuidado("mal")
        self.assertEqual(recinto.estado_cuidado, "mal")

if __name__ == '__main__':
    unittest.main()

