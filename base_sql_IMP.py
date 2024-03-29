# Implementação do módulo {base_sql}.

import sqlite3, sys
from utils_testes import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO

conexao = None 
  # O objeto retornado por {sqlite3.connect(...)}.  
  # Os métodos deste objeto permitem acessar a base no disco."""
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# IMPLEMENTAÇÔES

def conecta(dir, uid, senha):
  # Ignora {uid} e {senha} por enquanto.
  global conexao, diags
  mostra(4,"base_sql_IMP.conecta: conectando com a base")
  if conexao != None: 
    mostra(6,"base_sql_IMP.conecta: !! Já conectada")
    return None
  try:
    conexao = sqlite3.connect(dir + "/MC857.sqlite3")
    if diags: mostra(6,"base_sql_IMP.conecta: base {sqlite3}, versao = " + sqlite3.version)
    return None
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.conecta: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_CREATE_TABLE(nome_tb, descr_cols):
  global conexao, diags
  try:
    cursor = conexao.cursor()
    cmd = "CREATE TABLE IF NOT EXISTS " + nome_tb + "( " + descr_cols + " )"
    if diags: mostra(4,"base_sql_IMP.executa_comando_CREATE_TABLE: cmd = \"" + str(cmd) + "\"")
    cursor.execute(cmd)
    return None
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.executa_comando_CREATE_TABLE: ** erro = \"" + str(msg) + "\"")
    return msg

def num_entradas(nome_tb, nome_indice):
  global conexao, diags
  try:
    cursor = conexao.cursor()
    cmd = 'SELECT max(' + nome_indice + ') FROM ' + nome_tb
    if diags: mostra(4,"base_sql_IMP.num_entradas: cmd = \"" + str(cmd) + "\"")
    cursor.execute(cmd)
    max_ind = cursor.fetchone()[0]
    if diags: mostra(6,"max_ind = " + str(max_ind))
    if max_ind == None:
      max_ind = 0
    return max_ind
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.num_entradas: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_INSERT(nome_tb, atrs):
  global conexao, diags
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
  if diags: mostra(4,"base_sql_IMP.executa_comando_INSERT: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    ind = cursor.lastrowid
    if diags: mostra(6,"lastrowid = " + str(ind))
    return ind
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.executa_comando_INSERT: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_UPDATE(nome_tb, cond, atrs):
  global conexao, diags
  pares = ""
  for ch in atrs.keys():
    val = codifica_valor(atrs[ch]);
    # Acrescenta "{ch} = {val}" à lista de alterações de colunas:
    if pares != "": pares = pares + ","
    pares = pares + ch + " = " + val
  cmd = "UPDATE " + nome_tb + " SET " + pares + " WHERE " + cond
  if diags: mostra(4,"base_sql_IMP.executa_comando_UPDATE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    return None
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.executa_comando_UPDATE: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_SELECT(nome_tb, cond, nomes_cols):
  global conexao, diags
  cols = ""
  for cn in nomes_cols:
    # Acrescenta "{cn} à lista de nomes de colunas:
    if cols != "": cols = cols + ","
    cols = cols + cn

  cmd = "SELECT " + cols + " FROM " + nome_tb + " WHERE " + cond
  if diags: mostra(4,"base_sql_IMP.executa_comando_SELECT: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    iterador = cursor.execute(cmd)
    res = cursor.fetchall() # Converte o iterador em lista.
    cursor.close()
    if diags: mostra(6,"base_sql_IMP.executa_comando_SELECT: len(res) = " + str(len(res)))
    return res
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.executa_comando_SELECT: ** erro = \"" + str(msg) + "\"")
    mostra(4,"  cmd = \"" + str(cmd) + "\"")
    return msg

def executa_comando_DELETE(nome_tb, cond):
  global conexao, diags
  cmd = "DELETE FROM " + nome_tb + " WHERE " + cond
  if diags: mostra(4,"base_sql_IMP.executa_comando_DELETE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    cursor.close()
    return None
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.executa_comando_DELETE: ** erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_DROP_TABLE(nome_tb):
  global conexao, diags
  cmd = "DROP TABLE IF EXISTS " + nome_tb
  if diags: mostra(4,"base_sql_IMP.executa_comando_DROP_TABLE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = conexao.cursor()
    cursor.execute(cmd)
    conexao.commit()
    cursor.close()
    return None
  except sqlite3.Error as msg:
    mostra(4,"base_sql_IMP.executa_comando_DROP_TABLE: ** erro = \"" + str(msg) + "\"")
    return msg
    
def codifica_valor(val):
  # !!! (MAIS TARDE) Deveria proteger caracteres especiais em {val}, como ';'. !!!
  global conexao, diags
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

def mostra_comandos(val):
  global conexao, diags
  diags = val
  return
