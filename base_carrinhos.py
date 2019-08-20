# Interface do módulo {base_carrinhos}

# Interfaces importadas por esta interface:
import carrinho
import usuario

# Implementaçao deste módulo:
import base_carrinhos_IMP

# Funções exportadas por este módulo:

def lista_todos_carrinhos(user):
  """Dado um usuario {user}, devolve uma lista Python de objetos da classe {Carrinho}, 
  consistindo de todos os carrinho do usuario {usr} na base, em ordem cronologica de criação. 
  Se nao houver nenhum carrinho desse usuario na base, devolve {None}."""
  return base_carrinhos_IMP.lista_todos()

def armazena(car):
  """Dado um carrinho {car} da classe {Carrinho}, adiciona o {car} na base de dados de carrinhos,
  ou substitui se já existir"""

def remove_carrinho(car):
  """Dado um objeto carrinho {car} da classe {Carrinho} associado a um usuario, remove o carrinho
  e retorna {True}. Se o carrinho não estiver associado ao usuario, devolve {False}"""
  return base_carrinhos_IMP.remove()
