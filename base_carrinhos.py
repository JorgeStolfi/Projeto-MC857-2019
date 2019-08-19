# Interface do módulo {base_carrinhos}

# Interfaces importadas por esta interface:
import carrinho
import usuario

# Implementaçao deste módulo:
import base_carrinhos_IMP

# Funções exportadas por este módulo:

def get_carrinho(usuario):
  """Dado um usuario, retornar o carrinho do usuario."""
  return base_carrinhos_IMP.get_carrinho()

def lista_todos_carrinhos(usuario):
  """Dado um usuario, retornar a lista com todos os carrinhos do usuario."""
  return base_carrinhos_IMP.lista_todos_carrinhos()

def cria_novo_carrinho(usuario):
  """Dado um usuario, criar um novo carrinho para ele."""
  return base_carrinhos_IMP.cria_novo_carrinho()

def remove_carrinho(usuario, carrinho):
  """Dado um usuario e o carrinho desejado, remove de sua base de carrinhos."""
  return base_carrinhos_IMP.remove_carrinho()