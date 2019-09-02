#! /usr/bin/python3

import base
import base_sessoes
import identificador

class Sessao_IMP:
    def __init__(self):
        self.id = None
        self.usr = None

    def aberta(self):
        return self.usr is not None

    def login(self, usr):
        self.usr = usr

    def logout(self):
        self.usr = None
        
    def obtem_usuario(self):
        return self.usr

    def obtem_identificador(self):
        return self.id

def cria(bas):
    ses = Sessao_IMP()
    ind = base_sessoes.acrescenta(bas,ses)
    ses.id = identificador.de_indice("S",ind)
    return ses
