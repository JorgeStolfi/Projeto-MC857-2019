#! /usr/bin/python3

#Testes do módulo {conversao_sql}
import identificador
import conversao_sql

# Para diagnóstico:
import sys

# ----------------------------------------------------------------------
# Classe de objeto para teste:

class ObjBobo:
  def __init__(self,peso,orelhas):
    self.peso = peso;
    self.orelhas = orelhas
    
bobo1 = ObjBobo(23,'SIM')  
bobo1_ind = 100

bobo2 = ObjBobo(43,'AMBAS')
bobo2_ind = 200

def obtem_indice(obj,tipo_mem):
  if obj == bobo1:
    return bobo1_ind
  elif obj == bobo2:
    return bobo2_ind
  else:
    assert False

def obtem_obj(ind,tipo_mem):
  if ind == bobo1_ind:
    return bobo1
  elif ind == bobo2_ind:
    return bobo2
  else:
    assert False

# ----------------------------------------------------------------------

# define uma tabela boba só para conversao:
nome_tb = "objs"
let = "X"
cache = {}.copy()
colunas = (
  ('nome',    type("foo"), 'TEXT',        3,    60),
  ('email',   type("foo"), 'TEXT',        6,    60),
  ('CPF',     type("foo"), 'TEXT',       14,    14),
  ('pernas',  type(10),    'INTEGER',     2,  1000),
  ('volume',  type(412.2), 'FLOAT',   100.0, 999.9),
  ('chato',   type(True),  'INTEGER',     0,     0),
  ('bobagem', type(bobo1), 'INTEGER',     0,     0)
)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_valor(rotulo, val_mem, tipo_mem, val_SQL, tipo_SQL, vmin, vmax):
  """Testa {valor_mem_para_valor_SQL} e {valor_SQL_para_valor_mem}."""
  global ok_global
  ok = True # Estado deste teste.
  
  # Mostra parâmetros:
  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write(rotulo + "\n")
  sys.stderr.write("  val_mem = " + str(val_mem) + " tipo_mem = " + str(tipo_mem) + "\n")
  sys.stderr.write("  val_SQL = " + str(val_SQL) + " tipo_SQL = " + str(tipo_SQL) + "\n")
  sys.stderr.write("  vmin = " + str(vmin) + " vmax = " + str(vmax) + "\n")
   
  val_SQL_cmp = conversao_sql.valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, vmin, vmax, obtem_indice)
  if val_SQL_cmp != val_SQL:
    sys.stderr.write("  **erro: {valor_mem_para_valor_SQL} não bate = '" + str(val_SQL_cmp) + "'\n")
    ok = False
  val_mem_cmp = conversao_sql.valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, vmin, vmax, obtem_obj)
  if val_mem_cmp != val_mem:
    sys.stderr.write("  **erro: {valor_SQL_para_valor_mem} não bate = '" + str(val_mem_cmp) + "'\n")
    ok = False
  if ok:
    sys.stderr.write("  verifica_valor: ok\n")
  ok_global = ok_global and ok
  
def verifica_dict(rotulo, dic_mem, dic_SQL):
  """Testa {dict_mem_para_dict_SQL} e {dict_SQL_para_dict_mem}."""
  global ok_global
  ok = True # Estado deste teste.

  # Mostra parâmetros:
  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write(rotulo + "\n")
  dic_SQL_cmp = conversao_sql.dict_mem_para_dict_SQL(dic_mem, colunas, obtem_indice)
  if dic_SQL_cmp != dic_SQL:
    sys.stderr.write("  **erro: {dict_mem_para_dict_SQL} não bate = '" + str(dic_SQL_cmp) + "'\n")
    ok = False
  dic_mem_cmp = conversao_sql.dict_SQL_para_dict_mem(dic_SQL, colunas, obtem_obj)
  if dic_mem_cmp != dic_mem:
    sys.stderr.write("  **erro: {dict_SQL_para_dict_mem} não bate = '" + str(dic_mem_cmp) + "'\n")
    ok = False
  if ok:
    sys.stderr.write("  verifica_dict: ok\n")
  ok_global = ok_global and ok

# ----------------------------------------------------------------------
# Testes de valor único:

verifica_valor("inteiro",        418,       type(418),       418,  'INTEGER',       417,      419)
verifica_valor("float",     418.4615,     type(418.1),  418.4615,  'FLOAT',     417.000, 418.4634)
verifica_valor("string",   "Qüêntão",     type("foo"), "Qüêntão",  'TEXT',            7,        7)
verifica_valor("booleano",   True,        type(True),          1,  'INTEGER',         0,        0)
verifica_valor("objeto",       bobo1,     type(bobo1), bobo1_ind,  'INTEGER',         0,        0)

# ----------------------------------------------------------------------
# Testes de dicionário:

dic1_mem = { 
  'nome':   "José da Silva",
  'email':  "josi@gmail.com",
  'CPF':    "123.456.789-00",
  'pernas':  2,
  'volume':  418.4634,
  'chato':   True,
  'bobagem': bobo2
}
dic1_SQL = {
  'nome':   "José da Silva",
  'email':  "josi@gmail.com",
  'CPF':    "123.456.789-00",
  'pernas':  2,
  'volume':  418.4634,
  'chato':   1,
  'bobagem': bobo2_ind
}

verifica_dict("dicionrio {dic1}", dic1_mem, dic1_SQL)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  # Terminou OK:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  # Termina com erro:
  sys.stderr.write("**erro - teste falhou\n")
  assert False
