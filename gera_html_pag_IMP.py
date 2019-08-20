#! /usr/bin/python3
# Last edited on 2019-08-20 01:36:51 by stolfilocal

# Implementação do módulo {gera_html_pag}.

# Interfaces importadas por este módulo:
import gera_html_elem, gera_html_form, gera_html_botao
from utils import page_loader

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone

def entrada():
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto = "<hr/><i>DATA CORRENTE</i><br/><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  
  cor_texto = "#000488"
  cor_fundo = "#fff844"
  conteudo = gera_html_elem.bloco_texto(texto,"Courier","18px","5px","center",cor_texto,cor_fundo)
  return generica(conteudo)
  
def generica(conteudo):
  cabe = gera_html_elem.cabecalho("Projeto MC857A 2019-2s")
  menu = gera_html_elem.menu_geral()
  roda = gera_html_elem.rodape()
  return cabe + menu + conteudo + roda

def cadastrar(conteudo):
  conteudo_cadastro = gera_html_form.cadastrar_usuario()
  pagina = generica(conteudo_cadastro) 
  return pagina
  
def produto(prod):
  cabe = gera_html_elem.cabecalho("PRODUTO: ")
  menu = gera_html_elem.menu_geral()
  roda = gera_html_elem.rodape()
  return cabe + menu + roda
  
def login():
  cabecalho = gera_html_elem.cabecalho("Bilbo's Store")
  formulario = formulario_login()
  rodape = gera_html_elem.rodape()
  return cabecalho + formulario + rodape

def formulario_login():
  return page_loader.load_page('login')

def produtos(lista):
  todos_prods = []
  for prod in lista:
      todos_prods = todos_prods + gera_html_elem.bloco_de_produto(prod)
  return generica(todos_prods)
