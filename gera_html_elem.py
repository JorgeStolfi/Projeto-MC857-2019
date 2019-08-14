#! /usr/bin/python3
# Last edited on 2019-08-12 18:26:26 by stolfilocal

# Interface do módulo {gera_html_elem}.

# As funções desta interface retornam cadeias de caracteres que são 
# fragmentos de código HTML5, usados em várias páginas.

# Implementação desta interface:
import gera_html_elem_IMP

# Funções exportadas por este módulo:

def cabecalho(title):
  """Retorna o cabecalho padrão site, com titulo da página {title}."""
  return gera_html_elem_IMP.cabecalho(title)
  
def rodape():
  """Retorna o rodapé padrão do site."""
  return gera_html_elem_IMP.rodape()
  
def menu_geral():
  """Retorna o menu geral do site."""
  return gera_html_elem_IMP.menu_geral()

def botao_subm_comprar(id_produto,qtd_produto,fam_fonte,tam_fonte,cor_texto,cor_fundo):
  """Retorna um botão que é um fragmento HTML com o texto 'COMPRAR'.

  Os parâmetros {id_produto} e {qtd_produto} especificam o id do produto
  da qual se quer comprar e a quantidade de produtos desejados, respectivamente.
  
  Os parâmetros {fam_fonte} e {tam_fonte} especificam a família e o
  tamanho do fonte a usar (por exemplo 'Helvetica','18px').
  
  Os parâmetros {cor_texto} e {cor_fundo} devem ser cores aceitáveis no
  CSS (por exemplo, '#ff8800')."""
  return gera_html_elem_IMP.botao_subm_comprar()

def botao_subm_login(login,senha):
  """Retorna o botão para a submissão de login"""
  return gera_html_elem_IMP.botao_subm_login()

def bloco_texto(texto,fam_fonte,tam_fonte,pad,halign,cor_texto,cor_fundo):
  """Retorna un string que é um fragmento HTML consistindo do {texto}
  dado, que pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>').
  
  Os parâmetros {fam_fonte} e {tam_fonte} especificam a família e o
  tamanho do fonte a usar (por exemplo 'Helvetica','18px').
  
  O parâmetro {pad}, especifica a largura do espaço extra ('padding') em
  volta do texto como um todo.
  
  O parâmetro {halign} especifica o alinhamento das linhas do texto;
  pode ser 'left', 'center', ou 'right'.
  
  Os parâmetros {cor_texto} e {cor_fundo} devem ser cores aceitáveis no
  CSS (por exemplo, '#ff8800').
  
  Cada parâmetro de estilo pode ser {None} para indicar o defô."""
  return gera_html_elem_IMP.bloco_texto(texto,fam_fonte,tam_fonte,pad,halign,cor_texto,cor_fundo)

def bloco_de_produto(produto):
  """A funcao recebe o parâmetro {produto}, da classe Produto, e recupera
  a partir dele nome, descrição e imagem do produto correspondente em
  formato HTML."""
  return gera_html_elem_IMP.bloco_de_produto()
