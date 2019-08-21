#! /usr/bin/python3

# Last edited on 2019-08-20 01:32:22 by stolfilocal

# Implementação do módulo {gera_html_form}.

# Interfaces importadas por esta implementação:
import gera_html_elem, gera_html_botao

#Funções exportadas por este módulo:

def busca():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  cor_cinza = "#fff888"
  cor_fundo = "#fff888"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form action=\"search\" method=\"post\">\n" + \
    "    <span style=\"text-color:" + cor_cinza + ";text-align: left;\">\n" + \
    "      <input type =\"text\" name=\"search_arg\" placeholder=\"Buscar o que?\">\n" + \
    "    </span>\n" + \
    "    " + gera_html_botao.subm_busca() + "\n" + \
    "  </form>\n" + \
    "</span>"

def comprar(id_produto,qtd_produto,fam_fonte,tam_fonte,cor_texto,cor_fundo):
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form action=\"buy\" method=\"post\">\n" + \
    "    <input type =\"hidden\" name=\"id_produto\" value=\"" + id_produto + "\">\n" + \
    "    <input type =\"hidden\" name=\"qtd_produto\" value=\"" + qtd_produto + "\">\n" + \
    "    " + gera_html_botao.subm_comprar() + "\n" + \
    "  </form>\n" + \
    "</span>"

def cadastrar_usuario():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  cor_cinza = "#fff888"
  cor_fundo = "#fff888"
  padding = "5px"
  halign = "center"

  altura="auto"
  largura="400px"
  margem="64px"
  acolchoamento="32px"
  margem_entradas="8px"

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
  
  button = gera_html_botao.subm_cadastrar("Cadastrar", fam_fonte, tam_fonte, padding, halign, cor_cinza, cor_fundo)
  
  html = """<body class="body">
            <style>%s</style>
            <form id='login-form' class="formulario" action="" method='post'>
                <div class="container">
                    <label for="username"><b>Nome</b></label>
                    <input type="text" class="entrada" placeholder="Entre com o nome" name="username" required>
                </div>
                <div class="container">
                    <label for="email"><b>E-mail</b></label>
                    <input type="text" class="entrada" placeholder="Entre com o e-mail" name="email" required>
                </div>
                <div class="container">
                    <label for="cpf"><b>CPF</b></label>
                    <input type="text" class="entrada" placeholder="Entre com o CPF" name="cpf" required>
                </div>
                <div class="container">
                    <label for="telefone"><b>Telefone</b></label>
                    <input type="text" class="entrada" placeholder="Entre com o telefone" name="telefone" required>
                </div>
                <div class="container">
                    <label for="senha" class="texto"><b>Senha</b></label>
                    <input type="password" class="entrada" placeholder="Entre com a senha" name="senha" required>
                </div>
                <div class="container">
                  %s
                </div>
            </form>
        </body>""" %(css,button)

  return html

  # return \
  #     "<span style=\"\n" + \
  #   "  display: inline-block;\n" + \
  #   "  font-family:" + fam_fonte + ";\n" + \
  #   "  font-size:" + tam_fonte + ";\n" + \
  #   "  padding: " + padding + ";\n" + \
  #   "\">\n" + \
  #   "  <form action=\"cadastrar\" method=\"post\">" + \
  #   "    <div>" + \
  #   "	<label>Nome:</label>" + \
  #   "	<input type=\"text\" id=\"nome\" name=\"nome\"/>" + \
  #   "    </div>" + \
  #   "    <div>" + \
  #   "	<label>E-mail:</label>" + \
  #   "	<input type=\"email\" id=\"email\" name=\"email\"/>" + \
  #   "    </div>" + \
  #   "    <div>" + \
  #   "	<label>CPF:</label>" + \
  #   "	<input type=\"text\" id=\"cpf\" name=\"cpf\"/>" + \
  #   "    </div>" + \
  #   "    <div>" + \
  #   "	<label>Telefone:</label>" + \
  #   "	<input type=\"text\" id=\"telefone\" name=\"telefone\"/>" + \
  #   "    </div>" + \
  #   "    <div>" + \
  #   "	<label>Senha:</label>" + \
  #   "	<input type=\"text\" id=\"senha\" name=\"senha\"/>" + \
  #   "    </div>" + gera_html_botao.subm_cadastrar("Cadastrar", fam_fonte, tam_fonte, padding, halign, cor_cinza, cor_fundo) + \
  #   "  </form>\n" + \
  #   "</span>"
    
