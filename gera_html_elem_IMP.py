#! /usr/bin/python3

# Last edited on 2019-08-19 23:47:25 by stolfilocal

# Implementação do módulo {gera_html_elem}.

# Interfaces importadas por esta implementação:
from datetime import datetime, timezone
import gera_html_form
import gera_html_botao

#Funções exportadas por este módulo:

def cabecalho(title):
  return \
    "<!doctype html>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + title + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"bacground-color:'#eeeeee'\">\n" + \
    "<h1>" + title + "</h1>"

def rodape():
  nowraw = datetime.now(timezone.utc)
  nowfmt = nowraw.strftime("%Y-%m-%d %H:%M:%S %z")
  return \
    "<small><p>\n" + \
    "Page created on " + nowfmt + "\n" + \
    "</p></small>\n" + \
    "</body>\n" + \
    "</html>\n"

def menu_geral():
  return \
    "<nav>\n" + \
    "  " + gera_html_form.busca() + "\n" + \
    "  " + gera_html_botao.teste_de_popup("Clique Aqui") + "\n" + \
    "  " + gera_html_botao.teste_de_popup("Não, Clique Aqui!") + "\n" + \
    "  " + gera_html_botao.teste_de_popup("Não Clique Aqui") + "\n" + \
    "</nav>"

def bloco_texto(texto,fam_fonte,tam_fonte,pad,halign,cor_texto,cor_fundo):
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    ( "  font-family:" + fam_fonte + ";\n" if fam_fonte != None else "") + \
    ( "  font-size:" + tam_fonte + ";\n" if tam_fonte != None else "") + \
    ( "  padding:" + pad + ";\n" if pad != None else "") + \
    ( "  background-color:" + cor_fundo + ";\n" if cor_fundo != None else "") + \
    ( "  text-color:" + cor_texto + ";\n" if cor_texto != None else "") + \
    ( "  text-align:" + halign + ";\n" if halign != None else "") + \
    "\">" + texto + "</span>"

def bloco_de_produto(prod):
    bloco_final =  """ <img src="placeholder.jpg" alt="Produto teste" style="width:500px;height:600px;"> """ + bloco_texto("prod.nome" + ";\n" + "prod.desc", "Courier", "18px", "5px", "center", "#ff0000", "fff888")
    return bloco_final

def formulario_login(altura, largura, margem, acolchoamento, margem_entradas):
  """ Retorna o html para o formulário de login base, com campos de usuário, senha e lembrar da sessão. """
  css = """.formulario {
              border: 3px solid #f1f1f1;
              padding: """ + acolchoamento + """;
              width: """ + largura + """;
              height: """ + altura + """
              align-self: center;
              position: center;
              margin: """ + margem + """ auto;
          }
          .entrada {
              width: 100%;
              padding: 12px 20px;
              margin: """ + margem_entradas + """ 0;
              display: inline-block;
              border: 1px solid #ccc;
              box-sizing: border-box;
          }
          .botao {
              background-color: #4CAF50;
              color: white;
              padding: 14px 20px;
              margin: 8px 0;
              border: none;
              cursor: pointer;
              width: 100%;
          }
          .botao:hover {
              opacity: 0.8;
          }
          .texto {
              cursor:pointer;
          }
          .container {
              padding: 4px;
          }
          .link {
              float: right;
              padding-top: 4px;
          }"""
  html = """<body class="body">
            <style>%s</style>
            <form id='login-form' class="formulario" action="" method='post'>
                <div class="container">
                    <label for="username"><b>Usuário/E-mail</b></label>
                    <input type="text" class="entrada" placeholder="Entre com o usuário ou e-mail" name="username" required>
                </div>
                <div class="container">
                    <label for="senha" class="texto"><b>Senha</b></label>
                    <input type="password" class="entrada" placeholder="Entre com a senha" name="senha" required>
                </div>
                <div class="container">
                    <label class="texto">
                        <input type="checkbox" checked="checked" name="lembrar">Lembrar de mim</input>
                    </label>
                    <button type='submit' class="botao">Entrar</button>
                    <span class="link"><a href="#">Esqueceu a senha?</a></span>
                </div>
            </form>
        </body>""" % css

  return html