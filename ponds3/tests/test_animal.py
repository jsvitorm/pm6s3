import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):
    def test_alimentar(self):
        animal = Animal("Leão", "Felino", felicidade=40)
        animal.alimentar()
        self.assertEqual(animal.obter_felicidade(), 50)

    def test_definir_felicidade(self):
        animal = Animal("Tigre", "Felino", felicidade=60)
        animal.definir_felicidade(70)
        self.assertEqual(animal.obter_felicidade(), 70)

if __name__ == '__main__':
    unittest.main()
