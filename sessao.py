#! /usr/bin/python3

# Classe de sessao do projeto MC857.

# Essa classe é responsável por gerenciar a sessão do usuário, 
# realizando o login, logout e recuperando a senha.

import usuario
from usuario import Usuario

import sessao_IMP
from sessao_IMP import Sessao_IMP

def cria():
    Sessao_IMP.cria()

class Sessao():
    sessao_aberta = False

    def login(self, usr):
        """Faz o login do usuário"""
        Sessao_IMP.login(self, usr)

    def logout(self):
        """Faz o logout do usuario"""
        Sessao_IMP.logout(self)
	
    def aberta(self):
	"""Verifica se a sessão está aberta"""        
	return Sessao_IMP.aberta(self)

    def obtem_usuario(self):
	"""Retorna o usuário logado na sessão"""
        return Sessao_IMP.obtem_usuario(self)
