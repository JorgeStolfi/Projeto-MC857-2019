# Imlementação do módulo {tabela_generica}.

import base_sql
import identificador
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
  if type(res) is str:
    return res
  else:
    return None

def acrescenta(nome_tb, cache, let, cols, cria_obj, atrs):
  # Confere se atributos são válidos:
  if len(cols) != len(atrs):
    return "**erro: numero incorreto de atributos"
  for cp in cols:
    chave = cp[0]
    tipo = cp[1]
    vmin = cp[3]
    vmax = cp[4]
    if not chave in atrs:
      return "**erro: falta atributo '" + chave + "'"
    else:
      val = atrs[chave]
      if type(val) != tipo:
        return "**erro: atributo '" + chave + "' com tipo incorreto"
      elif type(val) is str:
        if len(val) < vmin or len(val) > vmax:
          return "**erro: tamanho do atributo '" + chave + "' fora dos limites"
      else:
        if val < vmin or val > vmax:
          return "**erro: atributo '" + chave + "' fora dos limites"
  # Insere na base de dados e obtém o índice na mesma:
  ind = base_sql.executa_comando_INSERT(nome_tb, atrs)
  # Cria o objeto :
  ident = identificador.de_indice(let, ind)
  obj = cria_obj(ident,atrs)
  cache[ident] = obj
  return obj

def busca_por_identificador(nome_tb, cache, let, cols, cria_obj, ident):
  if ident in cache:
    return cache[ident]
  else:
    ind = identificador.para_indice(let, ident)
    cond = "indice = " + str(ind)
    col_nomes = ( c[0] for c in cols )
    res = base_sql.executa_comando_SELECT(nome_tb, cond, col_nomes)
    sys.stderr.write("res = " + str(res) + "\n")
    if res == None or len(res) == 0:
      return None
    else:
      if len(res) > 1:
        return "**erro: SELECT com índice em '" + nome_tb + "' não é único"
      col_vals = res[0]
      assert len(col_vals) == len(col_nomes)
      atrs = dict(zip(col_nomes, col_vals))
      obj = cria_obj(ident,atrs)
      cache[ident] = obj
      return obj

def busca_por_campo(nome_tb, cache, let, cols, chave, valor):
  # Converte {valor} para string na libuagem SQL:
  valor = base_sql.codifica_valor(valor)

  # Supõe que o cache é um subconjuto da base em disco, então procura só na última:
  cond = chave + " = " + valor
  sys.stderr.write("executa_comando_SELECT cond = \"" + str(cond) + "\"\n")
  res = base_sql.executa_comando_SELECT(nome_tb, cond, ['indice'])
  sys.stderr.write("  res = " + str(res) + "\n")
  if res == None:
    # Busca falhou?
    return [].copy()
  elif type(res) is str:
    # Deu algum erro:
    return res
  else:
    # Resultado deve ser uma lista de tuplas, cada uma contendo apenas um índice:
    idents = [ identificador.de_indice(let, ind[0]) for ind in res ]
    return idents

def atualiza(nome_tb, cache, let, cols, cria_obj, muda_obj, ident, alts):
  # Obtém o objeto com esse identificador e garante que está em {cache}:
  obj = busca_por_identificador(nome_tb, cache, let, cols, cria_obj, ident)
  if obj == None:
    # Objeto não existe:
    return "**erro: identificador '" + ident + "' nao encontrado"
  elif type(obj) is str:
    # Deu algum erro:
    return obj
  # Atualiza os atributos do objeto na memória:
  muda_obj(obj,alts)
  # Atualiza a base de dados:
  ind = identificador.para_indice(let, ident)
  cond = "indice = " + str(ind)
  res = base_sql.executa_comando_UPDATE(nome_tb, cond, alts)
  if res == None:
    return obj
  else:
    return "**erro: UPDATE da tabela '" + nome_tb + "' falhou"

def limpa_tabela(nome_tb, cols):
  res = base_sql.executa_comando_DROP_TABLE(nome_tb);
  if type(res) is str:
    return res
  assert res == None
  colunas = constroi_colunas_SQL(cols)
  res = base_sql.executa_comando_CREATE_TABLE(nome_tb, colunas);
  if type(res) is str:
    return res
  assert res == None
  
  
