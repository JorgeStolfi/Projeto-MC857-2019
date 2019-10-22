# Interfaces usadas por este script:
import sys

import comando_fazer_login
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

ses1 = None
# !!! Preencher o {args} com dados do produto a comprar !!!
args1 = { 'email': 'primeiro@gmail.com', 'senha' : '123456789'}

pag, ses_nova = comando_fazer_login.processa(ses1, args1)
pag = pag + "\n"
sys.stdout.buffer.write(pag.encode('utf-8'))

sys.stderr.write("ses_nova = " + str(ses_nova) + "\n")

