#!/usr/bin/python3

# Implementação do módulo {base}

import mysql
# import mysql_bobo as mysql  # linha para teste

class Base_IMP:

  def __init__(self,con):
    self.conexao = con

  def executa_comando(self,cmd):
      try:
        cursor = self.conexao.cursor()
        resultado = cursor.execute(cmd)
        cursor.close()
        return resultado
      except mysql.Error as error:
        return None
  
  def indice_inserido(self):
      try:
        cursor = self.conexao.cursor(buffered=True)
        """Não há nome ainda para a base de sessões."""
        last_inserted_query = """SELECT MAX(ind) FROM compras,produto,usuarios"""
        resultado = cursor.execute(last_inserted_query)
        return resultado
      except mysql.Error as error:
        return None

def conecta(dir, uid, senha):
  conexao = mysql.connector.connect(user=uid, password=senha, database=(dir + "/mc857"))
  base = Base_IMP(conexao)
  return base

def identificador_de_indice(let,ind):
  return "%s-%08d" % (let,ind)

def indice_de_identificador(let,id):
  assert id.len() == 10 and id[0:1] == let and id[1:1] == "-"
  ind = int(id[3:])
  return ind
