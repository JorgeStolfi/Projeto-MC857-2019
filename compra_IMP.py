# Implementação do módulo {compra} e da classe {ObjCompra}.

import compra
import usuario
import produto
import itens_de_compras
import tabelas
import tabela_generica
import base_sql
import conversao_sql
import identificador
import sys # Para diagnóstico.
from utils_testes import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjCompra} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "compras"

  # Nome das tabelas na base de dados.

letra_tb = "C"

colunas = None
  # Descrição das colunas da tabela de compras na base de dados.

# Como a base SQL não permite listas em campos, os itens de uma compra
# são armazenados em disco em uma tabelas separada da base SQL,
# "items_de_compra". Cada item de cada pedido de compra no sistema é
# representado por uma linha nesta tabela. Cada linha desta tablea tem
# um índice inteiro (chave primária) distinto, que é atribuído quando a
# linha é criada. Cada linha também tem um identificador de item de
# compra, uma string da forma "I-{NNNNNNNN}" onde {NNNNNNNN} é o índice
# formatado em 8 algarismos.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {ObjCompra}:

class ObjCompra_IMP:
  def __init__(self, id_compra, atrs, itens):
    global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
    self.id_compra = id_compra
    self.atrs = atrs # Inclui cliente e status
    self.itens = itens.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  colunas = \
    ( ( 'status',  type("foo"),         'TEXT',    False,    4,   10 ), # status da compra: 'aberto', 'pagando', 'pago', etc..
      ( 'cliente', usuario.ObjUsuario,  'INTEGER', False,   14,   14 ), # Objeto/índice do cliente que realizou a compra.
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
  itens_de_compras.inicializa(limpa)
  return

def cria(cliente):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  atrs = { 'cliente': cliente, 'status': 'aberto' }

  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, tabelas.obj_para_indice)

  # Insere na base de dados e obtém o índice na mesma:
  cpr = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(cpr) is compra.ObjCompra:
    erro_prog("resultado de tipo inválido = " + str(cpr))

  # Como a lista de itens começa vazia, não precisa inserir nada na base de itens.
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  return cpr.id_compra

def obtem_indice(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  return identificador.para_indice(letra_tb, cpr.id_compra)

def obtem_atributos(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  return cpr.atrs.copy()

def obtem_cliente(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  return cpr.atrs['cliente']

def obtem_status(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  return cpr.atrs["status"]

def obtem_itens(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  return cpr.itens.copy()

def obtem_quantidade(cpr, prod):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  # Procura o produto na lista, obtendo {qt_velho}:
  pos = itens_de_compras.posicao_do_item(prod, cpr.itens)
  if pos == None:
    return 0.0
  else:
    return cpr.itens[pos][1]

def obtem_preco(cpr, prod):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  # Procura o produto na lista, obtendo {qt_velho}:
  pos = itens_de_compras.posicao_do_item(prod, cpr.itens)
  if pos == None:
    return 0.0
  else:
    return cpr.itens[pos][2]

def muda_atributos(cpr, mods):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags

  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice)

  # Modifica atributos na tabela e na memória, menos os itens:
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, cpr.id_compra, mods_SQL)
  if res != cpr:
    erro_prog("resultado inesperado = " + str(res))
  return

def calcula_total(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  total = 0
  for prod, qt, prc in cpr.itens:
    total += prc
  return total

def fecha_compra(cpr):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  status = obtem_status(cpr)
  if status == 'aberto':
    cpr.status = 'pagando'
    mods = { 'status': cpr.status }
    muda_atributos(cpr,mods)

def acrescenta_item(cpr, prod, qt):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags

  # !!! Deve dar erro de programa se a compra não está aberta. !!!
  assert qt >= 0.0
  qt_velho = obtem_quantidade(cpr, prod)
  qt_novo = qt_velho + qt
  id_compra = compra.obtem_identificador(cpr)
  itens_de_compras.atualiza_lista(id_compra, cpr.itens, prod, qt_velho, qt_novo)
  return

def troca_quantidade(cpr, prod, qt):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags

  # !!! Deve dar erro de programa se a compra não está aberta. !!!
  assert qt >= 0.0
  qt_velho = obtem_quantidade(cpr, prod)
  qt_novo = qt
  id_compra = compra.obtem_identificador(cpr)
  itens_de_compras.atualiza_lista(id_compra, cpr.itens, prod, qt_velho, qt_novo)

def elimina_produto(cpr, prod):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags

  # !!! Deve dar erro de programa se a compra não está aberta. !!!
  qt_velho = obtem_quantidade(cpr, prod)
  if qt_velho == 0.0:
    erro_prog("produto " + produto.obtem_identificador(prod) + " não existe na compra " + str(cpr.id_compra))
  qt_novo = 0.0
  id_compra = compra.obtem_identificador(cpr)
  itens_de_compras.atualiza_lista(id_compra, cpr.itens, prod, qt_velho, qt_novo)

def busca_por_identificador(id_compra):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  cpr = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_compra)
  return cpr

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  cpr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return cpr

def busca_por_usuario(id_usuario):
  global cache, nome_tb, letra_tb, colunas, diags
  ind_usuario = identificador.para_indice(id_usuario)
  res = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, "usuario", ind_usuario)
  if res == None:
    # Não achou ninguém?
    return [].copy()
  elif type(res) is not list:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    return res

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  inicializa(True)
  # Identificador de usuários e identificadores de produtos de cada compra:
  lista_ups = \
    [
      ( "U-00000001", ( "P-00000001", "P-00000003", "P-00000002" ) ),
      ( "U-00000001", ( "P-00000002", "P-00000003" ) ),
      ( "U-00000002", ( ) )
    ]
  for id_usuario, ids_prods in lista_ups:
    usr = usuario.busca_por_identificador(id_usuario)
    cpr = cria(usr)
    assert cpr != None and type(cpr) is compra.ObjCompra
    qt = 1
    for id_produto in ids_prods:
      prod = produto.busca_por_identificador(id_produto)
      acrescenta_item(cpr, prod, qt)
      qt = qt*qt + 1
  return

# FUNÇÕES INTERNAS

def def_obj(obj, id_compra, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjCompra} com
  identificador {id_compra} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes.  Extrai a lista de itens da tabela
  correspondente, se houver.  O objeto *não* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {ObjCompra}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.  A lista de itens não ser alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  if diags: mostra(0, "produto_IMP.def_obj(" + str(obj) + ", " + id_compra + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.indice_para_obj)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    itens = itens_de_compras.busca_por_compra(id_compra)
    obj = compra.ObjCompra(id_compra, atrs_mem, itens)
  else:
    assert obj.id_compra == id_compra
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.indice_para_obj)
    if diags: mostra(2, "modificando objeto, mods_mem = " + str(mods_mem))
    if len(mods_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      if chave == 'cliente' and val != val_velho:
        erro_prog("campo '" + chave + "' não pode ser alterado")
      obj.atrs[chave] = val
  if diags: mostra(2, "obj = " + str(obj))
  return obj

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, letra_tb_itens, colunas_itens, diags
  diags = val
  return
