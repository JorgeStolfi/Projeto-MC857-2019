#! /usr/bin/python3
# Last edited on 2019-08-19 23:52:35 by stolfilocal

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

def comprar(id_produto,qtd_produto,fam_fonte,tam_fonte,cor_texto,cor_fundo):
  """Retorna um botão que é um fragmento HTML com o texto 'COMPRAR'.

  Os parâmetros {id_produto} e {qtd_produto} especificam o id do produto
  da qual se quer comprar e a quantidade de produtos desejados, respectivamente.

  Os parâmetros {fam_fonte} e {tam_fonte} especificam a família e o
  tamanho do fonte a usar (por exemplo 'Helvetica','18px').

  Os parâmetros {cor_texto} e {cor_fundo} devem ser cores aceitáveis no
  CSS (por exemplo, '#ff8800')."""
  return gera_html_form_IMP.comprar(id_produto,qtd_produto,fam_fonte,tam_fonte,cor_texto,cor_fundo)

def login(login,senha):
  """Retorna o botão para a submissão de login"""
  return gera_html_form_IMP.login()

def cadastrar_usuario(texto,fam_fonte,tam_fonte,pad,haling,cor_texto,cor_fundo):
    """Retorna uma string que é um fragmento HTML consistindo do {texto} dado, que pode conter tags de HTML (como '<b>', <i>) de um botão de submeter cadastro.

    Caso nenhum parâmetro além do texto seja fornecido, os valores de estilo
    serão default.

    Os parâmetros {fam_fonte} e {tam_fonte} especificam a família e o
    tamanho do fonte a usar (por exemplo 'Helvetica','18px').

    O parâmetro {pad}, especifica a largura do espaço extra ('padding') em
    volta do texto como um todo.

    O parâmetro {halign} especifica o alinhamento das linhas do texto;
    pode ser 'left', 'center', ou 'right'.

    Os parâmetros {cor_texto} e {cor_fundo} devem ser cores aceitáveis no
    CSS (por exemplo, '#ff8800').
    """
    return gera_html_form_IMP.cadastrar_usuario(texto,fam_fonte,tam_fonte,pad,haling,cor_texto,cor_fundo);
