#! /usr/bin/python3

import sys
import base; from base import Base

bas = base.conecta("MC857",None,None)

def testa_ex(cmd):
  sys.stderr.write("comando: " + cmd + "\n")
  res = bas.executa_comando(cmd)
  sys.stderr.write("resultado: " + str(res) + "\n")
  
testa_ex(
  "CREATE TABLE testabela"
  "  ( indice int(8) NOT NULL AUTO_INCREMENT,"
  "    nome varchar(40),"
  "    cpf char(14),"
  "    cep char(9),"
  "    PRIMARY KEY ( indice )"
  "  )"
)
testa_ex("INSERT INTO testabela (nome,cpf,cep) VALUES (zeca, 123.456.789-10, 13083-851)")
testa_ex("INSERT INTO testabela (nome,cpf,cep) VALUES (juca, 987.654,321-00, 13083-851)")
testa_ex("INSERT INTO testabela (nome,cpf,cep) VALUES (caco, 111.222.333-44, 13083-851)")
testa_ex("UPDATE testabela SET cep = 13083-705 WHERE nome = juca")
testa_ex("SELECT nome,cpf FROM testabela WHERE cep = 13083-851")

testa_ex("INSERT INTO testabela (nome,cpf,cep) VALUES (sara, 123.321.123-45, 13083-852)")
sys.stderr.write("indice inserido: " + str(bas.indice_inserido()) + "\n")
