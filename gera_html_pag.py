# Interface do módulo {gera_html_pag}.
# As funções deste módulo retornam cadeias de caracteres que são 
# páginas completas em HTML5.

# Interfaces importadas por esta interface:

# Implementaçao deste módulo:
import gera_html_pag_IMP

# Nas funções abaixo, o parâmetro {ses} é um objeto da classe {ObjSessao}
# que representa a sessão de login corrente; ou {None} se o usuário
# nao está logado.

def principal(ses):
  """Retorna a página de entrada da loja (homepage)."""
  return gera_html_pag_IMP.principal(ses)

def mostra_produto(ses, prod, qt):
  """Retorna uma página com descrição detalhada do produto {prod}.
  Se {qt} não for {None}, mostra a quantidade {qt}
  e o preço para essa quantidade.  Se {qt} for {None},
  mostra o preço unitário, sem a quantidade."""
  return gera_html_pag_IMP.mostra_produto(ses, prod, qt)
  
def lista_de_produtos(ses, idents):
  """Dada uma lista {idents} de identificadores de produtos,
  retorna uma página mostrando todos esses produtos."""
  return gera_html_pag_IMP.lista_de_produtos(ses, idents)

def entrar(ses):
  """Retorna uma página contendo o formulário de entrar (login),
  com campos para entrada de usuário e senha e um botão 
  "Entrar" para submeter o formulário."""
  return gera_html_pag_IMP.entrar(ses)

def cadastrar_usuario(ses):
  """Retorna uma página de cadastro de usuário que contém um formulário 
  para entrada dos dados de um objeto usuário, e um botão "Cadastrar"
  para submeter o formulário."""
  return gera_html_pag_IMP.cadastrar_usuario(ses)

def mostra_usuario(ses, usr):
  """Retorna uma página que contém as informações do usuário {usr},
  por exemplo para feedback depois de cadastrá-lo."""
  return gera_html_pag_IMP.mostra_usuario(ses, usr)

def mostra_carrinho(ses):
  """Retorna uma página com a lista dos produtos no carrinho da sessão {ses}."""
  return gera_html_pag_IMP.mostra_carrinho(ses)

def mostra_compra(ses, cpr):
  """Retorna uma página com a lista dos produtos no pedido de compra {cpr}."""
  return gera_html_pag_IMP.mostra_compra(ses, cpr)

def mensagem_de_erro(ses, msg):
  """Retorna uma página de erro com a mensagem (msg) informada"""
  return gera_html_pag_IMP.mensagem_de_erro(ses, msg)

def lista_de_compras(ses, idents):
  """Retorna uma página com a lista de todas as compras realizadas por um usuário {usr}"""
  return gera_html_pag_IMP.lista_de_compras(ses, idents)

# Utilitários

def generica(ses, conteudo):
  """Retorna uma página com cabeçalho, menus, e rodapé padrões do projeto,
  e o {conteudo} dado (um {string} em formato HTML5)."""
  return gera_html_pag_IMP.generica(ses, conteudo)
