#! /usr/bin/python3

# Classe de sessao do projeto MC857.

import usuario
from usuario import Usuario

import sessao_IMP
from sessao_IMP import Sessao_IMP

class Sessao():
  """Um objeto desta classe representa uma sessão de acesso ao 
  servidor.  Cada sessão pertence a um único usuário. A sessão é criada 
  e "aberta" quando o usuário faz login, e é "fechada" no logout. Um mesmo 
  usuário pode ter várias sessões abertas ao mesmo tempo."""

  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'S-{NNNNNNNN}', onde 
    {NNNNNNNN} é um número de 8 algarismos 
    que identifica unicamente a sessão. Este identificador é 
    atribuído na criação da sessão e não pode ser alterado."""
    return sessao_IMP.obtem_identificador(self)

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

def cria():
  """Cria um novo objeto da classe {Sessao}, inicialmente fechada e sem usuário."""
  Sessao_IMP.cria()
