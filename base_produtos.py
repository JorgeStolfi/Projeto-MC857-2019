#! /usr/bin/python3
# Last edited on 2019-08-13 20:29:21 by PedroBarcha

# Funções para busca de produtos
# recebidos do usuário.  

# Estas funções devem devolver uma {List} dos produtos 
# compatíveis com a pesquisa feita

# Implementação desta interface:
import base_produtos_IMP

def busca_produto(id):
  """Esta função checa quais campos de busca foram usados pelo usuário, chama as funções de busca correspondente e faz a junção das tabelas retornadas"""
  return base_produtos_IMP.busca_produto_id(dados)

def busca_produto_nome(nome):
  """Esta função processa uma busca por nome"""
  return base_produtos_IMP.busca_produto_nome(dados)

def busca_produto_tipo(tipo):
  """Esta função processa uma busca por tipo de produto"""
  return base_produtos_IMP.busca_produto_tipo(dados)

def busca_produto_id(id):
  """Esta função processa uma busca pelo id do produto"""
  return base_produtos_IMP.busca_produto_id(dados)

def busca_produto_preco(preco_min, preco_max):
  """Esta função processa uma busca por um intervalo de preco"""
  return base_produtos_IMP.busca_produto_preco(dados)