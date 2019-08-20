#! /usr/bin/python3

# Classe de sessao do projeto MC857.

# Essa classe é responsável por gerenciar a sessão do usuário, 
# realizando o login, logout e recuperando a senha.

import sessao_IMP
from sessao_IMP import Sessao_IMP

def cria():
    s = Sessao()
    return s

class Sessao():
    sessao_aberta = False

    def __self__(self):
        Sessao_IMP(self)

    def login(self, usr):
        """Faz o login do usuario
           Parametros
            ----------
            usr : Usuario
                Objeto da classe Usuario
        """
        Sessao_IMP.login(self, usr)

    def logout(self):
        """Faz o logout do usuario"""
        Sessao_IMP.logout(self)

    def aberta(self):
        return Sessao_IMP.aberta(self)
    
    #TODO: Descomentar esse método quando a classe Usuario estiver corrigida
    # def obtem_usuario(self):
    #     return Sessao_IMP.obtem_usuario(self)