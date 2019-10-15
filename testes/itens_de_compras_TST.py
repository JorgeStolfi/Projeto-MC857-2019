#! /usr/bin/python3

import usuario
import produto
import compra
import itens_de_compras
import tabela_generica
import base_sql
import identificador
import utils_testes
import sys
from utils_testes import erro_prog, aviso_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB", None, None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
usuario.cria_testes()

indice1 = 1
uident1 = "U-00000001"
usr1 = usuario.busca_por_identificador(uident1)

indice2 = 2
uident2 = "U-00000002"
usr2 = usuario.busca_por_identificador(uident2)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {produto}, limpando tabela, criando produtos de teste:\n")
produto.cria_testes()

pindice1 = 1
pident1 = "P-00000001"
prod1 = produto.busca_por_identificador(pident1)
preco1 = produto.obtem_preco(prod1)

pindice2 = 2
pident2 = "P-00000002"
prod2 = produto.busca_por_identificador(pident2)
preco2 = produto.obtem_preco(prod2)

pindice3 = 3
pident3 = "P-00000003"
prod3 = produto.busca_por_identificador(pident3)
preco3 = produto.obtem_preco(prod3)

pindice4 = 4
pident4 = "P-00000004"
prod4 = produto.busca_por_identificador(pident4)
preco4 = produto.obtem_preco(prod4)

# ----------------------------------------------------------------------
# Dados de duas compras, sem criar o objeto:

cindice1 = 1
cident1 = "C-00000001"
citens1 = [].copy()
ctot1 = 0.0

cindice2 = 2
cident2 = "C-00000002"
citens2 = [].copy()
ctot2 = 0.0

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {itens_de_compras}, limpando tabela:\n")
itens_de_compras.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_itens_de_compras(rotulo, id_compra, lit_esp, ctot_esp):
  """Testes básicos de consistência da lista de itens do objeto {cpr} da classe {ObjCompra}, 
  dados a lista {lit_esp} de itens e o preço total {ctot_esp} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando lista de itens, teste %s\n" % rotulo)
  
  ok = True

  lit_cmp = itens_de_compras.busca_por_compra(id_compra)
  if lit_cmp == None or not (type(lit_cmp) is list or type(lit_cmp) is tuple):
    aviso_prog("retornou " + str(lit_cmp) + ", deveria ter retornado lista",True)
    ok = False
  elif lit_cmp != lit_esp:
    aviso_prog("retornou " + str(lit_cmp) + ", deveria ter retornado " + str(lit_esp), True)
    ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

def verifica_posicao_do_item(rotulo, lit, prod, pos_esp):
  """Verifica se {itens_de_compras.posicao_do_item(lit, prod)} devolve {pos_esp}."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando {posicao_do_item}, teste %s\n" % rotulo)

  ok = True

  pos_cmp = itens_de_compras.posicao_do_item(lit, prod)
  if pos_cmp != None and not (type(pos_cmp) is int):
    aviso_prog("retornou " + str(pos_cmp) + " " + str(type(pos_cmp)) + ", deveria ter retornado {None} ou {int}",True)
    ok = False
  elif pos_cmp != pos_esp:
    aviso_prog("retornou " + str(pos_cmp) + ", deveria ter retornado " + str(pos_esp),True)
    ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {itens_de_compras.posicao_do_item}:\n")

lit1 = [ (prod1, 10, 100, ), (prod3, 20, 30, ),  (prod2, 20, 30, ) ]
verifica_posicao_do_item("lit11", lit1, prod1, 0)
verifica_posicao_do_item("lit12", lit1, prod2, 2)
verifica_posicao_do_item("lit13", lit1, prod3, 1)
verifica_posicao_do_item("lit14", lit1, prod4, None)

# ----------------------------------------------------------------------
sys.stderr.write("testando {itens_de_compras.atualiza_lista}:\n")
 
# Acrescenta produto que não existe na compra 1:
qt11a = 15.0
prc11a = produto.calcula_preco(prod1, qt11a)
ctot11a = prc11a

itens_de_compras.atualiza_lista(cident1, citens1, prod1, 0.0, qt11a)

lit11a = [ (prod1, qt11a, prc11a, ), ]
verifica_itens_de_compras("11a", cident1, lit11a, ctot11a)
 
# Acrescenta produto que não existe na compra 2:
qt21a = 100.0
prc21a = produto.calcula_preco(prod1, qt21a)
ctot21a = prc21a

itens_de_compras.atualiza_lista(cident2, citens2, prod1, 0.0, qt21a)

lit21a = [ (prod1, qt21a, prc21a, ), ]
verifica_itens_de_compras("21a", cident2, lit21a, ctot21a)

# Acrescenta outro produto que não existe na compra 1:
qt12a = 25.0
prc12a = produto.calcula_preco(prod2, qt12a)
ctot12a = ctot11a + prc12a

itens_de_compras.atualiza_lista(cident1, citens1, prod2, 0.0, qt12a)

lit12a = lit11a + [ (prod2, qt12a, prc12a, ), ]
verifica_itens_de_compras("12a", cident1, lit12a, ctot12a)

# Modifica quantidade de produto que existe na compra 1:
qt11b = 30.0
prc11b = produto.calcula_preco(prod1, qt11b)
ctot11b = prc11b + prc12a

itens_de_compras.atualiza_lista(cident1, citens1, prod1, qt11a, qt11b)

lit11b = lit11a.copy();
lit11b[0] = (prod1, qt11b, prc11b,)
verifica_itens_de_compras("11b", cident1, lit11b, ctot11b)

# Elimina produto que existe na compra 1:
qt11c = 30.0
prc11c = produto.calcula_preco(prod1, qt11c)
ctot11c = prc11c + prc12a

itens_de_compras.atualiza_lista(cident1, citens1, prod1, qt11a, qt11c)

lit11c = lit11b.copy();
del lit11c[0]
verifica_itens_de_compras("11c", cident1, lit11c, ctot11c)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
