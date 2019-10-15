#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_menu_ver_todas_as_compras
import base_sql
import tabelas
import usuario
import sessao
import compra
from utils_testes import erro_prog, mostra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

ses1 = sessao.busca_por_identificador("S-00000001")
usr1 = usuario.busca_por_identificador("U-00000001")

args1 = { 'id_usuario': "U-00000001"}
userTest = comando_menu_ver_todas_as_compras.processa(ses1, args1)

if( userTest == usr1):
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
