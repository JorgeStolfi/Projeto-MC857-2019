#! /usr/bin/python3

# Last edited on 2019-08-19 23:53:13 by stolfilocal

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
  return \
      "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form action=\"insert\" method=\"post\">\n" + \
    "    " + gera_html_botao.subm_cadastrar() + "\n" + \
    "  </form>\n" + \
    "</span>"
    
