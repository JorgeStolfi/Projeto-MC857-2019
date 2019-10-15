#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_menu_sair
import base_sql
import tabelas
import sessao
import gera_html_pag

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res is None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()
ses1 = sessao.busca_por_identificador("S-00000001")

resultado = comando_menu_sair.processa(ses1, {})

assert not sessao.aberta(ses1)
assert resultado == gera_html_pag.principal(ses1)
