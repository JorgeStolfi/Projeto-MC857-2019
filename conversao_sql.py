# Este módulo oferece funções para converter valores 
# entre o formato de memória ({mem}), usado em variáveis e campos
# de objetos Python, e o formato usado na base de dados SQL.

# Nas funções abaixo, o parâmetro {cols} é uma seqüência de tuplas 
# que descrevem os campos da tabela, menos o índice da linha.
# Vide descrição deste parâmetro em {cria_tabela}).
#
# Nas funções abaixo, o parâmetro {obtem_indice} é uma função que, dado um 
# objeto Python {obj} na memória e seu tipo {tipo_mem}
# (como {ObjUsuario}, {ObjCompra}, etc.)
# devolve um inteiro que é seu índice na tabela correspondente
# da base SQL.
#
# Nas funções abaixo, {obtem_obj} é uma função que, dado o índice
# de uma linha de uma tabela da base SQL, e a classe {tipo_mem}
# do objeto Python correspondente na memória (como {ObjUsuario}, {ObjCompra}, etc.)
# devolve esse objeto.

# Implementação desta interface:
import conversao_sql_IMP

def valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, vmin, vmax, obtem_indice):
  """Converte um valor de atributo {val_mem} de tipo Python {tipo_mem}
  para o tipo {tipo_SQL} usado na base de dados. 
  
  Os parâmetros {vmin,vmax} são os limites mínimo e máximo
  para {val_mem}, antes da conversão. Se {tipo_mem} é inteiro ou float, os limites
  se referem ao valor; se {tipo_mem} é string, referem-se ao
  comprimento. Estes limites são ignorados nos demais casos. 
  
  Em particular, se {tipo_mem} é booleano, o {tipo_SQL} deve ser
  'INTEGER'; e o resultado é 0 se {val=False}) e 1 {se val=True}. Se
  {tipo_mem} é objeto Python (que representa um usuário, um produto,
  etc.), o {tipo_SQL} deve ser 'INTEGER'; e o objeto {val_mem} é convertido
  para um inteiro, o índice do mesmo na tabela correspondente,
  usando {obtem_indice(val_mem,tipo_mem)}."""
  return conversao_sql_IMP.valor_mem_para_valor_SQL(val_mem, tipo_mem, tipo_SQL, vmin, vmax, obtem_indice)
 
def valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, vmin, vmax, obtem_obj):
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
  correspondente com {obtem_obj(val_SQL,tipo_mem)}."""
  return conversao_sql_IMP.valor_SQL_para_valor_mem(val_SQL, tipo_SQL, tipo_mem, vmin, vmax, obtem_obj)
  
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

  
def dict_mem_para_dict_SQL(dic, cols, obtem_indice):
  """Supõe que {dic} é um dicionário Python com nomes
  e valores de atributos de um objeto na memória.
  Converte os valores para representações correspondentes
  na base de dados, usando {valor_mem_para_valor_SQL}
  e os tipos especificados em {cols}.
  
  Os nomes dos campos em {dic} devem ser um subconjunto
  dos definidos em {cols}.  O dicionário retornado terá 
  apenas esses mesmos campos."""
  return conversao_sql_IMP.dict_mem_para_dict_SQL(dic, cols, obtem_indice)
  
def dict_SQL_para_dict_mem(dic, cols, obtem_obj):
  """Supõe que {dic} é um dicionário Python com nomes
  e valores extraídos de uma linha de uma tabela da 
  base de dados. Converte os mesmos para nomes e valores 
  usando {valor_SQL_para_valor_mem}.
  
  Os nomes dos campos em {dic} devem ser todos os campos
  definidos em {cols}."""
  return conversao_sql_IMP.dict_SQL_para_dict_mem(dic, cols, obtem_obj)
  
