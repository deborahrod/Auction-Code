from datetime import datetime

class Participante:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email