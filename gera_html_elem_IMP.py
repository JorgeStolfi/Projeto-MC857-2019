#! /usr/bin/python3

# Last edited on 2019-08-13 20:15:11 by humanolaranja

# Implementação do módulo {gera_html_elem}.

# Interfaces importadas por esta implementação:
from datetime import datetime, timezone

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
    "  " + botao_de_busca() + "\n" + \
    "  " + botao_de_popup("Clique Aqui") + "\n" + \
    "  " + botao_de_popup("Não, Clique Aqui!") + "\n" + \
    "  " + botao_de_popup("Não Clique Aqui") + "\n" + \
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

# Funções internas deste módulo:


def botao_de_popup(texto): 
  """Função interna: retorna HTML de um botão do menu 
  que mostra um popup com o {texto} dado."""
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
 
def botao_de_busca(): 
  """Função interna: retorna HTML de um botão ed busca com o campo a buscar."""
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
    "    <span style=\"background-color:" + cor_fundo + ";text-align: center;\">\n" + \
    "      <input type=\"submit\" value=\"Buscar\">" + \
    "    </span>\n" + \
    "  </form>\n" + \
    "</span>"

def bloco_de_produto(produto):
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    ( "  font-family:" + "Courier" + ";\n") + \
    ( "  font-size:" + "18px" + ";\n") + \
    ( "  padding:" + "5px" + ";\n") + \
    ( "  background-color:" + "#fff888" + ";\n") + \
    ( "  text-color:" + "##ff0000" + ";\n") + \
    ( "  text-align:" + "center" + ";\n") + \
    "\">" + produto.nome + ";\n" + produto.desc + "</span>"
