#! /usr/bin/python3
# Last edited on 2019-08-19 23:47:22 by stolfilocal

# Implementação do módulo {gera_html_pag}.

# Interfaces importadas por este módulo:
import gera_html_elem, gera_html_form, gera_html_botao
from utils import page_loader

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone

def entrada():
  cor_texto = "#000488"
  cor_fundo = "#fff844"
  
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto = "<hr/><i>DATA CORRENTE</i><br/><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  
  conteudo = gera_html_elem.bloco_texto(texto,"Courier","18px","5px","center",cor_texto,cor_fundo)
  return generica(conteudo)
  
def generica(conteudo):
  cabe = gera_html_elem.cabecalho("Projeto MC857A 2019-2s")
  menu = gera_html_elem.menu_geral()
  roda = gera_html_elem.rodape()
  
  return cabe + menu + conteudo + roda

def cadastrar(conteudo):
  conteudo_cadastro = "  <form action=\"cadastrar\" method=\"post\">" + \
			"    <div>" + \
			"	<label>Nome:</label>" + \
			"	<input type=\"text\" id=\"nome\" name=\"nome\"/>" + \
			"    </div>" + \
			"    <div>" + \
			"	<label>E-mail:</label>" + \
			"	<input type=\"email\" id=\"email\" name=\"email\"/>" + \
			"    </div>" + \
			"    <div>" + \
			"	<label>CPF::</label>" + \
			"	<input type=\"text\" id=\"cpf\" name=\"cpf\"/>" + \
			"    </div>" + \
			"    <div>" + \
			"	<label>Telefone:</label>" + \
			"	<input type=\"text\" id=\"telefone\" name=\"telefone\"/>" + \
			"    </div>" + \
			"    <div>" + \
			"	<label>Senha:</label>" + \
			"	<input type=\"text\" id=\"senha\" name=\"senha\"/>" + \
			"    </div>" + gera_html_botao.subm_cadastrar("Cadastrar") + \
			"</form>"

  pagina = gera_html_pag.generica(conteudo_cadastro) 
	
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
      
  return gera_html_pag.generica(todos_prods)
