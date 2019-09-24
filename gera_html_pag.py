# Interface do módulo {gera_html_pag}.
# As funções deste módulo retornam cadeias de caracteres que são 
# páginas completas em HTML5.

# Interfaces importadas por esta interface:

# Implementaçao deste módulo:
import gera_html_pag_IMP

# Funções exportadas por este módulo:

def entrada_da_loja(sessao, dados):
  """Retorna a página de entrada da loja (homepage)."""
  return gera_html_pag_IMP.entrada_da_loja()

def mostra_produto(prod, qt):
  """Retorna uma página com descrição detalhada do produto {prod}.
  Se {qt} não for {None}, mostra a quantidade {qt}
  e o preço para essa quantidade.  Se {qt} for {None},
  mostra o preço unitário, sem a quantidade."""
  return gera_html_pag_IMP.mostra_produto(prod, qt)
  
def lista_de_produtos(idents):
  """Sasa uma lista {idents} de identificadores de produtos,
  retorna uma página mostrando todos esses produtos."""
  return gera_html_pag_IMP.lista_de_produtos(idents)

def entrar():
  """Retorna uma página contendo o fomulário de entrar. """
  return gera_html_pag_IMP.entrar()

def cadastrar_usuario():
  """Retorna uma página de cadastro de usuário que contém os campos do objeto usuário e um botão para submeter o cadastro."""
  return gera_html_pag_IMP.cadastrar_usuario()

def carrinho():
  """Retorna uma página de carrinho do usuário."""
  return gera_html_pag_IMP.carrinho()

def mostra_usuario(usr):
  """Retorna uma página que contém as informações do usuário que acabou de ser cadastrado"""
  return gera_html_pag_IMP.mostra_usuario(usr)

def mostra_compra(comp):
  """Retorna uma página com a lista dos produtos no pedido de compra {comp}."""
  return gera_html_pag_IMP.mostra_compra(comp)

# Utilitários

def generica(conteudo):
  """Retorna uma página com cabeçalho, menus, e rodapé padrões do projeto, e o {conteudo} dado (um {string} em formato HTML5)."""
  return gera_html_pag_IMP.generica(conteudo)
