#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_menu_sair
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

resultado = comando_menu_sair.processa(ses1, args1)

# !!! Verificar se a sessão foi de fato fechada !!! 

f = open("comando_menu_sair", "w")
f.write((resultado + "\n").encode('utf-8'))
f.close()
