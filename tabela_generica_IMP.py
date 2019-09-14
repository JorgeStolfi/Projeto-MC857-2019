# Imlementação do módulo {tabela_generica}.

import base_sql
import identificador
import conversao_sql
import sys # Para depuração.

# FUNÇÕES INTERNAS

def constroi_colunas_SQL(cols):
  """Constrói a descrição SQL das colunas de uma tabela, 
  dada a lista de propriedades {cols} como fornecida
  a {cria_tabela}."""
  colunas = "indice integer NOT NULL PRIMARY KEY"
  for cp in cols:
    chave = cp[0]
    tipo_SQL = cp[2]
    colunas = colunas + ", " + chave + " " + tipo_SQL
  return colunas

# IMPLEMENTAÇÕES

def cria_tabela(nome_tb, cols):
  colunas = constroi_colunas_SQL(cols)
  res = base_sql.executa_comando_CREATE_TABLE(nome_tb, colunas);
  if res != None:
    sys.stderr.write("usuario_IMP.inicializa: **erro CREATE_TABLE falhou " + str(res) + "\n")
    assert type(res) is str
    assert False
  return

def acrescenta(nome_tb, cache, let, cols, def_obj, atrs_SQL):
  # Insere na base de dados e obtém o índice na mesma:
  ind = base_sql.executa_comando_INSERT(nome_tb, atrs_SQL)
  if not type(ind) is int:
    sys.stderr.write("tabela_generica_IMP.acrescenta: ** erro: indice inválido " + str(ind) + "\n");
    assert False
  # Cria o objeto :
  ident = identificador.de_indice(let, ind)
  obj = def_obj(None, ident, atrs_SQL)
  cache[ident] = obj
  return obj

def busca_por_identificador(nome_tb, cache, let, cols, def_obj, ident):
  if ident in cache:
    return cache[ident]
  else:
    ind = identificador.para_indice(let, ident)
    return busca_por_identificador_e_indice(nome_tb, cache, let, cols, def_obj, ident, ind)
    
def busca_por_indice(nome_tb, cache, let, cols, def_obj, ind):
  ident = identificador.de_indice(let, ind)
  if ident in cache:
    return cache[ident]
  else:
    return busca_por_identificador_e_indice(nome_tb, cache, let, cols, def_obj, ident, ind)
    
def busca_por_identificador_e_indice(nome_tb, cache, let, cols, def_obj, ident, ind):
  """Função interna: mesmo que {busca_por identificador}, mas exige o índice inteiro {ind}
  da linha da tabela, além do identificador {ident}."""
  cond = "indice = " + str(ind)
  col_nomes = ( c[0] for c in cols )
  res = base_sql.executa_comando_SELECT(nome_tb, cond, col_nomes)
  if res == None or len(res) == 0:
    return None
  else:
    if len(res) > 1:
      sys.stderr.write("**erro: SELECT com índice em '" + nome_tb + "' não é único\n")
      sys.stderr.write("res = " + str(res) + "\n")
      assert False
    col_vals = res[0]
    assert len(col_vals) == len(col_nomes)
    atrs_SQL = dict(zip(col_nomes, col_vals))
    obj = def_obj(None, ident, atrs_SQL)
    cache[ident] = obj
    return obj

def busca_por_campo(nome_tb, cache, let, cols, chave, valor):
  # Converte {valor} para string na libuagem SQL:
  valor = base_sql.codifica_valor(valor)

  # Supõe que o cache é um subconjuto da base em disco, então procura só na última:
  cond = chave + " = " + valor
  sys.stderr.write("executa_comando_SELECT cond = \"" + str(cond) + "\"\n")
  res = base_sql.executa_comando_SELECT(nome_tb, cond, ['indice'])
  if res != None and type(res) is str:
    sys.stderr.write("usuario_IMP.busca_por_campo: **erro SELECT falhou " + str(res) + "\n")
    assert False
  return identificador.de_lista_de_indices(let, res)

def busca_por_semelhanca(nome_tb, cache, let, cols, chaves, valores):
  cond = ""
  total_de_chaves = len(chaves)
  for key in chaves:
    index_chave = chaves.index(key)
    for value in valores:
      cond += (key + "LIKE '%" + value + "%'")
      if (total_de_chaves - index_chave) != 1:
        cond += " OR "
  res = base_sql.executa_comando_SELECT(nome_tb, cond, ['indice'])
  if res != None and type(res) is str:
    sys.stderr.write("usuario_IMP.busca_por_campo: **erro SELECT falhou " + str(res) + "\n")
    assert False
  return identificador.de_lista_de_indices(let, res)

def atualiza(nome_tb, cache, let, cols, def_obj, ident, mods_SQL):
  # Obtém o objeto com esse identificador e garante que está em {cache}:
  obj = busca_por_identificador(nome_tb, cache, let, cols, def_obj, ident)
  if obj == None:
    # Objeto não existe:
    sys.stderr.write("**erro: identificador '" + ident + "' nao encontrado\n")
    assert False
  # Atualiza os atributos do objeto na memória:
  res = def_obj(obj, ident, mods_SQL)
  assert res == obj
  # Atualiza a base de dados:
  ind = identificador.para_indice(let, ident)
  cond = "indice = " + str(ind)
  res = base_sql.executa_comando_UPDATE(nome_tb, cond, mods_SQL)
  if res != None:
    sys.stderr.write("**erro: UPDATE da tabela '" + nome_tb + "' falhou\n")
    assert False
  return obj

def limpa_tabela(nome_tb, cols):
  res = base_sql.executa_comando_DROP_TABLE(nome_tb);
  if res != None:
    sys.stderr.write("**erro: DROP_TABLE de " + nome_tb + " falhou, res = '" + str(res) + "' falhou\n")
    assert type(res) is str
    assert False
  cria_tabela(nome_tb, cols)
  return
  
