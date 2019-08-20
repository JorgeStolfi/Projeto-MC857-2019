#! /usr/bin/python3
# Last edited on 2019-08-19 23:47:57 by stolfilocal

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

def cadastrar():
  """Retorna o botão para cadastro de um novo produto"""
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
  return gera_html_botao_IMP.subm_login(login,senha)

def subm_cadastrar(texto,fam_fonte,tam_fonte,pad,haling,cor_texto,cor_fundo):
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
    return gera_html_botao_IMP.subm_cadastrar(texto,fam_fonte,tam_fonte,pad,haling,cor_texto,cor_fundo);

def subm_busca():
  """Retorna HTML do botão <submit> para uso em formulario de busca."""
  return gera_html_botao_IMP.subm_busca()
