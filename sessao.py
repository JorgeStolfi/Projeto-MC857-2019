#! /usr/bin/python3

# Classe de sessao do projeto MC857.

# Essa classe é responsável por gerenciar a sessão do usuário, 
# realizando o login, logout e recuperando a senha.

import sessao_IMP
from sessao_IMP import Sessao_IMP

class Sessao():
    def login(self, usuario, senha):
        """Faz o login do usuario"""
        Sessao_IMP.login(self, usuario, senha)

    def logout(self):
        """Faz o logout do usuario"""
        Sessao_IMP.logout(self)

    def recuperar_senha(self, usuario):
        """Recuepera a senha do usuario"""
        Sessao_IMP.recuperar_senha(self, usuario)

    def aberta(self):
        return Sessao_IMP.aberta(self)


s = Sessao()
s.login('bilbo', '321teste')
s.logout()
s.recuperar_senha('bilbo')

if s.aberta():
    print('aberta')
else:
    print('fechada')