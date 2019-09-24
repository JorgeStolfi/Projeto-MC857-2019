# Implementação do módulo {compra} e da classe {ObjCompra}.

import compra
import usuario
import produto
import tabelas
import tabela_generica
import base_sql
import conversao_sql
import identificador
import sys # Para diagnóstico.

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
      ( 'itens',   type([1,2]),         None,      None,  None, None ), # Lista dos itens da compra.
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

def cria(cliente):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  atrs = { 'cliente': cliente, 'status': 'aberto', 'itens': [].copy() }
  
  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas_compras, tabelas.obj_para_indice)
  
  # O atributo 'itens' não deve ir para a tabelas de compras:
  assert not ('itens' in atrs_SQL)

  # Insere na base de dados e obtém o índice na mesma:
  cpr = tabela_generica.acrescenta(nome_tb_compras, cache, letra_tb_compras, colunas_compras, def_obj, atrs_SQL)
  if not type(cpr) is compra.ObjCompra:
    sys.stderr.write("compra_IMP.cria: ** erro: " + str(cpr) + "\n")
    assert False

  # Como a lista de itens começa vazia, não precisa inserir nada na base de itens.
  return cpr

def obtem_identificador(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.id_compra

def obtem_indice(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return identificador.para_indice(letra_tb_compras, cpr.id_compra)

def obtem_atributos(cpr):
  global cache, nome_tb, letra_tb, colunas
  return cpr.atrs.copy()

def obtem_cliente(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.atrs['cliente']

def obtem_status(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  return cpr.atrs["status"]

def obtem_itens(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  itens = cpr.atrs['itens']
  return itens.copy()
  
def obtem_quantidade(cpr, prod):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  # Procura o produto na lista, obtendo {qt_velho}:
  itens = cpr.atrs['itens']
  pos = posicao_do_item(prod, itens) 
  if pos == None:
    return 0.0
  else:
    return itens[pos][1]

def obtem_preco(cpr, prod):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  # Procura o produto na lista, obtendo {qt_velho}:
  itens = cpr.atrs['itens']
  pos = posicao_do_item(prod, itens) 
  if pos == None:
    return 0.0
  else:
    return itens[pos][2]

def muda_atributos(cpr, mods):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  
  if 'itens' in mods:
    sys.stderr.write("compra_IMP.muda_atributos: **erro atributo 'itens' não pode ser alterado\n")
    assert False
  
  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas_compras, tabelas.obj_para_indice)
  
  # Modifica atributos na tabela e na memória, menos os itens:
  res = tabela_generica.atualiza(nome_tb_compras, cache, letra_tb_compras, colunas_compras, def_obj, cpr.id_compra, mods_SQL)
  if res != cpr:
    sys.stderr.write("compra_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def calcula_total(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  itens = cpr.atrs['itens']
  total = 0
  for prod, qt, prc in itens:
    total += prc
  return total
  
def fecha_compra(cpr):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  status = obtem_status(cpr)
  if status == 'aberto':
    cpr.status = 'pagando'
    mods = {'status': cpr.status}
    muda_atributos(cpr,mods)

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

def elimina_produto(cpr, prod):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  qt_velho = obtem_quantidade(cpr, prod)
  if qt_velho == 0.0:
    sys.stderr.write("** produto " + produto.obtem_identificador(prod) + " não existe na compra " + str(cpr.id_compra) + "\n")
    assert False 
  qt_novo = 0.0
  atualiza_lista_de_itens(cpr, prod, qt_velho, qt_novo)

def busca_por_identificador(id_compra):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  cpr = tabela_generica.busca_por_identificador(nome_tb_compras, cache, letra_tb_compras, colunas_compras, def_obj, id_compra)
  return cpr

def busca_por_indice(ind):
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  cpr = tabela_generica.busca_por_indice(nome_tb_compras, cache, letra_tb_compras, colunas_compras, def_obj, ind)
  return cpr

def cria_testes():
  global cache, nome_tb, letra_tb, colunas
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

def posicao_do_item(prod, itens):
  """Obtem o índice do item com produto {prod} na lista de itens da compra {itens}. Se não 
  existir, devolve {None}."""
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens
  pos = 0
  for item in itens:
    if item[0] == prod:
      return pos
    pos = pos + 1
  return None

def atualiza_lista_de_itens(cpr, prod, qt_velho, qt_novo):
  """Atualiza a lista de itens do objeto {cpr}, trocando a quantidade do produto {prod}
  do valor atual {qt_velho} para {qt_novo}, e recalculando o preço. Também atualiza a
  tabela de itens na base SQL.
  
  Se {qt_novo} for igual a {qt_velho}, não faz nada.  Senão, se {qt_velho} é zero, 
  supõe que o produto não existe nem na lista nem na tabela, e acrescenta o mesmo 
  a ambas. Senão, se {qt_novo} é zero, supõe 
  que o produto existe na lista e na tabela, e elimina o mesma de ambas."""
  global cache, nome_tb_compras, letra_tb_compras, colunas_compras, letra_tb_itens, colunas_itens

  ind_compra = obtem_indice(cpr)
  ind_produto = produto.obtem_indice(prod)
  itens = cpr.atrs['itens']
  sys.stderr.write("  itens originais = " + str(itens) + "\n");
  if qt_velho == qt_novo:
    return
  elif qt_velho == 0:
    # Acrescenta a linha:
    preco_novo = produto.calcula_preco(prod, qt_novo)
    itens.append((prod, qt_novo, preco_novo))
    atrs_SQL = { 'compra': ind_compra, 'produto': ind_produto, 'qt': qt_novo, 'preco': preco_novo }
    base_sql.executa_comando_INSERT(nome_tb_itens, atrs_SQL)
  else:
    # Determina indice {pos} do produto na lista:
    pos = posicao_do_item(prod, itens)
    assert pos != None
    cond = "compra = " + str(obtem_indice(cpr)) + " AND produto = " + str(produto.obtem_indice(prod))
    if qt_novo == 0 and pos != None:
      # Elimina a linha:
      del itens[pos]
      base_sql.executa_comando_DELETE(nome_tb_itens, cond)
    else:
      # Modifica a linha:
      preco_novo = produto.calcula_preco(prod, qt_novo)
      itens[pos] = (prod, qt_novo, preco_novo)
      atrs_SQL = { 'qt': qt_novo, 'preco': preco_novo }
      base_sql.executa_comando_UPDATE(nome_tb_itens, cond, atrs_SQL)
  sys.stderr.write("  itens alterados = " + str(cpr.atrs['itens']) + "\n");
  return

def def_obj(obj, id_compra, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjCompra} com
  identificador {id_compra} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes.  Extrai a lista de itens da tabela
  correspondente, se houver.  O objeto *não* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjCompra}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.  Estas modificações não podem incluir o atributo 'itens'.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas
  sys.stderr.write("produto_IMP.def_obj(" + str(obj) + ", " + id_compra + ", " + str(atrs_SQL) + ") ...\n")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas_compras, tabelas.indice_para_obj)
    sys.stderr.write("  criando objeto, atrs_mem = " + str(atrs_mem) + "\n")
    # O atributo 'itens' não deve estar na tabelas de compras:
    assert not ('itens' in atrs_mem)
    atrs_mem['itens'] = obtem_itens_da_tabela(id_compra)
    obj = compra.ObjCompra(id_compra, atrs_mem)
  else:
    assert obj.id_compra == id_compra
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas_compras, tabelas.indice_para_obj)
    sys.stderr.write("  modificando objeto, mods_mem = " + str(mods_mem) + "\n")
    # O atributo 'itens' não deve ser modificado desta forma:
    assert not ('itens' in mods_mem)
    if len(mods_mem) > len(obj.atrs):
      sys.stderr.write("  **erro: numero excessivo de atributos a alterar\n")
      assert False
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        sys.stderr.write("  **erro: chave '" + chave + "' inválida\n")
        assert False
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        sys.stderr.write("  **erro: tipo do campo '" + chave + "' incorreto\n")
        assert False
      if chave == 'cliente' and val != val_velho:
        sys.stderr.write("  **erro: campo '" + chave + "' não pode ser alterado\n")
        assert False
      obj.atrs[chave] = val
  sys.stderr.write("  obj = " + str(obj) + "\n")
  return obj

def obtem_itens_da_tabela(id_compra):
  """Extrai da tabela de itens de compras todas as entradas referente
  ao pedido com identificador {id_compra}.  Devolve uma lista de
  itens apropriada para o atributo 'itens' de um objeto {ObjCompra}."""
  indice = identificador.para_indice("C", id_compra)
  # Obtem lista de identificadores de itens referentes a esta compra:
  cond = 'compra = ' + str(indice)
  nomes_cols = ('produto', 'qt', 'preco')
  itens_SQL = base_sql.executa_comando_SELECT(nome_tb_itens, cond, nomes_cols)
  # Converte para lista de itens na memória:
  itens_mem = [].copy()
  for it_SQL in itens_SQL:
    assert ((type(it_SQL) is list) or (type(it_SQL) is tuple))  and (len(it_SQL) == 3);
    prod = produto.busca_por_indice(it_SQL[0])
    qt = float(it_SQL[1])
    preco = float(it_SQL[2])
    it_mem = (prod, qt, preco)
    itens_mem.append(it_mem)
  return itens_mem
