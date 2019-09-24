#! /usr/bin/python3

# Este programa executável limpa todas as tabelas da base de dados e cria 
# pelo menos três objetos de cada classe nas tabela correspondente.

import base_sql
import tabelas
import sys

def principal():
  sys.stderr.write("Conectando com base de dados...\n")
  base_sql.conecta("DB/MC857",None,None)

  sys.stderr.write("cria_base_de_teste.py: limpando e criando objetos para testes...\n")
  tabelas.cria_todos_os_testes()

  sys.stderr.write("cria_base_de_teste.py: feito.\n")

principal()
