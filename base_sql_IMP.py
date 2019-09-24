# Implementação do módulo {base_sql}.

import sqlite3, sys
from utils_testes import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO

conexao = None 
  # O objeto retornado por {sqlite3.connect(...)}.  
  # Os métodos deste objeto permitem acessar a base no disco."""

# IMPLEMENTAÇÔES

def codifica_valor(val):
  # !!! Deveria proteger caracteres especiais em {val}, como ';'. !!!
  if val == None:
    return "NULL"
  elif type (val) is int:
    return str(val)
  elif type(val) is str:
    return "'" + val + "'"
  elif type(val) is float:
    return ("%.2f" % val)
  else:
    erro_prog("valor " + str(val) + " tipo = " + str(type(val)) + " invalido")
    return None

def conecta(dir, uid, senha):
  # Ignora {uid} e {senha} por enquanto.
  global conexao
  if conexao != None: 
    mostra(4,"base_sql_IM.conecta: !! Já conectada")
    return None
  try:
    conexao = sqlite3.connect(dir)
    mostra(4,"base_sql_IMP.conecta: base {sqlite3}, versao = " + sqlite3.version)
    return None
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.conecta: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_CREATE_TABLE(nome_tb, descr_cols):
  global conexao
  try:
    cursor = conexao.cursor()
    cmd = "CREATE TABLE IF NOT EXISTS " + nome_tb + "( " + descr_cols + " )"
    cursor.execute(cmd)
    return None
  except sqlite3.Error as msg:
    mostra(4,"Base_SQL_IMP.executa_comando_CREATE_TABLE: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_INSERT(nome_tb, atrs):
  global conexao
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
  mostra(4,"BASE_SQL_IMP.executa_comando_INSERT: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    return cursor.lastrowid
  except sqlite3.Error as msg:
    mostra(4,"BASE_SQL_IMP.executa_comando_INSERT: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_UPDATE(nome_tb, cond, atrs):
  global conexao
  pares = ""
  for ch in atrs.keys():
    val = codifica_valor(atrs[ch]);
    # Acrescenta "{ch} = {val}" à lista de alterações de colunas:
    if pares != "": pares = pares + ","
    pares = pares + ch + " = " + val
  cmd = "UPDATE " + nome_tb + " SET " + pares + " WHERE " + cond
  mostra(4,"BASE_SQL_IMP.executa_comando_UPDATE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    return None
  except sqlite3.Error as msg:
    mostra(4,"BASE_SQL_IMP.executa_comando_UPDATE: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_SELECT(nome_tb, cond, nomes_cols):
  global conexao
  cols = ""
  for cn in nomes_cols:
    # Acrescenta "{cn} à lista de nomes de colunas:
    if cols != "": cols = cols + ","
    cols = cols + cn

  cmd = "SELECT " + cols + " FROM " + nome_tb + " WHERE " + cond
  mostra(4,"BASE_SQL_IMP.executa_comando_SELECT: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    iterador = cursor.execute(cmd)
    res = cursor.fetchall() # Converte o iterador em lista.
    cursor.close()
    mostra(4,"BASE_SQL_IMP.executa_comando_SELECT: len(res) = " + str(len(res)))
    return res
  except sqlite3.Error as msg:
    mostra(4,"BASE_SQL_IMP.executa_comando_SELECT: ** erro = \"" + str(msg) + "\"")
    mostra(4,"  cmd = \"" + str(cmd) + "\"")
    return msg

def executa_comando_DELETE(nome_tb, cond):
  global conexao
  cmd = "DELETE FROM " + nome_tb + " WHERE " + cond
  mostra(4,"BASE_SQL_IMP.executa_comando_DELETE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    cursor.close()
    return None
  except sqlite3.Error as msg:
    mostra(4,"BASE_SQL_IMP.executa_comando_DELETE: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_DROP_TABLE(nome_tb):
  global conexao
  cmd = "DROP TABLE IF EXISTS " + nome_tb
  mostra(4,"BASE_SQL_IMP.executa_comando_DROP_TABLE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    cursor.close()
    return None
  except sqlite3.Error as msg:
    mostra(4,"BASE_SQL_IMP.executa_comando_DROP_TABLE: ** erro = \"" + str(msg) + "\"")
    return msg
    

