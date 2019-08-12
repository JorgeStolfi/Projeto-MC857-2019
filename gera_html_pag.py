#! /usr/bin/python3
# Last edited on 2019-08-12 18:31:25 by stolfilocal

# Interface do módulo {gera_html_pag}.
# As funções deste módulo retornam cadeias de caracteres que são 
# páginas completas em HTML5.

# Interfaces importadas por esta interface:

# Implementaçao deste módulo:
import gera_html_pag_IMP


# Funções exportadas por este módulo:

def entrada():
  """Retorna a página de entrada do projeto."""
  return gera_html_pag_IMP.entrada()
