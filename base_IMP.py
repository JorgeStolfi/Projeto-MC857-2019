#!/usr/bin/python3

#Guilherme Luis Domingues (guilhermeluisdomingues)
#155619
#Ultima Atualizacao: 20/08

# Funcao para criar e executar queries

# import mysql.connector as mariadb

def conecta():
  print ("Database conectada")

def executa_query(query):
  """Devolve o resultado da query executada. Se não houver algo que satisfaz essa busca, devolve {None}."""
  print ("query: " + query)