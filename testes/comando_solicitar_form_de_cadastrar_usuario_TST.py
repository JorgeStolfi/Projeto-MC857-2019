#! /usr/bin/python3

# Interfaces usadas por este script:
import sys
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

import comando_solicitar_form_de_cadastrar_usuario
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
# !!! Preencher o {args} com dados do produto a comprar !!!
usu = usuario.cria({'Lucio S.', 'senhasecretadele', 'lucy@domain.com', '123.123.123.12',
                   'Rua Margarida 12','12345-123', '+55(19)1234-1234', '23.234.254-7'} )
args1 = { 'usuario': usu }
html = comando_solicitar_form_de_cadastrar_usuario.processa(ses1, args1)
html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
