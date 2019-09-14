# Imlementação do módulo {produto} e da classe {ObjProduto}.

import tabela_generica
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO

# Nome da tabela na base de dados.
nome_tb = "produtos"

letra_tb = "P"
  # Prefixo dos identificadores de produtos.

# Dicionário que mapeia identificadores para os objetos {ObjProdutos} na memória.
# Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
# a fim de garantir a unicidadde dos objetos.
cache = {}.copy()

colunas = \
  (
    ( 'descr_curta', type("foo"), 'TEXT NOT NULL',  10, 80), # Descricao curta do produto.
    ( 'descr_media', type("foo"), 'TEXT NOT NULL',  8,  250), # Descricao media do produto.
    ( 'descr_longa', type("foo"), 'TEXT NOT NULL',  10, 500), # Descricao longa do produto.
    ( 'unidade',     type("foo"), 'TEXT NOT NULL',  0,  1000), # numero de unidades disponiveis no estoque
    ( 'preco',       type(float), 'FLOAT NOT NULL', 1,  10**10), # preco do produto em reais
  )
  # Descrição das colunas da tabela na base de dados.

def inicializa():
  global cache, nome_tb, colunas
  # Cria a tabela:
  res = tabela_generica.cria_tabela(nome_tb, colunas)
  if res != None:
    sys.stderr.write("produto_IMP.inicializa: **erro " + str(res) + "\n")
    assert False

class ObjProduto_IMP():
  def __init__(self, identificador, atrs):
    self.atributos = atrs.copy()
    self.identificador = identificador

def obtem_identificador(prod):
  global cache, nome_tb, colunas
  return prod.identificador

def obtem_atributos(prod):
  global cache, nome_tb, colunas
  return prod.atributos.copy()
  
def muda_atributos(prod, mods):
  global cache, nome_tb, colunas
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, prod.identificador, mods)
  if res != prod:
    sys.stderr.write("produto_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def cria(atrs):
  global cache, nome_tb, colunas
  sys.stderr.write("produto_IMP.cria(" + str(atrs) + ") ...\n")
  # Insere na base de dados e obtém o índice na mesma:
  atrs_SQL = ???(atrs)
  prod = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(prod) is ObjProduto_IMP:
    sys.stderr.write("produto_IMP.cria: ** erro: " + str(prod) + "\n")
    assert False
  return prod

def campos():
  global cache, nome_tb, colunas
  return colunas

def busca_por_palavras_chave(palavras_chave):
  produtos =  tabela_generica.busca_por_semelhanca(nome_tb, cache, letra_tb, colunas, def_obj, palavras_chave)
  return produtos

def busca_por_identificador(id_produto):
  global cache, nome_tb, colunas
  prod = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_produto)
  return prod

# FUNÇÕES INTERNAS

def def_obj(obj, ident, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjSessao} com
  identificador {ident} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjSessao}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, colunas
  sys.stderr.write("produto_IMP.def_obj(" + str(obj) + ", " + ident + ", " + str(atrs_SQL) + ") ...\n")
  if obj == None:
    atrs_mem = ???(atrs_SQL)
    sys.stderr.write("  criando objeto, atrs_mem = " + str(atrs) + "\n")
    obj = ObjProduto_IMP(ident, atrs)
  else
    assert obj.id == ident
    mods_mem = ???(atrs_SQL)
    sys.stderr.write("  modificando objeto, mods_mem = " + str(atrs) + "\n")
    if len(mods) > len(obj.atributos):
      return "**erro: numero excessivo de atributos a alterar"
    for chave, val in mods.items():
      if not chave in obj.atributos:
        return "**erro: chave '" + chave + "' inválida"
      val_velho = obj.atributos[chave]
      if not type(val_velho) is type(val):
        return "**erro: tipo do campo '" + chave + "' incorreto"
      obj.atributos[chave] = val
  sys.stderr.write("  obj = " + str(obj) + "\n")
  return obj

