# Interface do módulo {gera_html_form}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem formularios <form>...</form>, 
# para inclusão em outras páginas.

# Implementação desta interface:
import gera_html_form_IMP

# Funções exportadas por este módulo:

def buscar_produtos():
  """Retorna HTML de um formulario para busca textual no cadastro de produtos.
  O formulário deve conter um campo editável onde o usuário entra a palavra a 
  procurar, e um botão de 'Buscar' que solicita a busca ao servidor."""
  return gera_html_form_IMP.buscar_produtos()

def ver_produto(id_produto, qtd_produto):
  """Retorna o HTML de do formulário que mostra apenas um botão 'Ver' (de tipo 'submit').
  Esse botão permite ao usuário solicitar a visualização dos dados detalhados do produto 
  com identificador {id_produto}, na quantidade {qtd_produto}."""
  return gera_html_form_IMP.ver_produto(id_produto, qtd_produto)

def comprar_produto(id_produto, qtd_produto):
  """Retorna o HTML de do formulário que mostra um produto em detalhe, juntamente com o botão 'Comprar'.

  O formulário mostra os dados dos produto {id_produto} e quantidade do mesmo a comprar,
  além de um botão 'Comprar' (de tipo 'submit') que permite ao usuário solicitar a inclusão
  desse produto e quantidade no carrinho de compras.  
  
  A quantidade é apresentada em um campo numérico editável, com conteúdo 
  inicial {qt_produto}. Qualquer alteração feita pelo usuário nesse campo 
  deve causar a emissão de um comando HTTP que solicita ao
  servidor para mostrar novamente a página desse produto, com esse dado alterado."""
  return gera_html_form_IMP.comprar_produto(id_produto, qtd_produto)

def mostra_compra(cpr):
  """Retorna o HTML de do formulário que mostra um pedido de compra {cpr}.

  O formulário mostra os dados dos produtos na compra e as quantidade dos mesmos
  (vide {gera_html_elem.bloco_de_produto}.  Se a compra não estiver completamente 
  fechada mostra o botão adequado, como 'FINALIZAR' ou 'PAGAR'."""
  return gera_html_form_IMP.mostra_compra(cpr)

def entrar():
  """Retorna o HTML do formulário para login do usuário. 
  O formulário contém campos editáveis onde o usuário deverá digitar 
  o email e a senha, e um botão """
  return gera_html_form_IMP.entrar()

def cadastrar_usuario():
    """Retorna o HTML do formulário para para cadastro de um novo
    usuario.  O formuláro contém campos editáveis para os dados 
    de cadastro (nome, email, CPF, etc.) e um botão 'Cadastrar' 
    que solicita ao servidor a criação de tal usuário."""
    return gera_html_form_IMP.cadastrar_usuario()

def erro_generico(msg):
  """Retorna o HTML da pagina de erro com a mensagem (msg) informada"""
  return gera_html_form_IMP.erro_generico(msg)