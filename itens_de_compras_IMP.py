# Implementação do módulo {itens_de_compras}.

import compra
import produto
import tabelas
import tabela_generica
import base_sql
import conversao_sql
import identificador
import sys # Para diagnóstico.
from utils_testes import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "itens_de_compras"

cache = {}.copy()

letra_tb = "I"

colunas = None
  # Descrição das colunas da tabela de ítens de compras na base de dados.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

class ObjItensDeCompras_IMP:

  def __init__(self, compra, atrs):
    global cache, nome_tb, letra_tb, colunas
    self.compra = compra
    self.atrs = atrs.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  colunas = \
    ( ( 'compra',  compra.ObjCompra,   'INTEGER', False ), # Objeto/índice da compra.
      ( 'produto', produto.ObjProduto, 'INTEGER', False ), # Objeto/índice do produto.
      ( 'qtd',     type(int),          'INTEGER', False ), # quantidade do produto referente.
      ( 'preco',   type(1.5),          'FLOAT',   False ), # preco do produto referente.
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def posicao_do_item(lit, prod):
  global cache, nome_tb, letra_tb, colunas, diags
  pos = 0
  for item in lit:
    if item[0] == prod:
      return pos
    pos = pos + 1
  return None

def busca_por_compra(id_compra):
  global cache, nome_tb, letra_tb, colunas, diags
  ind_compra = identificador.para_indice("C", id_compra)
  # Obtem lista de itens da compra:
  res_cols = ('produto', 'qtd', 'preco')
  lit_SQL = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, 'compra', ind_compra, res_cols)
  # Converte para lista de itens na memória:
  lit_mem = [].copy()
  for it_SQL in lit_SQL:
    assert ((type(it_SQL) is list) or (type(it_SQL) is tuple))  and (len(it_SQL) == 3);
    prod = produto.busca_por_indice(it_SQL[0])
    qtd = float(it_SQL[1])
    preco = float(it_SQL[2])
    it_mem = (prod, qtd, preco)
    lit_mem.append(it_mem)
  return lit_mem

def busca_por_produto(id_produto):
  global cache, nome_tb, letra_tb, colunas, diags
  ind_produto = identificador.para_indice("P", id_produto)
  # Obtem lista de itens do produto:
  res_cols = ('compra', 'qtd', 'preco')
  lit_SQL = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, "produto", ind_produto, res_cols)
  # Converte para lista de itens na memória:
  lit_mem = [].copy()
  for it_SQL in lit_SQL:
    assert ((type(it_SQL) is list) or (type(it_SQL) is tuple))  and (len(it_SQL) == 3);
    cpr = compra.busca_por_indice(it_SQL[0])
    qtd = float(it_SQL[1])
    preco = float(it_SQL[2])
    it_mem = (cpr, qtd, preco)
    lit_mem.append(it_mem)
  return lit_mem

def busca_por_identificador(id_compra):
  global cache, nome_tb, letra_tb, colunas, diags
  cpr = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_compra)
  return cpr

def atualiza_lista(id_compra, lit, prod, qtd_velho, qtd_novo):
  global cache, nome_tb, letra_tb, colunas, diags

  ind_compra = identificador.para_indice("C", id_compra)
  ind_produto = produto.obtem_indice(prod)
  if diags: mostra(2, "itens originais = " + str(lit))
  if qtd_velho == 0 and qtd_novo != 0:
    # Acrescenta a linha:
    preco_novo = produto.calcula_preco(prod, qtd_novo)
    lit.append((prod, qtd_novo, preco_novo))
    atrs_SQL = { 'compra': ind_compra, 'produto': ind_produto, 'qtd': qtd_novo, 'preco': preco_novo }
    base_sql.executa_comando_INSERT(nome_tb, atrs_SQL)
  else:
    # O produto existe na lista.
    # Determina indice {pos} do produto na lista:
    pos = posicao_do_item(lit, prod)
    assert pos != None
    cond = "compra = " + str(ind_compra) + " AND produto = " + str(produto.obtem_indice(prod))
    if qtd_novo == 0 and pos != None:
      # Elimina a linha:
      del lit[pos]
      base_sql.executa_comando_DELETE(nome_tb, cond)
    else:
      # Modifica a linha:
      preco_novo = produto.calcula_preco(prod, qtd_novo)
      lit[pos] = (prod, qtd_novo, preco_novo)
      atrs_SQL = { 'qtd': qtd_novo, 'preco': preco_novo }
      base_sql.executa_comando_UPDATE(nome_tb, cond, atrs_SQL)
  if diags: mostra(2, "itens alterados = " + str(lit))
  return

def obtem_quantidade(lit, prod):
  global cache, nome_tb, letra_tb, colunas, diags
  pos = posicao_do_item(lit, prod)
  if pos == None:
    return 0.0
  else:
    return lit[pos][1]

def obtem_preco(lit, prod):
  global cache, nome_tb, letra_tb, colunas, diags
  pos = posicao_do_item(lit, prod)
  if pos == None:
    return 0.0
  else:
    return lit[pos][2]

def calcula_total(lit):
  global cache, nome_tb, letra_tb, colunas, diags
  total = 0
  for prod, qtd, prc in lit:
    total += prc
  return total

# FUNÇÕES INTERNAS

def def_obj(obj, id_item_compra, atrs_SQL):

  """Se {obj} for {None}, cria um novo objeto da classe {ObjUsuario} com
  identificador {id_usuario} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {ObjUsuario}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"itens_de_compra_IMP.def_obj(" + str(obj) + ", " + id_item_compra + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    obj = cria_obj(id_item_compra, atrs_SQL)
  else:
    assert obj.compra == id_item_compra
    modifica_obj(obj, atrs_SQL)
  if diags: mostra(2,"obj = " + str(obj))
  return obj
    
def cria_obj(id_compra, atrs_SQL):
  """Cria um novo objeto da classe {ObjItensDeCompras} com
  identificador {id_compra} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.obj_para_indice)
  if diags: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
  assert type(atrs_mem) is dict
  if len(atrs_mem) != len(colunas):
    erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(colunas)))

  # Paranóia: verifica de novo a unicidade de CPF e email:
  for chave in ('compra', 'produto'):
    if chave not in atrs_mem:
      erro_prog("falta atributo '" + chave + "'")
    else:
      val = atrs_mem[chave]
      id_bus = busca_por_campo_unico(chave, val);
      if id_bus != None:
        erro_prog("itens de produtos com '" + chave + "' = '" + val + "' já existe: " + id_compra + " " + id_bus)
    
  obj = itens_de_compras.ObjItensDeCompras(id_compra, atrs_mem)
  return obj
  
def modifica_obj(obj, atrs_SQL):
  """O parâmetro {obj} deve ser um objeto da classe {ObjItensDeCompras}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.

  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte atributos para formato na memória. Pode ser subconjunto:
  mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.obj_para_indice)
  if diags: mostra(2,"modificando objeto, mods_mem = " + str(mods_mem))
  assert type(mods_mem) is dict
  if len(mods_mem) > len(colunas):
    erro_prog("numero de atributos a alterar = " + str(len(mods_mem)) + " excessivo")

  # Paranóia: verifica de novo a unicidade de CPF e email:
  for chave in ('CPF', 'email'):
    if chave in mods_mem:
      val = mods_mem[chave]
      id_bus = busca_por_campo_unico(chave, val);
      if id_bus != None and id_bus != obj.id_usuario:
        erro_prog("usuário com '" + chave + "' = '" + val + "' já existe: " + id_usuario + " " + id_bus)

  # Modifica os atributos:
  for chave, val in mods_mem.items():
    if not chave in obj.atrs:
      erro_prog("chave '" + chave + "' inválida")
    val_velho = obj.atrs[chave]
    if val != None and val_velho != None and (not type(val_velho) is type(val)):
      erro_prog("tipo do campo '" + chave + "' incorreto")
    obj.atrs[chave] = val
  return obj

def busca_por_campo_unico(chave, val):
  """Função interna: procura itens de compras cujo atributo {chave}
  tem valor {val}, supondo que ele é único. Se
  encontrar, devolve o identificador desse item de compra,
  senão devolve {None}"""
  global cache, nome_tb, letra_tb, colunas, diags
  res = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, chave, val, None)
  if res == None:
    # Não achou ninguém?
    return None
  elif (type(res) is list or type(res) is tuple) and len(res) == 0:
    # Não achou ninguém:
    return None
  elif type(res) is str:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    if len(res) != 1:
      erro_prog("campo '" + chave + "' val = '" + str(val) + "' duplicado - res = " + str(res))
    compra = res[0];
    return compra

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return
