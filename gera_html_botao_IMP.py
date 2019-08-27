#! /usr/bin/python3

# Implementação do módulo {gera_html_botao}.

# Interfaces importadas por esta implementação:

# Implementação da interface:

def login():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  cor_fundo = "#fff888"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "  background-color:" + cor_fundo + ";\n" + \
    "  text-align: center;\n" + \
    "\">\n" + \
    "  <button\n" + \
    "    type=\"button\"\n" + \
    "    onclick=\"alert('" + "Login" + "')\"\n" + \
    "  >" + "Login Button" + "</button>\n" + \
    "</span>"

def logout():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  cor_fundo = "#fff888"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "  background-color:" + cor_fundo + ";\n" + \
    "  text-align: center;\n" + \
    "\">\n" + \
    "  <button\n" + \
    "    type=\"button\"\n" + \
    "    onclick=\"alert('" + "Logout" + "')\"\n" + \
    "  >" + "Logout Button" + "</button>\n" + \
    "</span>"

def teste_de_popup(texto):
  fam_fonte = "Courier"
  tam_fonte = "18px"
  cor_fundo = "#fff888"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "  background-color:" + cor_fundo + ";\n" + \
    "  text-align: center;\n" + \
    "\">\n" + \
    "  <button\n" + \
    "    type=\"button\"\n" + \
    "    onclick=\"alert('" + texto + "')\"\n" + \
    "  >" + texto + "</button>\n" + \
    "</span>"

def subm_botao_simples(texto, cor_fundo):
  return \
    "<span style=\"background-color:" + cor_fundo + ";text-align: center;\">\n" + \
    "  <input type=\"submit\" value=\"" + texto + "\">" + \
    "</span>"

def cadastrar():
  cor_fundo = "#fff888"
  texto = "CADASTRAR"
  return 
  "<form action=\" \" method=\"get\" style=\"background-color:" + cor_fundo + ";text-align: center;\">\n" + \
  "  <input type=\"submit\" value=\"" + texto + "\">" + \
  "</form>" 

def subm_comprar():
  texto = "COMPRAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

def subm_busca():
  texto = "BUSCAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

def subm_cadastrar(texto,fam_fonte,tam_fonte,pad,haling,cor_texto,cor_fundo):
  texto = "CADASTRAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

def subm_login(login,senha):
  texto = "ENTRAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

def subm_logout():
  texto = "SAIR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

