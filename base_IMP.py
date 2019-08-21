#!/usr/bin/python3

#Guilherme Luis Domingues (guilhermeluisdomingues)
#155619
#Ultima Atualizacao: 20/08

# Funcao para criar e executar queries

import mysql.connector as mariadb

def conecta():
  mariadb_connection = mariadb.connect(user='usuario', password='senha',
  database='banco_de_dados')
  cursor = mariadb_connection.cursor()
  return cursor

def executa_query(query):
    try:
      cursor = conecta()
      resultado = cursor.execute(query))
      cursor.close()
      return resultado
    except mariadb.Error as error:
      return None
