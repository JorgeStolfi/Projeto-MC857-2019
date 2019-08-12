#! /usr/bin/python3
# Last edited on 2019-08-12 18:44:14 by stolfilocal

# Implementação do módulo {gera_html_pag}.

# Interfaces importadas por este módulo:
import gera_html_elem

from datetime import datetime, timezone

def entrada():
  cor_texto = "#000488"
  cor_fundo = "#fff844"
  cor_bloco = "#ffd844"
  
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  blab = "<i>DATA CORRENTE</i><br/><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR"
  
  cabe = gera_html_elem.cabecalho("Projeto MC857A 2019-2s")
  menu = gera_html_elem.menu_geral()
  meio = gera_html_elem.bloco_texto(blab,"Courier","18px","5px","center",cor_texto,cor_fundo)
  roda = gera_html_elem.rodape()
  
  return cabe + menu + meio + roda
  
