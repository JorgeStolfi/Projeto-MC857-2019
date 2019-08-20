#! /usr/bin/python3
# Last edited on 2019-08-19 23:51:45 by stolfilocal

# Este programa pode ser usado para testar funções que
# escrevem páginas ou fragmentos HTML5.

# Interfaces usadas por este script:
import gera_html_elem, gera_html_botao, gera_html_form, gera_html_pag
import sys

# Comandos:
# html = gera_html_pag.entrada()

html= gera_html_form.busca()

html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
