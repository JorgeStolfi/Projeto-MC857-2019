# Implementação do módulo {compra} e da classe {ObjCompra}.

import tabela_generica
import base_sql
import identificador
import compra
import usuario
import sys # Para diagnóstico.
import produto

# VARIÁVEIS GLOBAIS DO MÓDULO

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjCompra} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb_compras = "compras"

  # Nome das tabelas na base de dados.
  
letra_tb_compras = "C"

colunas_compras = None
  # Descrição das colunas da tabela de compras na base de dados.

# Como a base SQL não permite listas em campos, os itens de uma compra são armazenados em disco
# em uma tabelas separada da base SQL, "items_de_compra".  Cada item de cada pedido de compra no sistema 
# é representado por uma linha nesta tabela. Cada linha desta tablea 
# tem um índice inteiro (chave primária) distinto, que é atribuído
# quando a linha é criada.  Neste sistema, esse índice é manipulado na forma de 
# um identificador de item de compra, uma string da forma "I-{NNNNNNNN}"
# onde {NNNNNNNN} é o índice formatado em 8 algarismos.

nome_tb_itens = "itens_de_compras"

letra_tb_itens = "I"

colunas_itens = None
  # Descrição das colunas da tabela de ítens de compras na base de dados.


# Definição interna da classe {ObjCompra}:

class ObjCompra_IMP:
  def __init__(self, id_compra, atrs):
    global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
    self.id_compra = id_compra
    self.atrs = atrs # Inclui cliente, status, e lista de itens

# Implementações:

def inicializa(limpa):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  colunas_compras = \
    ( ( 'status',  type("foo"),         'TEXT',    False,    4,   10 ), # status da compra: 'aberto', 'pagando', 'pago', etc..
      ( 'cliente', usuario.ObjUsuario,  'INTEGER', False,   14,   14 ), # Objeto/índice do cliente que realizou a compra.
      #( 'itens',   type([1,2]),         None,      None,  None, None ), # Lista dos itens da compra.
    )
  colunas_itens = \
    ( ( 'compra',  compra.ObjCompra,   'INTEGER', False, 10,         10 ), # Objeto/índice da compra.
      ( 'produto', produto.ObjProduto, 'INTEGER', False, 10,         10 ), # Objeto/índice do produto.
      ( 'qt',      type(int),          'INTEGER', False,  0 ,    999999 ), # quantidade do produto referente.
      ( 'preco',   type(1.5),          'FLOAT',   False,  0 , 999999.99 ), # preco do produto referente.
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb_compras, colunas_compras)
    tabela_generica.limpa_tabela(nome_tb_itens, colunas_itens)
  else:
    tabela_generica.cria_tabela(nome_tb_compras, colunas_compras)
    tabela_generica.cria_tabela(nome_tb_itens, colunas_itens)

def cria(usr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  atrs = { 'cliente': usr, 'status': 'aberto', 'itens': [].copy() }
  
  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas_compras, tabelas.obj_para_indice)

  # Insere na base de dados e obtém o índice na mesma:
  cpr = tabela_generica.acrescenta(nome_tb_compras, cache, letra_tb_compras, colunas_compras, def_obj, atrs_SQL)
  if not type(cpr) is compra.ObjCompra:
    sys.stderr.write("compra_IMP.cria: ** erro: " + str(cpr) + "\n")
    assert False

  # Não precisa inserir nada na base de itens.
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.id_compra

def obtem_indice(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return identificador.para_indice(letra_tb_compras, prod.id_compra)

def obtem_usuario(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.atrs['cliente']

def obtem_status(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.atributos["status"]

def obtem_itens(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.atrs['itens'].copy()
  
def obtem_quantidade(cpr, prod):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  # Procura o produto na lista, obtendo {qt_velho}:
  qt = 0.0
  for item in cpr.atrs['itens']:
    if item[0] == prod:
      qt = item[1]
      break
  return qt

def muda_atributos(cpr, mods):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  
  if 'itens' in mods:
    sys.stderr.write("compra_IMP.muda_atributos: **erro atributo 'itens' não pode ser alterado\n")
    assert False
  
  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas_compras, tabelas.obj_para_indice)
  
  # Modifica atributos na tabela e na memória, menos os itens:
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb_compras, colunas_tb_compras, def_obj, cpr.id_produto, mods_SQL)
  if res != cpr:
    sys.stderr.write("compra_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def calcula_total(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  total = 0
  for prod, qt, prc in compra.itens:
    total += prc
  return total

def acrescenta_item(cpr, prod, qt):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  
  assert qt >= 0.0
  if qt == 0.0: return
  qt_velho = obtem_quantidade(cpr, prod)
  qt_novo = qt_velho + qt
  atualiza_lista_de_itens(cpr, prod, qt_velho, qt_novo)
  return

def troca_quantidade(cpr, prod, qt):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  assert qt >= 0.0
  qt_velho = obtem_quantidade(cpr, prod)
  qt_novo = qt
  if qt_velho == qt_novo: return
  atualiza_lista_de_itens(cpr, prod, qt_velho, qt_novo)

def elimina_prod(cpr, prod):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  qt_velho = obtem_quantidade(cpr, prod)
  if qt_velho == 0.0:
    sys.stderr.write("** produto " + produto.obtem_identificador(prod) + " não existe na compra " + str(cpr.id_compra) + "\n")
    assert False 
  qt_novo = 0.0
  atualiza_lista_de_itens(cpr, prod, qt_velho, qt_novo)
  
def fecha_compra(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  status = obtem_status(cpr)
  if status == 'aberto':
    cpr.status = 'pagando'
    mods = {'status': cpr.status}
    muda_atributos(cpr,mods)
  

# FUNÇÕES INTERNAS

def atualiza_lista_de_itens(cpr, prod, qt_velho, qt_novo, preco_novo):
  """Atualiza a lista de itens do objeto {cpr}, trocando a quantidade do produto {prod}
  do valor atual {qt_velho} para {qt_novo}, e recalculando o preço. Também atualiza a
  tabela de itens na base SQL.
  
  Se {qt_novo} e {qt_velho} são ambos zero, não faz nada.  Senão, se {qt_velho} é zero, 
  supõe que o produto não existe nem na lista nem na tabela, e acrescenta o mesmo 
  a ambas. Senão, se {qt_novo} é zero, supõe 
  que o produto existe na lista e na tabela, e elimina o mesma de ambas."""
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens

  ind_compra = obtem_indice(cpr)
  ind_produto = produto.obtem_indice(prod)
  preco_novo = produto.calcula_preco(prod, qt_novo)
  if qt_velho == 0 and qt_novo == 0:
    return
  elif qt_velho == 0:
    # Acrescenta a linha:
    cpr.atrs['itens'].append((prod, qt_novo, preco_novo))
    atrs_SQL = { 'compra': ind_compra, 'produto': ind_produto, 'qt': qt_novo, 'preco': preco_novo }
    base_sql.executa_comando_INSERT(nome_tb_itens, atrs_SQL)
  else:
    # Determina indice {pos} do produto na lista:
    itens = cpr.atrs['itens']
    pos = None
    for k in range(len(itens)):
      el = itens[k]
      if el[0] == prod:
        pos = k
        break
    cond = "compra = " + str(obtem_indice(cpr)) + " AND produto = " + str(produto.obtem_indice(prod))
    if qt_novo == 0 and pos != None:
      # Elimina a linha:
      del itens[pos]
      base_sql.executa_comando_DELETE(nome_tb_itens, cond)
    else:
      # Modifica a linha:
      itens[pos] = (prod, qt_novo, preco_novo)
      atrs_SQL = { 'qt': qt_novo, 'preco': preco_novo }
      executa_comando_UPDATE(nome_tb_itens, cond, atrs_SQL)
  return
