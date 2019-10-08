# Este módulo oferece funções para converter valores 
# entre o formato de memória ({mem}), usado em variáveis e campos
# de objetos Python, e o formato usado na base de dados SQL.

# Nas funções abaixo, o parâmetro {obj_para_indice} é uma função que, dado um 
# objeto Python {obj} na memória e seu tipo {tipo_mem}
# (como {ObjUsuario}, {ObjCompra}, etc.)
# devolve um inteiro que é seu índice na tabela correspondente
# da base SQL.
#
# Nas funções abaixo, {indice_para_obj} é uma função que, dado o índice
# de uma linha de uma tabela da base SQL, e a classe {tipo_mem}
# do objeto Python correspondente na memória (como {ObjUsuario}, {ObjCompra}, etc.)
# devolve esse objeto.

# Implementação desta interface:
import conversao_sql_IMP

def valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, nulo_ok, vmin, vmax, obj_para_indice):
  """Converte um valor de atributo {val_mem} de tipo Python {tipo_mem}
  para o tipo {tipo_SQL} usado na base de dados. 
  
  Os parâmetros {vmin,vmax} são os limites mínimo e máximo
  para {val_mem}, antes da conversão. Se {tipo_mem} é inteiro ou float, os limites
  se referem ao valor; se {tipo_mem} é string, referem-se ao
  comprimento. Estes limites são ignorados nos demais casos. 
  
  Em particular, se {tipo_mem} é booleano, o {tipo_SQL} deve ser
  'INTEGER'; e o resultado é 0 se {val_mem=False}) e 1 {se val_mem=True}. Se
  {tipo_mem} é objeto Python (que representa um usuário, um produto,
  etc.), o {tipo_SQL} deve ser 'INTEGER'; e o objeto {val_mem} é convertido
  para um inteiro, o índice do mesmo na tabela correspondente,
  usando {obj_para_indice(val_mem,tipo_mem)}.
  
  Se o parametro {nulo_ok} for {True}, o valor {val_mem} pode ser {None},
  e nesse caso o resultado será {None}.  Se {nulo_ok} for {False}, o
  valor {val_mem} não pode ser {None}.
  
  Esta função dá erro se o tipo de {val_mem} for uma lista, tupla, ou dicionário."""
  return conversao_sql_IMP.valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, nulo_ok, vmin, vmax, obj_para_indice)
 
def valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, nulo_ok, vmin, vmax, indice_para_obj):
  """Converte um valor de atributo {val_SQL} do tipo {tipo_SQL} usado na base 
  de dados para um valor Python de tipo {tipo_mem}, como ficaria na 
  memória.
  
  Os parâmetros {vmin,vmax} são os limites mínimo e máximo para o valor
  resultante da conversão. Se {tipo_mem} é inteiro ou float, os limites
  se referem ao valor; se {tipo_mem} é string, referem-se ao
  comprimento. Estes limites são ignorados nos demais casos.
  
  Em particular, se {tipo_mem} é booleano, o {tipo_SQL} deve ser
  'INTEGER'; e o valor inteiro {val_SQL} é convertido para booleano usando a
  convenção 0={False}, 1={True}. Se {tipo_mem} é um objeto Python (que
  representa um usuário, um produto, etc.), o {tipo_SQL} deve ser
  'INTEGER': e o valor inteiro {val_SQL} é convertido para o objeto
  correspondente, usando {indice_para_obj(val_SQL,tipo_mem)}.
  
  Se o parametro {nulo_ok} for {True}, o valor {val_mem} pode ser {None},
  e nesse caso o resultado será {None}.  Se {nulo_ok} for {False}, o
  valor {val_mem} não pode ser {None}.
  
  Esta função dá erro se o {tipo_mem} for um tipo de lista, tupla,
  ou dicionário."""
  return conversao_sql_IMP.valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, nulo_ok, vmin, vmax, indice_para_obj)
  
# CONVERSÂO DE DICIONÁRIOS
# 
# As funções abaixo fazem a conversão entre um dicionário
# Python que representa atributos de um objeto na memória
# e outro dicionário que representa o conteúdo de uma 
# linha da tabela.
# 
# Nestas funções, o parâmetro {cols} deve ser uma descrição das 
# colunas da tabela, menos a coluna de índice de linha.
# Vide {tabela_generica.cria_tabela}.

  
def dict_mem_para_dict_SQL(dic_mem, cols, obj_para_indice):
  """Supõe que {dic_mem} é um dicionário Python com nomes e valores de
  atributos de um objeto na memória. Converte os valores para
  representações correspondentes na base de dados, usando
  {valor_mem_para_valor_SQL} e os tipos SQL especificados em {cols}.
  
  Os nomes dos campos em {dic_mem} devem ser um subconjunto dos
  definidos em {cols}. O dicionário retornado terá apenas esses mesmos
  campos.
  
  A lista de colunas {cols} não deve ter atributos cujo {tipo_mem} for
  lista, tupla, ou dicionário. """
  return conversao_sql_IMP.dict_mem_para_dict_SQL(dic_mem, cols, obj_para_indice)
  
def dict_SQL_para_dict_mem(dic_SQL, cols, indice_para_obj):
  """Supõe que {dic_SQL} é um dicionário Python com nomes
  e valores extraídos de uma linha de uma tabela da 
  base de dados. Converte os mesmos para nomes e valores 
  usando {valor_SQL_para_valor_mem}.
  
  Os nomes dos campos em {dic_SQL} devem ser um subconjunto dos campos
  definidos em {cols}.
  
  A lista {cols} não deve ter atributso cujo {tipo_mem} for lista, tupla, 
  ou dicionário."""
  return conversao_sql_IMP.dict_SQL_para_dict_mem(dic_SQL, cols, indice_para_obj)
  
