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

def bloco_de_produto(produto):
    bloco_final =  """ <img src="placeholder.jpg" alt="Produto teste" style="width:500px;height:600px;"> """ + bloco_texto("produto.nome" + ";\n" + "produto.desc", "Courier", "18px", "5px", "center", "#ff0000", "fff888")
    return bloco_final
