#! /usr/bin/python3

# Interfaces usadas por este script:
import sys
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

import comando_fazer_logout
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

assert sessao.aberta(ses1)
pag, ses_nova = comando_fazer_logout.processa(ses1, {})

assert not sessao.aberta(ses1)
assert pag == gera_html_pag.principal(None, ["Mensagem de teste", "Outra mensagem",])
assert ses_nova == None
