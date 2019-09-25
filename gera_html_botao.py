# -*- coding: utf-8 -*-

# Interface do módulo {gera_html_botao}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem elementos do tipo "<button>" ou
# "<input type=submit>", para uso em várias páginas.

# Implementação desta interface:
import gera_html_botao_IMP

# As funções abaixo geram botões "<button>":
def botao_simples(texto, URL, cor_fundo):
  """Função INTERNA para as demais funções de botões "<button>". 
  Retorna HTML do botão "<button>" com texto e cor de fundo especificados.
  Quando clicado, o botão executa um comando HTTP 'GET' para
  o URL dado."""
  return gera_html_botao_IMP.botao_simples(texto, URL, cor_fundo)

def menu_entrar():
  """Retorna fragmento de HTML5 que produz o botao de "Entrar" (login) no menu
  principal. Este botão será exibido em todas as páginas
  quando o usuário estiver navegando pelo site sem estar logado."""
  return gera_html_botao_IMP.menu_entrar()

def menu_sair():
  """Retorna fragmento de HTML5 que representa o botao "Sair" (logout) no menu principal,
  Este botão será exibido em todas as páginas enquanto o usuário estiver logado."""
  return gera_html_botao_IMP.menu_sair()

def menu_cadastrar():
  """Retorna botão que vai ser incluído no menu geral de todas as páginas,
  e pede ao servidor uma página com o formulário para cadastrar um novo usuário."""
  return gera_html_botao_IMP.menu_cadastrar()

# As funções abaixo geram botões "<input type=submit>" para uso dentro de "<form>...</form>":

def submit_ver_produto():
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'VER', 
  para uso em um bloco de descrição resumida do produto.  Por este botão
  o usuário pede ao servidor uma página mostrando o produto em detalhe."""
  return gera_html_botao_IMP.submit_ver_produto()

def submit_comprar_produto():
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'COMPRAR',
  para uso em uma página com descrição detalhada de um produto.  Por este botão
  o usuário pede ao servidor a inclusão do produto no seu carrinho de compras. """
  return gera_html_botao_IMP.submit_comprar_produto()

def submit_buscar_produtos():
  """Retorna HTML um fragmento HTML que descreve um botão <submit> com o texto 'BUSCAR',
  para uso em formulario de busca de produtos por palavras. Por este botão
  o usuário pede ao servidor que mostre a lista de todos os produtos que 
  satisfazem um critério especificado."""
  return gera_html_botao_IMP.submit_buscar_produtos()
  
def submit_cadastrar_usuario():
  """Gera apenas o o botão "cadastrar" que vai estar dentro de um <form>...</form>, dentro da página de cadastrar novo usuário"""
  return gera_html_botao_IMP.submit_cadastrar_usuario()

def submit_entrar():
  """Retorna o botão para a submissão de entrar"""
  return gera_html_botao_IMP.submit_entrar()

def submit_sair():
  """Retorna o botão para a confirmação de sair"""
  return gera_html_botao_IMP.submit_sair()

def inicio():
  """Retorna o botão que redireciona a tela inicia"""
  return gera_html_botao_IMP.botao_inicio()

def carrinho():
  """Retorna o botão que redireciona para a pagina do carrinho"""
  return gera_html_botao_IMP.botao_carrinho()