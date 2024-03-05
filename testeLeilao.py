import unittest
from participante import *
from leilao import Leilao

class TestLeilao(unittest.TestCase):

    def setUp(self):
        self.participante1 = Participante("João", "joao@example.com")
        self.participante2 = Participante("Maria", "maria@example.com")
        self.leilao = Leilao("Carro", 10000)

    def test_adicionar_participante(self):
        self.leilao.adicionar_participante(self.participante1)
        self.assertEqual(len(self.leilao.participantes), 1)
        self.assertEqual(self.leilao.participantes[0], self.participante1)

    def test_realizar_leilao(self):
        self.leilao.adicionar_participante(self.participante1)
        self.leilao.adicionar_participante(self.participante2)
        self.leilao.realizar_leilao()

    def test_mostrar_lances(self):
        self.leilao.adicionar_participante(self.participante1)
        self.leilao.adicionar_participante(self.participante2)

if __name__ == '__main__':
    unittest.main()
