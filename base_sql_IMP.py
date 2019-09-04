# Implementação do módulo {base_sql}

import sqlite3, sys

def codifica_valor(val):
  """Converte o valor {val} para o formato que pode ser inserido em comandos SQL.
  Especificamente:
  
    Se {val} é um inteiro, converte em string de algarismos decimais,
    com sinal "-" se necessário. 
    
    Se {val} é um float, converte em um string decimal fracionário com
    (arbitrariamente) 2 casas depois do ponto, e sinal "-" se necessario. 
    
    Se {val} é um string, envolve-o em aspas simples. 
    !!! Deveria proteger caracteres especiais em {val}. !!!
  
  """
  
  if type (val) is int:
    return str(val)
  elif type(val) is str:
    return "'" + val + "'"
  elif type(val) is float:
    return ("%.2f" % val)
  else:
    assert False # Should raise an exception instead.
    return None

class Base_SQL_IMP:

  """Um objeto desta classe tem um atributo privado {conexao}
  que é o objeto retornado por {sqlite3.connect(...)}.  
  Or métodos deste objeto permitem acessar a base no disco."""

  def __init__(self, con):
    self.conexao = con

  def executa_comando_CREATE_TABLE(self, nome_tb, colunas):
    try:
      cursor = self.conexao.cursor()
      cmd = "CREATE TABLE IF NOT EXISTS " + nome_tb + "( " + colunas + " )"
      cursor.execute(cmd)
      return True
    except sqlite3.Error as msg:
      sys.stderr.write("Base_SQL_IMP.executa_comando_CREATE_TABLE: erro = \"" + msg + "\"\n")
      return False

  def executa_comando_INSERT(self, nome_tb, atrs):
    chaves = ""
    valores = ""
    for ch in atrs.keys():
      val = codifica_valor(atrs[ch]);
      # Acrescenta a chave {ch} à lista de nomes de colunas:
      if chaves != "": chaves = chaves + ","
      chaves = chaves + ch
      # Acrescent o valor {val} à lista de valores de colunas:
      if valores != "": valores = valores + ","
      valores = valores + val
    cmd = "INSERT INTO " + nome_tb + " ( " + chaves + " ) VALUES (" + valores + ")"
    try:
      cursor = self.conexao.cursor()
      cursor.execute(cmd)
      self.conexao.commit()
      return cursor.lastrowid
    except sqlite3.Error as msg:
      sys.stderr.write("BASE_SQL_IMP.executa_comando_INSERT: erro = \"" + msg + "\"\n")
      return None
        
  def executa_comando_UPDATE(self, nome_tb, cond, atrs):
    pares = ""
    for ch in atrs.keys():
      val = codifica_valor(atrs[ch]);
      # Acrescenta "{ch} = {val}" à lista de alterações de colunas:
      if pares != "": pares = pares + ","
      pares = pares + ch + " = " + val
    cmd = "UPDATE " + nome_tb + " SET " + pares + " WHERE " + cond
    try:
      cursor = self.conexao.cursor()
      cursor.execute(cmd)
      self.conexao.commit()
      return True
    except sqlite3.Error as msg:
      sys.stderr.write("BASE_SQL_IMP.executa_comando_UPDATE: erro = \"" + msg + "\"\n")
      return False
 
  def executa_comando_SELECT(self, nome_tb, cond, colunas):
    cols = ""
    for cn in colunas:
      # Acrescenta "{cn} à lista de nomes de colunas:
      if cols != "": cols = cols + ","
      cols = cols + cn
    
    cmd = "SELECT " + cols + " FROM " + nome_tb + " WHERE " + cond
    try:
      cursor = self.conexao.cursor()
      iterador = cursor.execute(cmd)
      res = cursor.fetchall() # Converte o iterador em lista.
      cursor.close()
      sys.stderr.write("BASE_SQL_IMP.executa_comando_SELECT: len(res) = " + str(len(res)) + "\n")
      return res
    except sqlite3.Error as error:
      return None

  def executa_comando_DELETE(self, nome_tb, nome_col, val_col):
    cmd = "DELETE FROM " + nome_tb + " WHERE " + nome_col + " = " + codifica_valor(val_col)
    try:
      cursor = self.conexao.cursor()
      cursor.execute(cmd)
      self.conexao.commit()
      cursor.close()
      return True
    except sqlite3.Error as error:
      return False

  def executa_comando_CLEAR_TABLE(self, nome_tb):
    cmd = "DELETE FROM " + nome_tb
    try:
      cursor = self.conexao.cursor()
      cursor.execute(cmd)
      self.conexao.commit()
      cursor.close()
      return True
    except sqlite3.Error as error:
      return False

def conecta(dir, uid, senha):
  # Ignora {uid} e {senha} por enquanto.
  try:
    conexao = sqlite3.connect(dir)
    sys.stderr.write("base_sql_IMP: connectado com base {sqlite3}, versao = " + sqlite3.version + "\n")
    bas = Base_SQL_IMP(conexao)
    return bas
  except sqlite3.Error as msg:
    sys.stderr.write("base_sql_IMP: ** erro = \"" + msg + "\"\n")
    return None
    

