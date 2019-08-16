#! /usr/bin/python3
# Last edited on 2019-08-13 01:58:03 by stolfilocal

# Interfaces do projeto usadas por este módulo:
import gera_html_pag, gera_html_elem

# Outras interfaces usadas por este módulo:
import json, sys, re

def comando_GET(dados):
  if dados['query'] == "":
    return gera_html_pag.entrada()
  else:
    return mostra_comando(dados)

def comando_POST(dados):
  return mostra_comando(dados)

def comando_HEAD(dados):
  return mostra_comando(dados)
  
def mostra_comando(dados):
  cor_fundo = "#fff844"
  dados_lin = json.dumps(dados,indent='&nbsp;&nbsp;',sort_keys=True,separators=(',<br/>',': '))
  dados_lin = re.sub(r'\[','[<br/>',dados_lin);
  dados_lin = re.sub(r'\{','{<br/>',dados_lin);
  tipo = dados['command']
  texto = "<hr/>Metodo %s chamado com dados:<br/>%s<hr/>" % (tipo, dados_lin);
  conteudo = gera_html_elem.bloco_texto(texto,"Courier","18px","5px","left",None,cor_fundo)
  pagina = gera_html_pag.generica(conteudo)
  return pagina
