#! /usr/bin/python3

import sys
import base_sql

base_sql.conecta("DB/MC857",None,None)
nome_tb = "testabela"

sys.stderr.write("testando CREATE TABLE:\n")
res = base_sql.executa_comando_CREATE_TABLE (
  nome_tb,
  "indice integer PRIMARY KEY," + \
  "nome varchar(40) NOT NULL," + \
  "cpf char(14) NOT NULL," + \
  "cep char(9) NOT NULL," + \
  "peso fixed(8,2)," + \
  "pernas int(4)"
)
sys.stderr.write("resultado: " + str(res) + "\n\n")

sys.stderr.write("testando CLEAR TABLE:\n")
res = base_sql.executa_comando_CLEAR_TABLE(nome_tb)
sys.stderr.write("resultado: " + str(res) + "\n\n")

def testa_insert(atrs):
  sys.stderr.write("testando INSERT:\n")
  res = base_sql.executa_comando_INSERT(nome_tb,atrs)
  sys.stderr.write("resultado: " + str(res) + "\n\n")
  
testa_insert({ 'nome': 'zeca', 'cpf': '123.456.789-10', 'cep':  '13083-851', 'peso':  30.22, 'pernas': 3 })
testa_insert({ 'nome': 'juca', 'cpf': '987.654.321-00', 'cep':  '13083-851', 'peso': 120.01, 'pernas': 2 })
testa_insert({ 'nome': 'caco', 'cpf': '111.222.333-44', 'cep':  '13083-851', 'peso':  12.10, 'pernas': 4 })

sys.stderr.write("testando UPDATE:\n")
res = base_sql.executa_comando_UPDATE(nome_tb, "nome = 'juca'", { 'cep': '13083-705' })
sys.stderr.write("resultado: " + str(res) + "\n\n")

sys.stderr.write("testando SELECT:\n")
res = base_sql.executa_comando_SELECT(nome_tb,"cep = '13083-851'", ('nome', 'cpf' ))
sys.stderr.write("resultado: " + str(res) + "\n\n")

sys.stderr.write("testando DELETE:\n")
res = base_sql.executa_comando_DELETE(nome_tb, 'nome', 'juca')
sys.stderr.write("resultado: " + str(res) + "\n\n")

sys.stderr.write("testando SELECT:\n")
res = base_sql.executa_comando_SELECT(nome_tb,"cep ='13083-851'", ('nome', 'cpf' ))
sys.stderr.write("resultado: " + str(res) + "\n\n")

testa_insert({ 'nome': 'sara', 'cpf': '123.321.123-45', 'cep': '13083-852', 'peso':  45.99, 'pernas': 3 })

sys.stderr.write("testando SELECT:\n")
res = base_sql.executa_comando_SELECT(nome_tb,"pernas = 3", ('nome', 'cpf', 'peso', 'pernas' ))
sys.stderr.write("resultado: " + str(res) + "\n\n")

