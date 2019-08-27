#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import gera_html_form
import sys

# Comandos:
# html = gera_html_pag.entrada()

html= gera_html_form.busca()

html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
