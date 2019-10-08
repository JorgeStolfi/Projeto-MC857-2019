#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_submit_finalizar_compra
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
# !!! Preencher o {args} com dados do formulario !!!
args1 = { 'coisa': True }

html = comando_submit_finalizar_compra.processa(ses1, args1)
html = html + "\n"

sys.stdout.buffer.write(html.encode('utf-8'))

# !!! Verificar se a compra foi fechada, etc. !!!
