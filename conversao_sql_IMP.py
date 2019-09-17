# Implementação do módulo {conversao_sql}

# CONVERSÃO DE VALORES MEMÓRIA <--> SQL

import identificador
import sys # Para diagnósticos

def valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, nulo_ok, vmin, vmax, obj_para_indice):
  if val_mem == None:
    if nulo_ok:
      return None
    else:
      sys.stderr.write("**erro: atributo não pode ser {None}\n")
      assert False 
  if type(val_mem) != tipo_mem:
    sys.stderr.write("**erro: atributo " + str(val_mem) + " com tipo incorreto\n")
    assert False 
  elif type(val_mem) is str:
    if len(val_mem) < vmin or len(val_mem) > vmax:
      sys.stderr.write("**erro: tamanho da cadeia '" + str(val_mem) + "' fora dos limites\n")
      assert False
    assert tipo_SQL == 'TEXT'
    val_SQL = val_mem
  elif type(val_mem) is int:
    if val_mem < vmin or val_mem > vmax:
      sys.stderr.write("**erro: valor int " + str(val_mem) + " fora dos limites\n")
      assert False
    assert tipo_SQL == 'INTEGER'
    val_SQL = val_mem
  elif type(val_mem) is float:
    if val_mem < vmin or val_mem > vmax:
      sys.stderr.write("**erro: valor float " + str(val_mem) + " fora dos limites\n")
      assert False
    assert tipo_SQL == 'FLOAT'
    val_SQL = val_mem
  elif type(val_mem) is bool:
    assert tipo_SQL == 'INTEGER'
    val_SQL = (1 if val_mem else 0)
  elif type(val_mem) is list or type(val_mem) is tuple or type(val_mem) is dict:
    sys.stderr.write("**erro: valor " + str(val_mem) + " não pode ser convertido\n")
    assert False
  else:
    # Supõe que é objeto.  Obtem o indice:
    assert tipo_SQL == 'INTEGER'
    val_SQL = obj_para_indice(val_mem, tipo_mem)
  return val_SQL

def valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, nulo_ok, vmin, vmax, indice_para_obj):
  if val_SQL == None:
    if nulo_ok:
      return None
    else:
      sys.stderr.write("**erro: atributo não pode ser {None}\n")
      assert False 
  if tipo_mem is list or tipo_mem is tuple or tipo_mem is dict:
    sys.stderr.write("**erro: valor " + str(val_SQL) + " não pode ser convertido para tipo " + str(tipo_mem) + "\n")
    assert False
  if tipo_SQL == 'TEXT':
    assert type(val_SQL) is str
    if len(val_SQL) < vmin or len(val_SQL) > vmax:
      sys.stderr.write("**erro: tamanho da cadeia '" + str(val_SQL) + "' fora dos limites\n")
      assert False
    val_mem = val_SQL
  elif tipo_SQL == 'FLOAT':
    assert type(val_SQL) is float
    if val_SQL < vmin or val_SQL > vmax:
      sys.stderr.write("**erro: valor float " + str(val_SQL) + " fora dos limites\n")
      assert False
    val_mem = val_SQL
  elif tipo_SQL == 'INTEGER':
    assert type(val_SQL) is int
    # Tipo na memória pode ser {int}, {bool}, ou objeto
    if tipo_mem is int:
      if val_SQL < vmin or val_SQL > vmax:
        sys.stderr.write("**erro: valor inteiro " + str(val_SQL) + " fora dos limites\n")
        assert False
      val_mem = val_SQL
    elif tipo_mem is bool:
      if val_SQL < 0 or val_SQL > 1:
        sys.stderr.write("**erro: valor booleano " + str(val_SQL) + " inválido\n")
        assert False
      val_mem = (val_SQL == 1)
    else:
      # Supõe que é objeto.  Obtem o dito cujo:
      val_mem = indice_para_obj(val_SQL, tipo_mem)
  else:
    sys.stderr.write("**erro: tipo SQL '" + str(tipo_SQL) + "' inválido\n")
    assert False
  assert type(val_mem) is tipo_mem
  return val_mem

# CONVERSÃO DE DICIONÁRIOS MEMÓRIA <--> SQL

def dict_mem_para_dict_SQL(dic_mem, cols, obj_para_indice):
  if len(dic_mem) > len(cols):
    sys.stderr.write("**erro: numero excessivo de atributos em " + str(dic_mem) + "\n")
    assert False
  dic_SQL = {}.copy()
  omitidos = 0; # Número de campos de {dic_mem} omitidos de {dic_SQL} por necessidade:
  for chave, tipo_mem, tipo_SQL, nulo_ok, vmin, vmax in cols:
    if chave in dic_mem:
      val_mem = dic_mem[chave]
      if val_mem != None and not type(val_mem) is tipo_mem:
        sys.stderr.write("**erro: valor " + str(val_mem) + " deveria ter tipo " + str(tipo_mem) + "\n")
        assert False
      # Omite valores de {dic_mem} que são seqüências ou dicionários:
      if val_mem != None and (type(val_mem) is list or type(val_mem) is tuple or type(val_mem) is dict):
        omitidos = omitidos + 1
      else:
        val_SQL = valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, nulo_ok, vmin, vmax, obj_para_indice)
        dic_SQL[chave] = val_SQL
  if len(dic_mem) > len(dic_SQL) + omitidos:
    sys.stderr.write("**erro: atributos espúrios em " + str(dic_mem) + "\n")
    assert False
  return dic_SQL

def dict_SQL_para_dict_mem(dic_SQL, cols, indice_para_obj):
  if len(dic_SQL) > len(cols):
    sys.stderr.write("**erro: numero excessivo de atributos em " + str(dic_SQL) + "\n")
    assert False
  dic_mem = {}.copy()
  for chave, tipo_mem, tipo_SQL, nulo_ok, vmin, vmax in cols:
    if chave in dic_SQL: 
      val_SQL = dic_SQL[chave]
      if tipo_mem is list or tipo_mem is tuple or tipo_mem is dict:
        sys.stderr.write("**erro: campo de tipo " + str(tipo_mem) + " = '" + str(val_SQL) + "' não pode estar na tabela\n")
        assert False
      val_mem = valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, nulo_ok, vmin, vmax, indice_para_obj)
      dic_mem[chave] = val_mem
  if len(dic_SQL) > len(dic_mem):
    sys.stderr.write("**erro: atributos espúrios em " + str(dic_SQL) + "\n")
    assert False
  return dic_mem

