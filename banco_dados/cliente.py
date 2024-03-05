import pandas as pd 
import csv 

class Cliente:
    def __init__(self):
        self.nome = None
        self.email = None
        self.objeto = None
        self.valor_min = None
        self.conta = None
        self.agencia = None 
        self.pix = None

    def get_cadastro_leiloeiro(self):
        cadastro = {'nome': [], 'email': [], 'objeto': [], 'valor_min': []}
        
        for i in range(2):
            print("Dados do Cadastro Leiloeiro")
            nome = input("Nome: ")
            email = input("Email: ")
            objeto = input("Objeto: ")
            valor_min = input("Valor minimo: ")
            print("\n")

            cadastro['nome'].append(nome)
            cadastro['email'].append(email)
            cadastro['objeto'].append(objeto)
            cadastro['valor_min'].append(float(valor_min))

        df = pd.DataFrame(cadastro)
        df.to_csv("bd_leiloeiro.csv", index=False)
    
    def get_cadastro_comprador(self):
        cadastro = {'nome': [], 'email': [], 'celular': [], 'conta': [], 'agencia': [], 'pix': []}
        
        for i in range(1):
            print("Dados do Cadastro Comprador")
            nome = input("Nome: ")
            email = input("Email: ")
            objeto = input("celular: ")
            print("\nDados Bancarios")
            conta = input("Conta: ")
            agencia = input("Agencia:")
            pix = input("Pix:")
            print("\n")

            cadastro['nome'].append(nome)
            cadastro['email'].append(email)
            cadastro['celular'].append(objeto)
            cadastro['conta'].append(int(conta))
            cadastro['agencia'].append(int(agencia))
            cadastro['pix'].append(pix)
        
        df = pd.DataFrame(cadastro)
        df.to_csv("bd_comprador.csv", index=False)
