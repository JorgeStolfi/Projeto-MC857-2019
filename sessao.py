#! /usr/bin/python3

# Classe de sessao do projeto MC857.

# Essa classe é responsável por gerenciar a sessão do usuário, 
# realizando o login, logout e recuperando a senha.

import sessao_IMP

class Sessao():
    def login(self, usuario, senha):
        sessao_IMP.login(usuario, senha)

    def logout(self):
        sessao_IMP.logout()

    def recuperar_senha(self, usuario):
        sessao_IMP.recuperar_senha(usuario)


s = Sessao()
s.login('bilbo', '321teste')
s.logout()
s.recuperar_senha('bilbo')