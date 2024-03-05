import csv
import unicodedata

# Função para remover acentos de uma string
def remover_acentos(texto):
    return ''.join(ch for ch in unicodedata.normalize('NFD', texto) if not unicodedata.combining(ch))

arquivo_entrada = 'C:\\Users\\deborah\\Área de Trabalho\\Teste de Software\\leilao\\bd_comprador.csv'
arquivo_saida = 'C:\\Users\\deborah\\Área de Trabalho\\Teste de Software\\leilao\\comprador.csv'


# Abre o arquivo de entrada para leitura e o arquivo de saída para escrita
with open(arquivo_entrada, 'r', encoding='utf-8') as csv_entrada, \
        open(arquivo_saida, 'w', newline='', encoding='utf-8') as csv_saida:
    # Cria um leitor e um escritor CSV
    leitor_csv = csv.reader(csv_entrada)
    escritor_csv = csv.writer(csv_saida)

    # Itera sobre cada linha do arquivo de entrada
    for linha in leitor_csv:
        # Remove os acentos de cada campo da linha
        linha_sem_acentos = [remover_acentos(campo) for campo in linha]
        # Escreve a linha sem acentos no arquivo de saída
        escritor_csv.writerow(linha_sem_acentos)

print("Acentos removidos com sucesso. Verifique o arquivo de saída:", arquivo_saida)
