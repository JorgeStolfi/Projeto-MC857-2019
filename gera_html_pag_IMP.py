#! /usr/bin/python3

# Implementação do módulo {gera_html_pag}.

# Interfaces importadas por este módulo:
import gera_html_elem, gera_html_form, gera_html_botao

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

def produto(prod):
  cabe = gera_html_elem.cabecalho("PRODUTO: ")
  menu = gera_html_elem.menu_geral()
  roda = gera_html_elem.rodape()
  return cabe + menu + roda

def produtos(lista):
  todos_prods = []
  for prod in lista:
      todos_prods = todos_prods + gera_html_elem.bloco_de_produto(prod)
  return generica(todos_prods)

def login():
  cabecalho = gera_html_elem.cabecalho("Bilbo's Store")
  formulario = gera_html_elem.formulario_login(altura="auto",
                                             largura="400px",
                                             margem="64px",
                                             acolchoamento="32px",
                                             margem_entradas="8px")
  rodape = gera_html_elem.rodape()
  return cabecalho + formulario + rodape

def cadastrar_usuario(conteudo):
  conteudo_cadastro = gera_html_form.cadastrar_usuario()
  pagina = generica(conteudo_cadastro) 
  return pagina
