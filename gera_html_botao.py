#! /usr/bin/python3

# Interface do módulo {gera_html_botao}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem elementos do tipo "<button>" ou
# "<input type=submit>", para uso em várias páginas.

# Implementação desta interface:
import gera_html_botao_IMP

# As funções abaixo geram botões "<button>":

def login():
  """Retorna fragmento de HTML5 que representa o botao de login"""
  return gera_html_botao_IMP.login()

def logout():
  """Retorna fragmento de HTML5 que representa o botao de logout"""
  return gera_html_botao_IMP.logout()

def cadastrar_usuario():
  """retorna botão que vai ser incluído no menu geral de todas as páginas, e pede ao servidor uma página com o formulário para cadastrar um novo usuário."""
  return gera_html_botao_IMP.cadastrar()

def teste_de_popup(texto):
  """Retorna HTML de um botão do menu
  que mostra um popup com o {texto} dado."""
  return gera_html_botao_IMP.teste_de_popup(texto)

# As funções abaixo geram botões "<input type=submit>" para uso dentro de "<form>...</form>":

def subm_comprar():
  """Retorna um botão simples que é um fragmento HTML com o texto 'COMPRAR'."""
  return gera_html_botao_IMP.subm_comprar()

def subm_login(login,senha):
  """Retorna o botão para a submissão de login"""
  return gera_html_botao_IMP.subm_login()

def subm_logout():
  """Retorna o botão para a confirmação de logout"""
  return gera_html_botao_IMP.subm_logout()
  
def subm_cadastrar(texto):
    """Gera apenas o o botão "cadastrar" que vai estar dentro de um <form>...</form>, dentro da página de cadastrar novo usuário
    """
    return gera_html_botao_IMP.subm_cadastrar(texto);

def subm_busca():
  """Retorna HTML do botão <submit> para uso em formulario de busca."""
  return gera_html_botao_IMP.subm_busca()
