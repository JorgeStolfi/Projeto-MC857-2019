# Implementação do módulo {gera_html_form}.

# Interfaces importadas por esta implementação:
import gera_html_elem, gera_html_botao

#Funções exportadas por este módulo:

def buscar_produtos():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  cor_cinza = "#fff888"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">\n" + \
    "    <span style=\"text-color:" + cor_cinza + ";text-align: left;\">\n" + \
    "      <input type =\"text\" name=\"condicao\" id=\"condicao\" placeholder=\"Buscar o que?\">\n" + \
    "    </span>\n" + \
    "    " + gera_html_botao.submit_buscar_produtos() + "\n" + \
    "  </form>\n" + \
    "</span>"

def ver_produto(id_produto, qtd_produto):
  fam_fonte = "Courier"
  tam_fonte = "18px"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">\n" + \
    "    <input type =\"hidden\" name=\"id_produto\" id=\"id_produto\" value=\"" + id_produto + "\">\n" + \
    "    <input type =\"hidden\" name=\"quantidade\" id=\"quantidade\" value=\"" + str(qtd_produto) + "\">\n" + \
    "    " + gera_html_botao.submit_ver_produto() + "\n" + \
    "  </form>\n" + \
    "</span>"

def comprar_produto(id_produto, qtd_produto):
  fam_fonte = "Courier"
  tam_fonte = "18px"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">\n" + \
    "    <input type =\"hidden\" name=\"id_produto\" id=\"id_produto\" value=\"" + id_produto + "\">\n" + \
    "    <input name=\"quantidade\" id=\"quantidade\" value=\"" + str(qtd_produto) + "\">\n" + \
    "    " + gera_html_botao.submit_comprar_produto() + "\n" + \
    "  </form>\n" + \
    "</span>"

def cadastrar_usuario():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  return \
      "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">" + \
    "    <div>" + \
    "	<label>Nome: <span style=\"color:red;\"></span></label>" + \
    "	<input type=\"text\" id=\"nome\" name=\"nome\"/>" + \
    "    </div>" + \
    "    <div>" + \
    "	<label>E-mail: <span style=\"color:red;\"></span></label>" + \
    "	<input type=\"email\" id=\"email\" name=\"email\"/>" + \
    "    </div>" + \
    "    <div>" + \
    "	<label>CPF:: <span style=\"color:red;\"></span></label>" + \
    "	<input type=\"text\" id=\"cpf\" name=\"cpf\"/>" + \
    "    </div>" + \
    "    <div>" + \
    "	<label>Telefone:</label>" + \
    "	<input type=\"text\" id=\"telefone\" name=\"telefone\"/>" + \
    "    </div>" + \
    "    <div>" + \
    "	<label>Senha: <span style=\"color:red;\"></span></label>" + \
    "	<input type=\"text\" id=\"senha\" name=\"senha\"/>" + \
    "    </div>" + gera_html_botao.submit_cadastrar_usuario() + \
    "  </form>\n" + \
    "</span>"
    
def mostra_compra(cpr):
   return gera_html_elem.bloco_texto("!!! IMPLEMENTAR !!!", None, "Courier", "18px", "bold", "0px", "left", None, None)

def entrar():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  return \
      "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">" + \
    "   <label>E-mail:</label>" + \
    "	<input type=\"email\" id=\"email\" name=\"email\"/>" + \
    "   </div>" + \
    "   <label>Senha:</label>" + \
    "	<input type=\"text\" id=\"senha\" name=\"senha\"/>" + \
    "   </div>" + gera_html_botao.submit_entrar() + \
    "  </form>\n" + \
    "</span>"

def formulario_entrar(altura, largura, margem, acolchoamento, margem_entradas):
  """ Retorna o html para o formulário que , com campos de usuário, senha e lembrar da sessão. """
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
            <form id='login-form' class="formulario" method='post'>
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
                    <button type='submit' formacion="submit_entrar" class="botao">Entrar</button>
                    <span class="link"><a href="#">Esqueceu a senha?</a></span>
                </div>
            </form>
        </body>""" % css

  return html


def informacao_usuario(usr):
    """ A função recebe o parâmetro {usr}, da classe {ObjUsuario}, e recupera
    a partir dele nome, email, CPF, endereco, CEP, telefone do usuario
    correspondente em formato HTML."""
    info_final = """ <h1> """ + usr.nome + """ </h1> <br> """ + usr.cpf + """ <br> """ + usr.email + """ <br> """ + usr.endereco + """ <br> """ + usr.cep + """ <br> """ + + usr.telefone + """ <br> """
    return info_final
