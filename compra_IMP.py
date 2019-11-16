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
import frete
from utils_testes import erro_prog, mostra

import sys  # Para diagnóstico.

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
    global cache, nome_tb, letra_tb, colunas, diags
    self.id_compra = id_compra
    self.atrs = atrs  # Inclui cliente, status, CEP e endereço
    self.itens = itens.copy()


# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  colunas = \
    ( ( 'status',   type("foo"),         'TEXT',    False ), # status da compra: 'aberto', 'pagando', 'pago', etc..
      ( 'cliente',  usuario.ObjUsuario,  'INTEGER', False ), # Objeto/índice do cliente que realizou a compra.
      ( 'endereco', type("foo"),         'TEXT',    False ), # Endereço de entrega
      ( 'CEP',      type("foo"),         'TEXT',    False ), # CEP de entrega
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
  itens_de_compras.inicializa(limpa)
  return

def cria(cliente):
  global cache, nome_tb, letra_tb, colunas, diags
  
  endereco = usuario.obtem_atributos(cliente)['endereco']
  CEP = usuario.obtem_atributos(cliente)['CEP']
  atrs = {'cliente': cliente, 'status': 'aberto', 'endereco': endereco, 'CEP': CEP}

  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, False, tabelas.obj_para_indice)

  # Insere na base de dados e no cache:
  cpr = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  assert type(cpr) is compra.ObjCompra
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.id_compra

def obtem_indice(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return identificador.para_indice(letra_tb, cpr.id_compra)

def obtem_atributos(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.atrs.copy()

def obtem_cliente(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.atrs['cliente']

def obtem_status(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.atrs["status"]

def obtem_cep(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.atrs["CEP"]

def obtem_endereco(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.atrs["endereco"]

def obtem_itens(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return cpr.itens.copy()

def obtem_quantidade(cpr, prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return itens_de_compras.obtem_quantidade(cpr.itens, prod)

def obtem_preco(cpr, prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return itens_de_compras.obtem_preco(cpr.itens, prod)

def calcula_total(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  return itens_de_compras.calcula_total(cpr.itens)

def muda_atributos(cpr, mods):
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, True, tabelas.obj_para_indice)

  # Modifica atributos na tabela e na memória, menos os itens:
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, cpr.id_compra, mods_SQL)
  assert res == cpr
  return cpr

def fecha_compra(cpr):
  global cache, nome_tb, letra_tb, colunas, diags
  status = obtem_status(cpr)
  if status == 'aberto':
    cpr.status = 'pagando'
    mods = {'status': cpr.status}
    muda_atributos(cpr, mods)
  return

def modifica_status(cliente, novo_status):
  return muda_atributos(cliente, [status, novo_status])

def acrescenta_item(cpr, prod, qtd):
  global cache, nome_tb, letra_tb, colunas, diags

  # !!! Deve dar erro de programa se a compra não está aberta. !!!
  assert qtd >= 0.0
  qtd_velho = obtem_quantidade(cpr, prod)
  qtd_novo = qtd_velho + qtd
  id_compra = compra.obtem_identificador(cpr)
  itens_de_compras.atualiza_lista(id_compra, cpr.itens, prod, qtd_velho, qtd_novo)
  return

def troca_quantidade(cpr, prod, qtd):
  global cache, nome_tb, letra_tb, colunas, diags

  # !!! Deve dar erro de programa se a compra não está aberta. !!!
  assert qtd >= 0.0
  qtd_velho = obtem_quantidade(cpr, prod)
  qtd_novo = qtd
  id_compra = compra.obtem_identificador(cpr)
  itens_de_compras.atualiza_lista(id_compra, cpr.itens, prod, qtd_velho, qtd_novo)

def elimina_produto(cpr, prod):
  global cache, nome_tb, letra_tb, colunas, diags

  # !!! Deve dar erro de programa se a compra não está aberta. !!!
  qtd_velho = obtem_quantidade(cpr, prod)
  if qtd_velho == 0.0:
      erro_prog("produto " + produto.obtem_identificador(prod) + " não existe na compra " + str(cpr.id_compra))
  qtd_novo = 0.0
  id_compra = compra.obtem_identificador(cpr)
  itens_de_compras.atualiza_lista(id_compra, cpr.itens, prod, qtd_velho, qtd_novo)

def busca_por_identificador(id_compra):
  global cache, nome_tb, letra_tb, colunas, diags
  cpr = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_compra)
  return cpr

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas, diags
  cpr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return cpr

def busca_por_produto(id_produto):
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! Furada! A tabela de compras NÃO tem os itens das compras. !!!
  cpr = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_produto)
  return cpr

def busca_por_usuario(id_usuario):
  global cache, nome_tb, letra_tb, colunas, diags
  ind_usuario = identificador.para_indice('U', id_usuario)
  res = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, "cliente", ind_usuario)
  if res is None:
    # Não achou ninguém?
    return [].copy()
  elif type(res) is not list:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    return res

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  
  # Identificador de usuários e identificadores de produtos de cada compra:
  lista_ups = \
    [
      ("U-00000001", ("P-00000001", "P-00000003", "P-00000002")),
      ("U-00000001", ("P-00000002", "P-00000003")),
      ("U-00000002", ( ))
    ]
  for id_usuario, ids_prods in lista_ups:
    usr = usuario.busca_por_identificador(id_usuario)
    cpr = cria(usr)
    assert cpr != None and type(cpr) is compra.ObjCompra
    qtd = 1
    for id_produto in ids_prods:
      prod = produto.busca_por_identificador(id_produto)
      acrescenta_item(cpr, prod, qtd)
      qtd = qtd * qtd + 1
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
  equivalentes na memória.
  
  Em caso de sucesso, retorna o objeto {obj}, dado ou criado. Se os parâmetros 
  forem inválidos ou incompletos, retorna uma ou mais mensagens
  de erro, na forma de uma lista de strings."""
  global cache, nome_tb, letra_tb, colunas, diags
  
  erros = [].copy()
  if diags: mostra(0, "produto_IMP.def_obj(" + str(obj) + ", " + id_compra + ", " + str(atrs_SQL) + ") ...")
  if obj is None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.indice_para_obj)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    itens = itens_de_compras.busca_por_compra(id_compra)
    obj = compra.ObjCompra(id_compra, atrs_mem, itens)
  else:
    assert obj.id_compra == id_compra
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.indice_para_obj)
    if diags: mostra(2, "modificando objeto, mods_mem = " + str(mods_mem))
    assert type(mods_mem) is dict
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
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

def calcular_frete(comp, CEP):
  # peso_total = 0
  # volume_total = 0
  # for item in compra.obtem_itens(comp):
  #   peso_total = peso_total + item.peso
  #   volume_total = volume_total + item.volume
  return frete.calcula(CEP, len(compra.obtem_itens(comp) ), len(compra.obtem_itens(comp)))
