#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

sys.path.insert(1, "/home/cc2016/ra173711/mc857/data/173711")

import comando_submit_comprar_produto
import base_sql
import tabelas
import usuario
import sessao
import compra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ses1 = sessao.busca_por_identificador("S-00000001")
args1 = {"id_produto": "P-00000001", "quantidade": "3"}

html = comando_submit_comprar_produto.processa(ses1, args1)
html = html + "\n"

sys.stdout.buffer.write(html.encode("utf-8"))
