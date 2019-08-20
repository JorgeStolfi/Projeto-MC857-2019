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

    def login(self):
        """Faz o login do usuario"""
        Sessao_IMP.login(self)

    def logout(self):
        """Faz o logout do usuario"""
        Sessao_IMP.logout(self)

    def aberta(self):
        return Sessao_IMP.aberta(self)
    
    #TODO: Descomentar esse método quando a classe Usuario estiver corrigida
    # def obtem_usuario(self):
    #     return Sessao_IMP.obtem_usuario(self)


s = cria()
if s.aberta():
    print('aberta')
else:
    print('fechada')

s.login()
if s.aberta():
    print('aberta')
else:
    print('fechada')

s.logout()
if s.aberta():
    print('aberta')
else:
    print('fechada')