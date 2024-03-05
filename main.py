from datetime import datetime
from participante import Participante
from leilao import Leilao
from lance import Lance
import random

lance = Lance
leilao = Leilao

leiloes = lance.carregar_leiloes('C:\\Users\\deborah\\Área de Trabalho\\Teste de Software\\leilao\\banco_dados\\leilao.csv')
participantes = lance.carregar_participantes('C:\\Users\\deborah\\Área de Trabalho\\Teste de Software\leilao\\banco_dados\\comprador.csv', 3)


leilao_escolhido = random.choice(leiloes)# Escolher aleatoriamente um leilão e participantes
leilao_escolhido.adicionar_participante(participantes[0])
leilao_escolhido.adicionar_participante(participantes[1])
leilao_escolhido.adicionar_participante(participantes[2])

leilao_escolhido.realizar_leilao()