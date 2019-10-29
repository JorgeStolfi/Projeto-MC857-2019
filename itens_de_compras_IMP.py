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

letra_tb = "I"

colunas = None
  # Descrição das colunas da tabela de ítens de compras na base de dados.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  colunas = \
    ( ( 'compra',  compra.ObjCompra,   'INTEGER', False, 10,         10 ), # Objeto/índice da compra.
      ( 'produto', produto.ObjProduto, 'INTEGER', False, 10,         10 ), # Objeto/índice do produto.
      ( 'qtd',     type(int),          'INTEGER', False,  0 ,    999999 ), # quantidade do produto referente.
      ( 'preco',   type(1.5),          'FLOAT',   False,  0 , 999999.99 ), # preco do produto referente.
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
  indice = identificador.para_indice("C", id_compra)
  # Obtem lista de identificadores de itens referentes a esta compra:
  cond = 'compra = ' + str(indice)
  nomes_cols = ('produto', 'qtd', 'preco')
  lit_SQL = base_sql.executa_comando_SELECT(nome_tb, cond, nomes_cols)
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
  indice = identificador.para_indice("P", id_produto)
  # Obtem lista de identificadores de itens referentes a esta compra:
  compras = tabela_generica.busca_por_campo("itens_de_compras", "I", "id_compra", "id_produto", indice)
  return compras

def atualiza_lista(id_compra, lit, prod, qtd_velho, qtd_novo):
  global cache, nome_tb, letra_tb, colunas, diags

  ind_compra = identificador.para_indice("C", id_compra)
  ind_produto = produto.obtem_indice(prod)
  if diags: mostra(2, "itens originais = " + str(lit));
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
  if diags: mostra(2, "itens alterados = " + str(lit));
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

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return
