#! /usr/bin/python3

# Classe de sessao do projeto MC857.

# Essa classe é responsável por gerenciar a sessão do usuário, 
# realizando o login, logout e recuperando a senha.

import sessao_IMP

class Sessao():
    def login(self, usuario, senha):
        sessao_IMP.login(usuario, senha)

    def logout(self):
        raise Exception('logout nao implementado')

    def recuperar_senha(self):
        raise Exception('recuperar_senha nao implementado')


s = Sessao()
s.login('Teste 123', '321teste')