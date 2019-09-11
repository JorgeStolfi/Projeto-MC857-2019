# Imlementação do módulo {produto} e da classe {ObjProduto}.

import tabela_generica
import sys

# VARIÁVEIS GLOBAIS DO MÓDULO

# Nome da tabela na base de dados.
nome_tb = "produtos"

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
  
def muda_atributos(prod, alts):
  global cache, nome_tb, colunas
  res = tabela_generica.atualiza(nome_tb, cache, "U", colunas, cria_obj, muda_obj, prod.identificador, alts)
  if res != prod:
    sys.stderr.write("produto_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def cria_obj(id_prod, atrs):
  global cache, nome_tb, colunas
  sys.stderr.write("produto_IMP.cria_obj(" + id_prod + ", " + str(atrs) + ") ...\n")
  prod = ObjProduto_IMP(id_prod, atrs)
  sys.stderr.write("  prod = " + str(prod) + "\n")
  return prod

def muda_obj(prod, alts):
  global cache, nome_tb, colunas
  sys.stderr.write("produto_IMP.muda_obj\n")
  sys.stderr.write("  prod antes = " + str(prod) + "\n")
  sys.stderr.write("  alts = " + str(alts) + "\n")

  if len(alts) > len(prod.atributos):
    return "**erro: numero excessivo de atributos a alterar"

  for chave, val in alts.items():
    if not chave in prod.atributos:
      return "**erro: chave '" + chave + "' inválida"
    val_velho = prod.atributos[chave]
    if not type(val_velho) is type(val):
      return "**erro: tipo do campo '" + chave + "' incorreto"
    prod.atributos[chave] = val

  sys.stderr.write("  prod = " + str(prod) + "\n")
  return prod

def cria(atrs):
  global cache, nome_tb, colunas
  sys.stderr.write("produto_IMP.cria(" + str(atrs) + ") ...\n")
  # Insere na base de dados e obtém o índice na mesma:
  prod = tabela_generica.acrescenta(nome_tb, cache, "U", colunas, cria_obj, atrs)
  if not type(prod) is ObjProduto_IMP:
    sys.stderr.write("produto_IMP.cria: ** erro: " + str(prod) + "\n")
    assert False
  return prod

def campos():
  global cache, nome_tb, colunas
  return colunas

def busca_por_palavra_chave(palavras_chave):
  # Implementar um busca por like/semelhanca no modulo de tabelas
  # e realizar a busca das palavras chaves em cada campo
  # do produto
  pass

def busca_por_identificador(id_produto):
  global cache, nome_tb, colunas
  prod = tabela_generica.busca_por_identificador(nome_tb, cache, "U", colunas, cria_obj, id_produto)
  return prod
