from datetime import datetime
import csv
import random
from leilao import Leilao 
from participante import Participante

class Lance:
    def carregar_leiloes(filename):
        leiloes = []

        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                objeto = row['objeto']
                valor_min_str = row['valor_min']
                if valor_min_str:  # Verifica se o valor não está vazio
                    valor_min = float(valor_min_str)
                    leilao = Leilao(objeto, valor_min)
                    leiloes.append(leilao)
                else:
                    print(f"AVISO: Linha ignorada - Objeto '{objeto}' não possui um valor mínimo definido.")
        return leiloes


    def carregar_participantes(filename, num_participantes):
        participantes = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                participante = Participante(row['nome'], row['email'])
                participantes.append(participante)
        return random.sample(participantes, num_participantes)
    
    @property
    def objeto(self):
        return self.__objeto

    @objeto.setter
    def objeto(self, novo_objeto):
        self.__objeto = novo_objeto

    @property
    def valor_minimo(self):
        return self.__valor_minimo

    @valor_minimo.setter
    def valor_minimo(self, novo_valor_minimo):
        self.__valor_minimo = novo_valor_minimo

    @property
    def participantes(self):
        return self.__participantes

    def adicionar_participante(self, participante):
        self.__participantes.append(participante)

    @property
    def lances(self):
        return self.__lances
