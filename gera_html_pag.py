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

def mostra_produto(ses, id_compra, prod, qtd):
  """Retorna uma página com descrição detalhada do produto {prod},
  como construída pro {gera_html_elem.bloco_de_produto(id_compra, prod, qtd, True)},
  e um botão 'Comprar'.
  
  Se {qtd} não for {None}, mostra a quantidade {qtd}
  e o preço para essa quantidade.  Se {qtd} for {None},
  mostra o preço unitário, sem a quantidade.
  
  O parâmetro {id_compra}, se não for {None}, será incluído nos argumentos do POST
  gerado pelo botão "Comprar".  Nesse caso, deve ser o identificador do pedido de
  compra ao qual o produto deve ser acrescentado."""
  return gera_html_pag_IMP.mostra_produto(ses, id_compra, prod, qtd)
  
def lista_de_produtos(ses, idents):
  """Dada uma lista {idents} de identificadores de produtos,
  retorna uma página mostrando a descrição resumida de todos esses produtos.
  
  Cada descrição será gerada por {gera_html_elem.bloco_de_produto(None, prod, qtd, False)},
  e terá um botão 'Ver' para mostrar a descrição detalhada."""
  return gera_html_pag_IMP.lista_de_produtos(ses, idents)

def entrar(ses):
  """Retorna uma página contendo o formulário de entrar (login),
  com campos para entrada de usuário e senha e um botão 
  "Entrar" para submeter o formulário."""
  return gera_html_pag_IMP.entrar(ses)

def cadastrar_usuario(ses):
  """Retorna uma página de cadastro de usuário que contém um formulário 
  para entrada dos dados de um objeto usuário, e um botão "Cadastrar"
  que emite um comando 'definir_dados_de_usuario', sem parametro 'id_usuario'."""
  return gera_html_pag_IMP.cadastrar_usuario(ses)

def mostra_usuario(ses, usr):
  """Retorna uma página que contém as informações do usuário {usr},
  por exemplo para feedback depois de cadastrá-lo. Os campos 
  estarão já preenchidos com os daddos do usuário {usr} (menos a
  senha). Os campos serão editáveis (menos email e CPF). No fundo da
  página  haverá um botão "Alterar" que emite um comando 
  'definir_dados_de_usuario', com o mesmo campo 'id_usuario'."""
  return gera_html_pag_IMP.mostra_usuario(ses, usr)

def mostra_carrinho(ses):
  """Retorna uma página com os dados do carrinho de compras {cpr} da sessão {ses}, como 
  descrito em {gera_html_elem.bloco_de_compra(cpr,detalhe=True)}."""
  return gera_html_pag_IMP.mostra_carrinho(ses)

def mostra_compra(ses, cpr):
  """Retorna uma página com os dados da compra {cpr}, como 
  descrito em {gera_html_elem.bloco_de_compra(cpr,detalhe=True)}. """
  return gera_html_pag_IMP.mostra_compra(ses, cpr)

def lista_de_compras(ses, idents):
  """Retorna uma página com a lista de todas as compras realizadas por um usuário {usr}. 
  O parâmetro {idents} deve ser uma lista de strings que são os identificadores "C-{NNNNNNNN}" 
  das compras a mostrar.
  
  Para cada compra {cpr} cujo identificador estiver na lista, a página mostrará
  a descrição resumida da compra, como especificado em 
  {gera_html_elem.bloco_de_compra(cpr,detalhe=False)}."""
  return gera_html_pag_IMP.lista_de_compras(ses, idents)

def mensagem_de_erro(ses, msg):
  """Retorna uma página de erro com a mensagem (msg) informada"""
  return gera_html_pag_IMP.mensagem_de_erro(ses, msg)

# Utilitários

def generica(ses, conteudo):
  """Retorna uma página com cabeçalho, menus, e rodapé padrões do projeto,
  e o {conteudo} dado (um {string} em formato HTML5)."""
  return gera_html_pag_IMP.generica(ses, conteudo)
