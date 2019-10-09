#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_submit_excluir_item_de_compra
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
sys.stderr.write("Objetos criados...\n")

sys.stderr.write("Buscando sessao por identificador...\n")
ses1 = sessao.busca_por_identificador("S-00000001")
sys.stderr.write("Sessao: " + str(ses1) + "\n")

# !!! Preencher o {args} com dados do formulario !!!
args1 = { 'id_produto': "P-00000000", 'id_compra': "C-00000000"}
sys.stderr.write("args1: " + str(args1) + "\n")

html = comando_submit_excluir_item_de_compra.processa(ses1, args1)
html = html + "\n"

sys.stdout.buffer.write(html.encode('utf-8'))