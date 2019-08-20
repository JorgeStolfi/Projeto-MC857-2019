#! /usr/bin/python3
# Last edited on 2019-08-20 01:36:51 by stolfilocal

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

def cadastrar_usuario(conteudo):
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
  css = """body {
              font-family: Arial, Helvetica, sans-serif;
              margin: auto;
          }
          form {
              border: 3px solid #f1f1f1;
              padding: 16px;
              width: 640px;
              align-self: center;
              position: center;
              margin: 64px auto;
          }
          input[type=text], input[type=password] {
              width: 100%;
              padding: 12px 20px;
              margin: 8px 0;
              display: inline-block;
              border: 1px solid #ccc;
              box-sizing: border-box;
          }
          button {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 100%;
          }
          button:hover {
              opacity: 0.8;
          }
          label {
              cursor:pointer;
          }
          .container {
              padding: 16px;
          }
          span.psw {
              float: right;
              padding-top: 4px;
          }"""
  html = """<body class="body">
            <style>%s</style>
            <form id='login-form' action="" method='post'>
                <div class="container">
                    <label for="username"><b>Usuário/E-mail</b></label>
                    <input type="text" placeholder="Entre com o usuário ou e-mail" name="username" required>
                </div>
                <div class="container">
                    <label for="senha"><b>Senha</b></label>
                    <input type="password" placeholder="Entre com a senha" name="senha" required>
                </div>
                <div class="container">
                    <label>
                        <input type="checkbox" checked="checked" name="lembrar">Lembrar de mim</input>
                    </label>
                    <button type='submit'>Entrar</button>
                    <span class="psw"><a href="#">Esqueceu a senha?</a></span>
                </div>
            </form>
        </body>""" % css

  return html

def produtos(lista):
  todos_prods = []
  for prod in lista:
      todos_prods = todos_prods + gera_html_elem.bloco_de_produto(prod)
  return generica(todos_prods)
