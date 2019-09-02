#! /usr/bin/python3

# Classe de sessao do projeto MC857.

from sessao_IMP import Sessao_IMP
import sessao_IMP

class Sessao(Sessao_IMP):
  """Um objeto desta classe representa uma sessao de acesso ao
  servidor.  Cada sessao pertence a um unico usuario. A sessao e criada
  e "aberta" quando o usuario faz login, e e "fechada" no logout. Um mesmo
  usuario pode ter varias sessoes abertas ao mesmo tempo."""

  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'S-{NNNNNNNN}', onde 
    {NNNNNNNN} e um numero de 8 algarismos 
    que identifica unicamente a sessao. Este identificador e 
    atribuido na criacao da sessao e nao pode ser alterado."""
    return Sessao_IMP.obtem_identificador(self)

  def login(self, usr):
    """Faz o login do usuario
       Antes de chamar esta funcao e necessario realizar logout, caso alguem ja esteja logado
       O parametro do usr deve ser um objeto do tipo Usuario
       A funcao nao possue retorno"""
    Sessao_IMP.login(self, usr)

  def logout(self):
    """Faz o logout do usuario
       apos o logout todas as chamadas ao metodo 'aberta' retornara false
    """
    Sessao_IMP.logout(self)

  def aberta(self):
    """Retorna True se a sessao esta aberta, caso contrario False"""
    return Sessao_IMP.aberta(self)

  def obtem_usuario(self):
    """Retorna o um objeto do tipo Usuario, para o usuario logado na sessao"""
    return Sessao_IMP.obtem_usuario(self)
    
# Construtor da classe:

def cria(bas):
  """Cria um novo objeto da classe {Sessao}, inicialmente fechada e sem usuario."""
  return sessao_IMP.cria(bas)
