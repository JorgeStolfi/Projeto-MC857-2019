# -*- coding: utf-8 -*-

# Interface do módulo {gera_html_botao}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem elementos do tipo "<button>" ou
# "<input type=submit>", para uso em várias páginas.

# Implementação desta interface:
import gera_html_botao_IMP

# As funções abaixo geram botões "<button>":
def botao_simples(texto, cor_fundo):
  """Função INTERNA para as demais funções de botões "<button>". Retorna HTML do botão "<button>" com texto e cor de fundo especificados."""
  return gera_html_botao_IMP.botao_simples(texto, cor_fundo)

def login():
  """Retorna fragmento de HTML5 que representa o botao de login"""
  return gera_html_botao_IMP.login()

def logout():
  """Retorna fragmento de HTML5 que representa o botao de logout"""
  return gera_html_botao_IMP.logout()

def cadastra():
  """Retorna botão que vai ser incluído no menu geral de todas as páginas, e pede ao servidor uma página com o formulário para cadastrar um novo usuário."""
  return gera_html_botao_IMP.cadastrar()


# As funções abaixo geram botões "<input type=submit>" para uso dentro de "<form>...</form>":
def botao_submit(texto, cor_fundo):
  """Função INTERNA para as demais funções de botões "<input type=submit>". Retorna HTML do botão <submit> com texto e cor de fundo especificados."""
  return gera_html_botao_IMP.subm_botao_simples(texto, cor_fundo)

def submit_compra():
  """Retorna um botão simples que é um fragmento HTML com o texto 'COMPRAR'."""
  return gera_html_botao_IMP.subm_comprar()

def submit_busca():
  """Retorna HTML do botão <submit> para uso em formulario de busca."""
  return gera_html_botao_IMP.subm_busca()
  
def submit_cadastrar():
  """Gera apenas o o botão "cadastrar" que vai estar dentro de um <form>...</form>, dentro da página de cadastrar novo usuário"""
  return gera_html_botao_IMP.subm_cadastrar()

def submit_login():
  """Retorna o botão para a submissão de login"""
  return gera_html_botao_IMP.subm_login()

def submit_logout():
  """Retorna o botão para a confirmação de logout"""
  return gera_html_botao_IMP.subm_logout()


