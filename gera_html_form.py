#! /usr/bin/python3

# Interface do módulo {gera_html_form}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem formularios <form>...</form>, 
# para inclusão em outras páginas.

# Implementação desta interface:
import gera_html_form_IMP

# Funções exportadas por este módulo:

def busca():
  """Retorna HTML de um formulario para busca textual no cadastro de produtos."""
  return gera_html_form_IMP.busca()

def comprar(id_produto,qtd_produto):
  """Retorna um fragmento HTML que contem o formulãrio de submissão de uma compra, juntamente com o botão comprar.

  Os parâmetros {id_produto} e {qtd_produto} especificam o id do produto
  da qual se quer comprar e a quantidade de produtos desejados, respectivamente."""

  return gera_html_form_IMP.comprar(id_produto,qtd_produto)

def login():
  """Retorna o botão para a submissão de login"""
  return gera_html_form_IMP.login()

def cadastrar_usuario():
    """Retorna o <form> para cadastro do usuario"""
    return gera_html_form_IMP.cadastrar_usuario()
