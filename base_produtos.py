#!/usr/bin/python3

#Pedro Henrique Barcha Correia (PedroBarcha)
#158338
#Última Atualização: 13/08

# Funções para busca de produtos
# recebidos do usuário.  

# Estas funções devem devolver uma {List} dos produtos 
# compatíveis com a pesquisa feita

# Implementação desta interface:
import base_produtos_IMP

def conecta():
  """Devolve uma conexao com a base Produto. Se houver algum erro, devolve {None}."""
  return base_produtos_IMP.conecta()

def busca_por_nome(nome):
  """Devolve uma lista Python de objetos da classe {Produto}, consistindo de todos os produtos da base que tem a cadeia {nome} no seu nome, em ordem arbitrária. Se não houver nenhum produto que satisfaz essa busca, devolve {None}."""
  return base_produtos_IMP.busca_por_nome(nome)

def busca_por_id(id):
  """Devolve um objetos da classe {Produto}, consistindo do produto da base que tem a cadeia {id} no seu id. Se não houver nenhum produto que satisfaz essa busca, devolve {None}."""
  return base_produtos_IMP.busca_por_id(id)