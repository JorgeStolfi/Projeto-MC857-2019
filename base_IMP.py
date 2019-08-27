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


def conecta():
  conexao = mysql.connect(user=uid, password=senha, database=(dir + "/mc857"))
  base = Base_IMP(conexao)
  return base

def identificador_de_indice(let,ind):
  return "%s-%08d" % (let,ind)

def indice_de_identificador(let,id):
  assert id.len() == 10 and id[0:1] == let and id[1:1] == "-"
  ind = int(id[3:])
  return ind
