#! /usr/bin/python3
# Last edited on 2019-08-19 23:30:22 by stolfilocal

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

def subm_comprar():
  texto = "COMPRAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

def subm_busca():
  texto = "BUSCAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)

def subm_cadastrar():
  texto = "CADASTRAR"
  cor_fundo = "#fff888"
  return subm_botao_simples(texto, cor_fundo)
