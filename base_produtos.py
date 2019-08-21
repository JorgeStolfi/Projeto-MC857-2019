#!/usr/bin/python3

#Pedro Henrique Barcha Correia (PedroBarcha)
#158338
#Última Atualização: 20/08

#Funções para busca de produtos
#(requisições feitas pelo usuário).  

#Estas funções devolvem um ou mais objetos da classe {Produto}, 
#compatíveis com a pesquisa feita

#Implementação desta interface:
import base_produtos_IMP

def conecta():
  """Abre conexao com a base de dados"""
  return base_produtos_IMP.conecta()

def desconecta(conexao_mysql):
  """Fecha conexao com a base de dados"""
  return base_produtos_IMP.desconecta(conexao_mysql)


def busca_por_nome(nome, conexao_mysql):
  """Devolve uma lista Python de objetos da classe {Produto}, consistindo de todos os produtos da base que tem a cadeia {nome} no seu nome, em ordem arbitrária. Se não houver nenhum produto que satisfaça essa busca, devolve {None}."""
  return base_produtos_IMP.busca_por_nome(nome, conexao_mysql)

def busca_por_id(id, conexao_mysql):
  """Devolve um único objeto da classe {Produto}, com o produto da base que tem a cadeia {id} em seu identificador. Se não houver nenhum produto que satisfaça essa busca, devolve {None}."""
  return base_produtos_IMP.busca_por_id(id, conexao_mysql)
