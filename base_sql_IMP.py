#!/usr/bin/python3

# Implementação do módulo {base}

# import mysql.connector as sql
import mysql_bobo as sql  # linha para teste

class Base_IMP:

  """Um objeto desta classe tem um atributo privado {conexao}
  que é o objeto retornado por {sql.connect(...)}.  
  Or métodos deste objeto permitem acessar a base no disco."""

  def __init__(self,con):
    self.conexao = con

  def executa_comando(self,cmd):
      try:
        cursor = self.conexao.cursor(buffered=True)
        # Este código supõe que o {cmd} é um "SELECT".  Falta tratar "INSERT", "UPDATE".
        iterador = cursor.execute(cmd)
        resultado = cursor.fetchall() # Converte o iterador em lista.
        # Por via das dúvidas, se o comando for "INSERT" ou "UPDATE":
        self.conexao.commit()
        cursor.close()
        return resultado
      except mysql.Error as error:
        return None
  
  def indice_inserido(self):
      return self.conexao.insert_id()

def conecta(dir, uid, senha):
  conexao = sql.connect(user=uid, password=senha, database=(dir + "/mc857"))
  bas = Base_IMP(conexao)
  return bas

