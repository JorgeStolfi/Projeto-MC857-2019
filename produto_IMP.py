# Imlementação do módulo {produto} e da classe {ObjProduto}.

import produto

import tabela_generica
import conversao_sql
import identificador
import tabelas
from utils_testes import erro_prog, aviso_prog, mostra
import sys # Para diagnóstico.

# VARIÁVEIS GLOBAIS DO MÓDULO

# Nome da tabela na base de dados.
nome_tb = "produtos"

# Dicionário que mapeia identificadores para os objetos {ObjProdutos} na memória.
# Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
# a fim de garantir a unicidadde dos objetos.
cache = {}.copy()

# Prefixo dos identificadores de produtos.
letra_tb = "P"

# Descrição das colunas da tabela na base de dados.
colunas = \
  (
    ( 'descr_curta', type("foo"), 'TEXT',    False,    1,         80 ), # Descricao curta do produto.
    ( 'descr_media', type("foo"), 'TEXT',    False,   10,        250 ), # Descricao media do produto.
    ( 'descr_longa', type("foo"), 'TEXT',    False,   10,       3000 ), # Descricao longa do produto.
    ( 'unidade',     type("foo"), 'TEXT',    False,    1,         20 ), # Unidade de venda ('metro', 'caixa', 'peça', etc.).
    ( 'preco',       type(10.5),  'FLOAT',   False,    1,  999999.99 ), # Preco unitário do produto em reais.
    ( 'imagem',      type("foo"), 'TEXT',    False,    5,         50 ), # Nome do arquivo da imagem no diretorio 'imagens'.
    ( 'estoque',     type(10),    'INTEGER', False,    0,   99999999 )  # Estoque do produto  

  )

# Quando {True}, mostra comandos e resultados em {stderr}. 
diags = False

# Definição interna da classe {ObjUsuario}:
class ObjProduto_IMP():
  def __init__(self, id_produto, atrs):
    self.atrs = atrs.copy()
    self.id_produto = id_produto

# Implementação das funções:

# Inicializa a tabela de produtos dada as informaçoes globais
# Caso seja passada a variavel limpa como TRUE, a tabela é limpa.
def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
    
# Cria a tabela com os atributos passados pela variavel atributo
def cria(atrs):
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "produto_IMP.cria(" + str(atrs) + ") ...")
  
  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, tabelas.obj_para_indice)
  
  # Insere na base de dados e obtém o índice na mesma:
  prod = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(prod) is produto.ObjProduto:
    erro_prog("resultado de tipo inesperado = " + str(prod))
  return prod

# Retorna identificador do produto prod
def obtem_identificador(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.id_produto

# Obtem indice de um produto na tabela
def obtem_indice(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return identificador.para_indice(letra_tb, prod.id_produto)

# Retorna o custo de um produto na tabela
def obtem_preco(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.atrs['preco']

# Obtem a lista de atributos: desc_curta, desc_media, desc_longa
# unidade, preco, imagem e estoque de um produto especifico
def obtem_atributos(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.atrs.copy()

# Calcula o valor dos produtos a serem retirados do estoque e colocados
# no carrinho.
def calcula_preco(prod, qt):
  return prod.atrs['preco'] * qt

# Modifica determinados atributos de um produto na tabela
def muda_atributos(prod, mods):
  global cache, nome_tb, letra_tb, colunas, diags
  # Converte valores de formato memória para formato SQL. 
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice)
  
  # Modifica atributos na tabela e na memória:
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, prod.id_produto, mods_SQL)
  if res != prod:
    erro_prog("resultado inesperado = " + str(res))
  return

# Dado um id, retorna o produto associado a ele
def busca_por_identificador(id_produto):
  global cache, nome_tb, letra_tb, colunas, diags
  prod = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_produto)
  return prod

# Dado um indice, retorna o usuario associado a ele
def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas, diags
  usr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return usr

# Dado uma palavra, procura e retorna produtos que possuam essa palavra em
# sua descricao curta ou media.
def busca_por_palavra(pal):
  chaves = ('descr_curta', 'descr_media')
  valores = (pal,)
  produtos =  tabela_generica.busca_por_semelhanca(nome_tb, letra_tb, colunas, chaves, valores)
  return produtos

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      {
        'descr_curta': "Escovador de ouriço",
        'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
        'descr_longa': "Fabricante: Ouricex LTD<br/>\nOrigem: Cochinchina<br/>\nModelo: EO-22<br/>\nTensão: 110-230 V<br/>\nPotência: 1500 W<br/>\nAcessórios: cabo de força de 50 m, 10 pentes finos, 10 pentes grossos, valise em ABS<br/>\nDimensões: 300 x 200 x 3000 mm",
        'preco': float(120.50),
        'imagem': '155951.png',
        'estoque': 500,
        'unidade': '1 aparelho',
      },
      {
        'descr_curta': "Furadeira telepática (x 2)",
        'descr_media': "Kit com duas furadeiras telepáticas 700 W para canos de até 2 polegadas com acoplador para guarda-chuva e cabo de força",
        'descr_longa': "Fabricante: Ferramentas Tres Dedos SA<br/>\nOrigem: Brasil<br/>\nModelo: FT7T<br/>\nTensão: insuportável<br/>\nPotência: 700 W<br/>\nMaterial: Alumínio, policarbonato, chiclete.<br/>\nAcessórios: 1 acoplador para guarda-chuvas, 1 jogo de 5 pedais, cabo de força de 2 m.<br/>\nDimensões: 150 x 400 x 250 mm",
        'preco': float(420.00),
        'imagem': '156931.png',
        'estoque': 500,
        'unidade': 'caixa de 2'
      },
      {
        'descr_curta': "Luva com 8 dedos",
        'descr_media': "Luva para mão esquerda com 8 dedos, em camurça, com forro de bom-bril",
        'descr_longa': "Fabricante: United Trash Inc.<br/>\nOrigem: USA<br/>\nModelo: 8-EB<br/>\nNormas: ANSI 2345, ABNT 2019-857<br/>\nMaterial: Camurça artificial 1 mm, lã de aço.<br/>\nTamanho: G<br/>\nPeso: 120 g",
        'preco': float(19.95),
        'imagem': '160519.png',
        'estoque': 500,
        'unidade': '1 unidade'
      },
      {
        'descr_curta': "Ferroada",
        'descr_media': "Espada élfica forjada na cidade de Gondolin.",
        'descr_longa': "Fabricante: Gondolin Ferreiros SA\nOrigem: Gondolin\Dono Original: Bilbo\n",
        'preco': 2000.00,
        'imagem': '170859.png',
        'estoque': 500,
        'unidade': '1 espada' 
      }
    ]
  for atrs in lista_atrs:
    prod = cria(atrs)
    assert prod != None and type(prod) is produto.ObjProduto
  return

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
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "produto_IMP.def_obj(" + str(obj) + ", " + id_produto + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = produto.ObjProduto(id_produto, atrs_mem)
  else:
    assert obj.id_produto == id_produto
    # Converte atributos para formato na memória.
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    if diags: mostra(2, "modificando objeto, mods_mem = " + str(mods_mem))
    if len(mods_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      obj.atrs[chave] = val
  if diags: mostra(2, "obj = " + str(obj))
  return obj


def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return
