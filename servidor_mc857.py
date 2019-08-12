#! /usr/bin/python3
# Last edited on 2019-08-12 18:43:31 by stolfilocal

# Script principal.
# Este script é executado pelo servidor em resposta a 
# um comando HTTP GET ou POST enviados por um usuário.
# Deve escrever no standard output uma página HTML5
# com a resposta aproriada.

# Interfaces usadas por este script:
import gera_html_pag
import sys

# Comandos:
pagina = gera_html_pag.entrada()
sys.stdout.buffer.write(pagina.encode('utf-8'))
