#! /usr/bin/python3

# Interfaces usadas por este script:
import sys
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

import comando_solicitar_form_de_login
import base_sql
import tabelas
import usuario
import sessao

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ses1 = sessao.busca_por_identificador("S-00000001")
args1 = { 'coisa': True }

html = comando_solicitar_form_de_login.processa(ses1, args1)
html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
