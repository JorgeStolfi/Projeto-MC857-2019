#! /usr/bin/python3

# Implementação do módulo {gera_html_form}.

# Interfaces importadas por esta implementação:
import gera_html_elem, gera_html_botao

#Funções exportadas por este módulo:

def busca():
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
    "  <form action=\"search\" method=\"post\">\n" + \
    "    <span style=\"text-color:" + cor_cinza + ";text-align: left;\">\n" + \
    "      <input type =\"text\" name=\"search_arg\" placeholder=\"Buscar o que?\">\n" + \
    "    </span>\n" + \
    "    " + gera_html_botao.subm_busca() + "\n" + \
    "  </form>\n" + \
    "</span>"

def comprar(id_produto,qtd_produto):
  fam_fonte = "Courier"
  tam_fonte = "18px"
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
  return \
      "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form action=\"cadastrar\" method=\"post\">" + \
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
    "    </div>" + gera_html_botao.subm_cadastrar() + \
    "  </form>\n" + \
    "</span>"

def login():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  return \
      "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form action=\"login\" method=\"post\">" + \
    "   <label>E-mail:</label>" + \
    "	<input type=\"email\" id=\"email\" name=\"email\"/>" + \
    "   </div>" + \
    "   <label>Senha:</label>" + \
    "	<input type=\"text\" id=\"senha\" name=\"senha\"/>" + \
    "   </div>" + gera_html_botao.login() + \
    "  </form>\n" + \
    "</span>"

    
