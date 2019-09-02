#! /usr/bin/python3

# Funções para acesso à base de dados das sessões.

# Implementação desta interface:
import base_sessoes_IMP

# Cada entrada da base de sessões tem os mesmos atributos de um objeto de 
# classe {Sessao}, menos o identificador.  Cada entrada tem um índice 
# inteiro (chave primária) que é atribuído quando a entrada é criada.

# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base}
# que representa a base de dados da loja.

def busca_por_indice(bas,ind):
  """Devolve um objeto da classe {Sessao} extraído da base de sessões, 
  dado seu índice inteiro {ind} na base."""
  return base_sessoes_IMP.busca_por_indice(bas,ind)

def acrescenta(bas,ses):
  """Dado um objeto {ses} da classe {Sessao}, acrescenta uma nova entrada na base
  com os dados dessa sessão (menos o identificador, que é ignorado).  Devolve o 
  índice inteiro da sessão na base."""
  return base_sessoes_IMP.acrescenta(bas,ses)

def atualiza(bas,ind,ses):
  """Dado um objeto {ses} da classe {Sessao}, atualiza
  a entrada de índice {ind} da base com os os atributos de {ses}
  (menos o identificador, que é ignorado).  

  O objeto {ses} não é alterado.  A função não devolve nenhum resultado."""
  base_sessoes_IMP.atualiza(bas,ind,ses)
