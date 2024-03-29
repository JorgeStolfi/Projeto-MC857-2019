#! /usr/bin/python3

# Interfaces usadas por este script:
import sys
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

import comando_finalizar_compra
import base_sql
import tabelas
import usuario
import produto
import sessao
import compra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ses1 = sessao.busca_por_identificador("S-00000001")

args1 = {'id_compra': 'C-00000001'}

html = comando_finalizar_compra.processa(ses1, args1)
html = html + "\n"

sys.stdout.buffer.write(html.encode('utf-8'))

cpr = compra.busca_por_identificador('C-00000001')
status = compra.obtem_status(cpr)

assert status == 'pagando'
