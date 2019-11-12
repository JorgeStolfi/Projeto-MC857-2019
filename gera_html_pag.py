# Interface do módulo {gera_html_pag}.
# As funções deste módulo retornam cadeias de caracteres que são 
# páginas completas em HTML5.

# Interfaces importadas por esta interface:

# Implementaçao deste módulo:
import gera_html_pag_IMP

# Nas funções abaixo, o parâmetro {ses} é um objeto da classe {ObjSessao}
# que representa a sessão de login corrente; ou {None} se o usuário
# nao está logado.
# 
# Nas funções abaixo, o parâmetro {erros} é uma lista de mensagens de erro 
# que serão mostradas no alto da página devolvida.  Se for um string, ele é
# dividido em mensagens separadas nas quebtas de linha '\n'.
# Se for {None}. ou uma cadeia ou lista vazia, supõe que não há mensagens.

def principal(ses, erros):
  """Retorna a página de entrada da loja (homepage)."""
  return gera_html_pag_IMP.principal(ses, erros)

def mensagem_de_erro(ses, msg):
  """Retorna uma página de erro com a mensagem de erro {msg}.  O parâmetro 
  {erros} pode ser um string ou uma lista de strings.  
  
  A página terá um botão "OK" que, quando clicado, gera um comando
  "GET" com URL "principal"."""
  return gera_html_pag_IMP.mensagem_de_erro(ses, msg)

def mostra_produto(ses, id_compra, prod, qtd, erros):
  """Retorna uma página com descrição detalhada do produto {prod},
  como construída pro {gera_html_elem.bloco_de_produto(id_compra, prod, qtd, True)},
  e um botão 'Comprar'.
  
  Se {qtd} não for {None}, mostra a quantidade {qtd}
  e o preço para essa quantidade.  Se {qtd} for {None},
  mostra o preço unitário, sem a quantidade.
  
  O parâmetro {id_compra}, se não for {None}, será incluído nos argumentos do POST
  gerado pelo botão "Comprar".  Nesse caso, deve ser o identificador do pedido de
  compra ao qual o produto deve ser acrescentado."""
  return gera_html_pag_IMP.mostra_produto(ses, id_compra, prod, qtd, erros)
  
def lista_de_produtos(ses, idents, erros):
  """Dada uma lista {idents} de identificadores de produtos,
  retorna uma página mostrando a descrição resumida de todos esses produtos.
  
  Cada descrição será gerada por {gera_html_elem.bloco_de_produto(None, prod, qtd, False)},
  e terá um botão 'Ver' para mostrar a descrição detalhada."""
  return gera_html_pag_IMP.lista_de_produtos(ses, idents, erros)

def entrar(ses, erros):
  """Retorna uma página contendo o formulário de entrar (login),
  com campos para entrada de usuário e senha e um botão 
  "Entrar" para submeter o formulário."""
  return gera_html_pag_IMP.entrar(ses, erros)

def cadastrar_usuario(ses, atrs, erros):
  """Retorna uma página com o formulário de cadastramento de 
  novo usuario.
  
  O formulário tem entradas adicionais se a sessão {ses} não for
  {None} e o usuário da mesma for um administrador.  
  Vide detalhes em {gera_html_form.cadastrar_usuario}. 
  
  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos."""
  return gera_html_pag_IMP.cadastrar_usuario(ses, atrs, erros)

def alterar_usuario(ses, id_usuario, atrs, erros):
  """Retorna uma página com formulário para alterar os dados
  do usuário {usr} cujo identificador é {id_usuario}
  e cujos atributos correntes são {atrs}.
  
  O formulário é tem entradas adicionais se o usuário da sessão {ses}
  (NÃO o usuário que está sendo alterado) é  um administrador.  
  Vide detalhes em {gera_html_form.alterar_usuario}."""
  return gera_html_pag_IMP.alterar_usuario(ses, id_usuario, atrs, erros)

def alterar_endereco(ses, id_compra, atrs, erros):
  """Retorna uma página que mostra o endereço de entrega de um pedido de compra
  cujo identificador está em {id_compra}, com campos editáveis pelo usuário.
  Os valores iniciais desses campos são especificados pelo dicionário 
  {atrs}.  A página inclui tambem um botão "Confirmar".  
  Vide {gera_html_form.preencher_endereco} para mais detalhes. """
  return gera_html_pag_IMP.alterar_endereco(ses, id_compra, atrs, erros)

def escolher_pagamento(ses, id_compra, atrs, erros):
  """ !!! Documentar !!! """
  return gera_html_pag_IMP.escolher_pagamento(ses, erros)

def mostra_carrinho(ses, erros):
  """Retorna uma página com os dados do carrinho de compras {cpr} da sessão {ses}, como 
  descrito em {gera_html_elem.bloco_de_compra(cpr,detalhe=True)}."""
  return gera_html_pag_IMP.mostra_carrinho(ses, erros)

def mostra_compra(ses, cpr, erros):
  """Retorna uma página com os dados da compra {cpr}, como 
  descrito em {gera_html_elem.bloco_de_compra(cpr,detalhe=True)}. """
  return gera_html_pag_IMP.mostra_compra(ses, cpr, erros)

def lista_de_compras(ses, idents, erros):
  """Retorna uma página com a lista de todas as compras realizadas por um usuário {usr}. 
  O parâmetro {idents} deve ser uma lista de strings que são os identificadores "C-{NNNNNNNN}" 
  das compras a mostrar.
  
  Para cada compra {cpr} cujo identificador estiver na lista, a página mostrará
  a descrição resumida da compra, como especificado em 
  {gera_html_elem.bloco_de_compra(cpr,detalhe=False)}."""
  return gera_html_pag_IMP.lista_de_compras(ses, idents, erros)

def mostra_sessao(ses, erros):
  """Retorna uma página que mostra os dados da sessão {ses}."""
  return gera_html_pag_IMP.mostra_sessao(ses, erros)

# Utilitários

def generica(ses, conteudo, erros):
  """Retorna uma página com cabeçalho, menus, e rodapé padrões do projeto,
  e o {conteudo} dado (um {string} em formato HTML5)."""
  return gera_html_pag_IMP.generica(ses, conteudo, erros)
