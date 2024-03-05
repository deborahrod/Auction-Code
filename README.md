# Auction-Code

Este é um sistema de leilão implementado em Python, onde os usuários podem participar de leilões, dar lances e competir para ganhar itens leiloados.

## Funcionalidades

- Listagem de Leilões, com filtro por estado (ABERTOS, FINALIZADOS, EXPIRADOS e INATIVOS).
- Cadastro de leilões com estados de INATIVO, ABERTO, EXPIRADO e FINALIZADO.
- Recebimento de lances durante o leilão, respeitando as regras estabelecidas.
- Finalização de leilões expirados, determinando um vencedor, se houver.
- Envio de e-mail ao vencedor do leilão.
- Registro de participantes pré-cadastrados.
- Acesso à lista de lances de um leilão específico.
- Identificação do maior e menor lance efetuado em um leilão.

## Como usar

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/sistema-leilao.git
```

## 1. Certifique-se de ter o Python instalado em sua máquina.

## 2. Execute o arquivo principal do sistema:

```bash
python main.py
```
## 3. Siga as instruções apresentadas no console para interagir com o sistema de leilão.

# Teste Unitários 

## O sistema possui testes unitários para garantir o correto funcionamento das principais funcionalidades. Para executar os testes, utilize o seguinte comando:

```bash
python -m unittest
```
