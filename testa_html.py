#! /usr/bin/python3
# Last edited on 2019-08-12 20:18:22 by stolfilocal

# Este programa pode ser usado para testar funções que
# escrevem páginas ou fragmentos HTML5.

# Interfaces usadas por este script:
import gera_html_impl, gera_html_pag
import sys

# Comandos:
pagina = gera_html_pag.entrada()
sys.stdout.buffer.write(pagina.encode('utf-8'))
