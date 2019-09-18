# Imlementação do módulo {produto} e da classe {ObjProduto}.

import produto

import tabela_generica
import conversao_sql
import identificador
import tabelas
import sys # Para diagnóstico.

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "produtos"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjProdutos} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "P"
  # Prefixo dos identificadores de produtos.

colunas = \
  (
    ( 'descr_curta', type("foo"), 'TEXT',    False,   10,         80 ), # Descricao curta do produto.
    ( 'descr_media', type("foo"), 'TEXT',    False,    8,        250 ), # Descricao media do produto.
    ( 'descr_longa', type("foo"), 'TEXT',    False,   10,        500 ), # Descricao longa do produto.
    ( 'unidade',     type("foo"), 'TEXT',    False,    1,         20 ), # Unidade de venda ('metro', 'caixa', 'peça', etc.).
    ( 'preco',       type(10.5),  'FLOAT',   False,    1,  999999.99 ), # Preco unitário do produto em reais.
    ( 'estoque',     type(10),    'INTEGER', False,    0,   99999999 )  # Estoque do produto  

  )
  # Descrição das colunas da tabela na base de dados.

# Definição interna da classe {ObjUsuario}:

class ObjProduto_IMP():
  def __init__(self, id_produto, atrs):
    self.atributos = atrs.copy()
    self.id_produto = id_produto

# Implementação das funções:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs):
  global cache, nome_tb, letra_tb, colunas
  sys.stderr.write("produto_IMP.cria(" + str(atrs) + ") ...\n")
  
  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, tabelas.obj_para_indice)
  
  # Insere na base de dados e obtém o índice na mesma:
  prod = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(prod) is produto.ObjProduto:
    sys.stderr.write("produto_IMP.cria: ** erro: " + str(prod) + "\n")
    assert False
  return prod

def obtem_identificador(prod):
  global cache, nome_tb, letra_tb, colunas
  return prod.id_produto

def obtem_indice(prod):
  global cache, nome_tb, letra_tb, colunas
  return identificador.para_indice(letra_tb, prod.id_produto)

def obtem_atributos(prod):
  global cache, nome_tb, letra_tb, colunas
  return prod.atributos.copy()
  
def muda_atributos(prod, mods):
  global cache, nome_tb, letra_tb, colunas
  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice)
  
  # Modifica atributos na tabela e na memória:
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, prod.id_produto, mods_SQL)
  if res != prod:
    sys.stderr.write("produto_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def busca_por_identificador(id_produto):
  global cache, nome_tb, letra_tb, colunas
  prod = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_produto)
  return prod

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas
  usr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return usr

def busca_por_palavra(pal):
  chaves = ('descr_curta', 'descr_media')
  valores = (pal, pal)
  produtos =  tabela_generica.busca_por_semelhanca(nome_tb, letra_tb, colunas, chaves, valores)
  return produtos

def campos():
  global cache, nome_tb, letra_tb, colunas
  return colunas

# FUNÇÕES INTERNAS

def def_obj(obj, id_produto, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjProduto} com
  identificador {id_produto} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjProduto}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas
  sys.stderr.write("produto_IMP.def_obj(" + str(obj) + ", " + id_produto + ", " + str(atrs_SQL) + ") ...\n")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    sys.stderr.write("  criando objeto, atrs_mem = " + str(atrs_mem) + "\n")
    obj = produto.ObjProduto(id_produto, atrs_mem)
  else:
    assert obj.id_produto == id_produto
    # Converte atributos para formato na memória.
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    sys.stderr.write("  modificando objeto, mods_mem = " + str(mods_mem) + "\n")
    if len(mods_mem) > len(obj.atrs):
      sys.stderr.write("produto_IMP.def_obj:  **erro: numero excessivo de atributos a alterar\n")
      assert False
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        sys.stderr.write("produto_IMP.def_obj: **erro: chave '" + chave + "' inválida\n")
        assert False
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        sys.stderr.write("produto_IMP.def_obj:  *erro: tipo do campo '" + chave + "' incorreto\n")
        assert False
      obj.atrs[chave] = val
  sys.stderr.write("  obj = " + str(obj) + "\n")
  return obj

