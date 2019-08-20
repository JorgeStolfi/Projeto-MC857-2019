#! /usr/bin/python3
# Last edited on 2019-08-13 00:32:21 by stolfilocal

# Interface do módulo {gera_html_pag}.
# As funções deste módulo retornam cadeias de caracteres que são 
# páginas completas em HTML5.

# Interfaces importadas por esta interface:

# Implementaçao deste módulo:
import gera_html_pag_IMP

# Funções exportadas por este módulo:

def entrada():
  """Retorna a página de entrada do projeto."""
  return gera_html_pag_IMP.entrada()

def generica(conteudo):
  """Retorna uma página com cabeçalho, menus, e rodapé padrões do projeto, e o {conteudo} dado (um {string} em formato HTML5)."""
  return gera_html_pag_IMP.generica(conteudo)

def produto(prod):
  """Retorna uma página com os elementos referentes ao produto passado como parâmetro, como nome, categoria, preço, quantidade disponíve"""
  return gera_html_pag_IMP.produto(prod)
  
def lista_de_produtos(lista):
  """Retorna uma página contendo todos os produtos de determinado tipo do site."""
  return gera_html_pag_IMP.produtos(lista)

def login():
  """Retorna uma página contendo o fomulário de login. """
  return gera_html_pag_IMP.login()

def cadastrar_usuario():
  """Retorna uma página de cadastro de usuário que contém os campos do objeto usuário e um botão para submeter o cadastro."""
  return gera_html_pag_IMP.cadastrar_usuario()
