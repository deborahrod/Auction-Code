from datetime import datetime

class Leilao:
    def __init__(self, objeto, valor_minimo):
        self.objeto = objeto
        self.valor_minimo = valor_minimo
        self.participantes = []
        self.lances = []

    def adicionar_participante(self, participante):
        self.participantes.append(participante)

    def realizar_leilao(self):
        print("\n\n")
        print(f"Iniciando leilão para o objeto '{self.objeto}' com lance mínimo de R${self.valor_minimo}")
        for participante in self.participantes:
            print(f"Participante: {participante.nome} ({participante.email})")

        while len(self.participantes) > 1:
            for participante in self.participantes:
                if len(self.participantes) == 1:
                    break
                continuar = input(f"{participante.nome} deseja participar/continuar no leilão? (s/n): ")
                if continuar.lower() == 'n':
                    self.participantes.remove(participante)
                elif continuar.lower() == 's':
                    lance = float(input(f"\n{participante.nome}, dê seu lance (lance mínimo: R${self.valor_minimo}): "))
                    if lance < self.valor_minimo:
                        print("Lance deve ser maior ou igual ao lance mínimo.")
                        continue
                    self.lances.append((participante, lance))
                    self.mostrar_lances()
                    self.valor_minimo = lance  # Atualiza o lance mínimo

        vencedor, lance_vencedor = self.lances[-1]
        print(f"\nLeilão finalizado! O vencedor é: {vencedor.nome} ({vencedor.email}) com lance de R${lance_vencedor} no {self.objeto}.")


    def mostrar_lances(self):
        print("\nLances até o momento:")
        for participante, lance in self.lances:
            print(f"{participante.nome}: R${lance}")