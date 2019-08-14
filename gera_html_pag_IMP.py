#! /usr/bin/python3
# Last edited on 2019-08-13 00:28:38 by stolfilocal

# Implementação do módulo {gera_html_pag}.

# Interfaces importadas por este módulo:
import gera_html_elem

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
  textoCampoUsuario = "Usuário"
  textoCampoSenha = "Senha"
  textoBotaoLogin = "Entrar"
  metodoDeEnvio = "post"
  css = """form {
            margin:0 auto;
            width:300px
          }
          input {
            margin-bottom:3px;
            padding:10px;
            width: 100%;
            border:1px solid; #CCC
          }
          button {
            padding:10px;
          }
          label {
            cursor:pointer;
          }"""
  html = """<style type="text/css">%s</style>
            <form id='login-form' action="" method='%s'>
              <input type="text" placeholder="%s" required>
              <input type="password" placeholder="%s" required>
              <button type='submit'>%s</button>
            </form>""" \
            % (css, metodoDeEnvio, textoCampoUsuario, textoCampoSenha, textoBotaoLogin)
  return html
