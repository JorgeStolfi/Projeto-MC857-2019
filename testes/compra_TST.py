#! /usr/bin/python3

import compra
import usuario
import produto
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
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela, criando usuários de teste:\n")
usuario.cria_testes()

sys.stderr.write("Inicializando módulo {produto}, limpando tabela, criando produtos de teste:\n")
produto.cria_testes()

sys.stderr.write("Inicializando módulo {compra}, limpando tabela:\n")
compra.inicializa(True)

# ----------------------------------------------------------------------
sys.stderr.write("Obtendo usuários para teste:\n")
uindice1 = 1
uident1 = "U-00000001"
usr1 = usuario.busca_por_identificador(uident1)

uindice2 = 2
uident2 = "U-00000002"
usr2 = usuario.busca_por_identificador(uident2)

# ----------------------------------------------------------------------
sys.stderr.write("Obtendo produtos para teste:\n")

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

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_compra(rotulo, cpr, indice, ident, atrs, itens, ctot):
  """Testes básicos de consistência do objeto {cpr} da classe {ObjCompra}, dados {indice},
  {ident}, {atrs}, e preço total {ctot} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando compra %s\n" % rotulo)
  ok = utils_testes.verifica_objeto(compra, compra.ObjCompra, cpr, indice, ident, atrs)

  if cpr != None and type(cpr) is compra.ObjCompra:
  
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {obtem_cliente()}:\n")
    usr_cmp = compra.obtem_cliente(cpr)
    usr_esp = atrs['cliente']
    if usr_cmp != usr_esp:
      aviso_prog("retornou " + str(usr_cmp) + ", deveria ter retornado " + str(usr_esp),True)
      ok = False
    
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {obtem_status()}:\n")
    stat_cmp = compra.obtem_status(cpr)
    stat_esp = atrs['status']
    if stat_cmp != stat_esp:
      aviso_prog("retornou " + str(stat_cmp) + ", deveria ter retornado " + str(stat_esp),True)
      ok = False
    
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {obtem_itens()}:\n")
    its_cmp = compra.obtem_itens(cpr)
    its_esp = itens
    if its_cmp != its_esp:
      aviso_prog("retornou " + str(its_cmp) + ", deveria ter retornado " + str(its_esp),True)
      ok = False
    
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {calcula_total()}:\n")
    ctot_cmp = compra.calcula_total(cpr)
    if ctot_cmp != ctot:
      aviso_prog("retornou " + str(ctot_cmp) + ", deveria ter retornado " + str(ctot),True)
      ok = False

  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return
 
def testa_cria_compra(rotulo, indice, ident, cliente):
  """Testa criação de pedido de compra cliente {cliente}. Retorna o pedido de compra."""
  global ok_global
  # Cria o objeto inicialmente com status aberto e sem itens:
  cpr = compra.cria(cliente)
  ender = usuario.obtem_atributos(cliente)['endereco']
  CEP = usuario.obtem_atributos(cliente)['CEP']
  atrs_ini = { 'cliente': cliente, 'status': 'aberto', 'endereco': ender, 'CEP': CEP }
  itens_ini = [].copy()
  ctot_ini = 0.0
  verifica_compra(rotulo, cpr, indice, ident, atrs_ini, itens_ini, ctot_ini)
  return cpr
  
def testa_quantidade(rotulo, cpr, prod, qtd_esp, preco_esp):
  """Verifica se a quantidade de {prod} em {cpr} foi alterada para {qtd_esp}."""
  global ok_global
  sys.stderr.write("%s\n" % ("-" * 70))
  ok = True # Este teste deu certo?
  assert qtd_esp >= 0
  id_compra = compra.obtem_identificador(cpr)
  id_produto = produto.obtem_identificador(prod)
  sys.stderr.write("  compra = " + id_compra + " produto = " + id_produto + " qtd_esp = " + str(qtd_esp) + "\n")

  # ----------------------------------------------------------------------
  sys.stderr.write("testando {compra.obtem_quantidade}:\n")
  qtd_cmp = compra.obtem_quantidade(cpr, prod)
  if abs(qtd_cmp - qtd_esp) >= 0.001:
    aviso_prog("{compra.obtem_quantidade} é " + str(qtd_cmp) + ", deveria ser " + str(qtd_esp),True)
    ok = False

  # ----------------------------------------------------------------------
  sys.stderr.write("testando {compra.obtem_preco}:\n")
  preco_cmp = compra.obtem_preco(cpr, prod)
  if abs(preco_cmp - preco_esp) >= 0.001:
    aviso_prog("{compra.obtem_preco} é " + str(preco_cmp) + ", deveria ser " + str(preco_esp),True)
    ok = False
  preco_prd = produto.calcula_preco(prod, qtd)
  if abs(preco_cmp - preco_prd) >= 0.001:
    aviso_prog("{compra.obtem_preco} é " + str(preco_cmp) + ", deveria ser " + str(preco_prd),True)
    ok = False

  # ----------------------------------------------------------------------
  sys.stderr.write("testando produto em {compra.obtem_itens}:\n")
  itens_cmp = compra.obtem_itens(cpr)
  conta = 0 # Numero de vezes que o produto apareceu:
  for prod_it, qtd_it, preco_it in itens_cmp:
    if prod_it == prod:
      conta = conta + 1
      if qtd_esp == 0:
        aviso_prog("produto não deveria aparecer na compra, item = " + str(item),True)
        ok = False
      elif abs(qtd_it - qtd_esp) >= 0.001:
        aviso_prog("quantidade nos itens da compra é " + str(qtd_it) + ", deveria ser " + str(qtd_esp),True)
        ok = False
      if abs(preco_it - preco_esp) >= 0.001:
        aviso_prog("preço nos itens da compra é " + str(preco_it) + ", deveria ser " + str(preco_esp),True)
        ok = False
  conta_esp = (1 if qtd_esp != 0.0 else 0)
  if conta != conta_esp:
    aviso_prog("produto  ocorre na compra " + str(conta_cmp) + " vezes, deveria ser " + str(conta_esp),True)
    ok = False
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False
  sys.stderr.write("%s\n" % ("-" * 70))
  
# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.cria}:\n")
cindice1 = 1
cident1 = "C-00000001"
cusr1 = usr1
cpr1 = testa_cria_compra("cpr1", cindice1, cident1, cusr1)
cpr1_atrs = {
  'cliente': cusr1,
  'status': "aberto",
  'endereco': 'Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP', 
  'CEP': '13083-418'
}
cpr1_itens = [].copy()
ctot1 = 0.0

cindice2 = 2
cident2 = "C-00000002"
cusr2 = usr2
cpr2 = testa_cria_compra("cpr2", cindice2, cident2, cusr2)
cpr2_atrs = {
  'cliente': cusr2,
  'status': "aberto", 
  'endereco': "Avenida dos Semáforos, 1003\nJardim Pelado\nCampinas, SP", 
  'CEP': "13083-007"
}
cpr2_itens = [].copy()
ctot2 = 0.0

cindice3 = 3
cident3 = "C-00000003"
cusr3 = usr1
cpr3 = testa_cria_compra("cpr3", cindice3, cident3, cusr3)
cpr3_atrs = {
  'cliente': cusr3,
  'status': "aberto",
  'endereco': 'Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP', 
  'CEP': '13083-418'
}
cpr3_itens = [].copy()
ctot3 = 0.0

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.muda_atributos}:\n")

cpr1_mods = {
  'cliente': cusr1,
  'status': "despachada"
}
compra.muda_atributos(cpr1, cpr1_mods)
for k, v in cpr1_mods.items():
  cpr1_atrs[k] = v
verifica_compra("cpr1_d", cpr1, cindice1, cident1, cpr1_atrs, cpr1_itens, ctot1)

cpr2_mods = cpr2_atrs.copy()
compra.muda_atributos(cpr2, cpr2_mods) # Não deveria mudar os atributos
verifica_compra("cpr2", cpr2, cindice2, cident2, cpr2_atrs, cpr2_itens, ctot2)

cpr2_mods = cpr3_atrs.copy()
cpr2_mods['cliente'] = cpr2_atrs['cliente'] # Não pode alterar o cliente.
compra.muda_atributos(cpr2, cpr2_mods) # Deveria assumir os valores do cpr3
for k, v in cpr2_mods.items():
  cpr2_atrs[k] = v
verifica_compra("cpr2_m", cpr2, cindice2, cident2, cpr2_atrs, cpr2_itens, ctot2)

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.fecha_compra}:\n")

compra.fecha_compra(cpr3)
cpr3_atrs['status'] = "pagando"
verifica_compra("cpr3_m", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.acrescenta_item}:\n")

cpr3_itens = [ (prod1, 2, 2*preco1), (prod3, 3, 3*preco3), (prod2, 20, 20*preco2) ]
for prod, qtd, preco in cpr3_itens:
  compra.acrescenta_item(cpr3, prod, qtd)
ctot3 = 0.00
for prod, qtd, preco in cpr3_itens:
  testa_quantidade("+prod", cpr3, prod, qtd, preco)
  ctot3 = ctot3 + preco
verifica_compra("3prods", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)  

# Acrecenta a produto que já existe:
assert cpr3_itens[2][0] == prod2
qtd_old = cpr3_itens[2][1]
qtd_add = 10
qtd_new = qtd_old + qtd_add
compra.acrescenta_item(cpr3, prod2, qtd_add)
cpr3_itens[2] = (prod2, qtd_new, 420.00*qtd_new)
ctot3 = 0.00
for prod, qtd, preco in cpr3_itens:
  testa_quantidade("prod2:+10", cpr3, prod, qtd, preco)
  ctot3 = ctot3 + preco
verifica_compra("prod2:+10", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)  

# Acrescenta quantidade zero:
compra.acrescenta_item(cpr3, prod2, 0)
ctot3 = 0.00
for prod, qtd, preco in cpr3_itens:
  testa_quantidade("prod2:+0", cpr3, prod, qtd, preco)
  ctot3 = ctot3 + preco
verifica_compra("prod2:+0", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)  

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.troca_quantidade}:\n")

# Produto que existe:
assert cpr3_itens[0][0] == prod1
qtd_old = cpr3_itens[0][1]
qtd_new = 6
compra.troca_quantidade(cpr3, prod1, qtd_new)
cpr3_itens[0] = (prod1, qtd_new, 120.50*qtd_new)
ctot3 = 0.00
for prod, qtd, preco in cpr3_itens:
  testa_quantidade("prod2:+10", cpr3, prod, qtd, preco)
  ctot3 = ctot3 + preco
verifica_compra("prod1:=6", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)  

# Produto que não existe:
assert cpr2_itens == []
qtd_old = 0
qtd_new = 6
compra.troca_quantidade(cpr2, prod1, qtd_new)
cpr2_itens.append((prod1, qtd_new, 120.50*qtd_new))
ctot2 = 0.00
for prod, qtd, preco in cpr2_itens:
  testa_quantidade("prod1:=6", cpr2, prod, qtd, preco)
  ctot2 = ctot2 + preco
verifica_compra("prod1:=6", cpr2, cindice2, cident2, cpr2_atrs, cpr2_itens, ctot2)  

# Exliminando produto que existe:
assert cpr3_itens[1][0] == prod3
qtd_old = cpr3_itens[1][1]
qtd_new = 0
compra.troca_quantidade(cpr3, prod3, qtd_new)
del cpr3_itens[1]
ctot3 = 0.00
for prod, qtd, preco in cpr3_itens:
  testa_quantidade("prod3:=0", cpr3, prod, qtd, preco)
  ctot3 = ctot3 + preco
verifica_compra("prod1:=6", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)  

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.elimina_produto}:\n")

assert cpr3_itens[1][0] == prod2
qtd_old = cpr3_itens[1][1]
qtd_new = 0
compra.elimina_produto(cpr3, prod2)
del cpr3_itens[1]
ctot3 = 0.00
for prod, qtd, preco in cpr3_itens:
  testa_quantidade("prod2:elim", cpr3, prod, qtd, preco)
  ctot3 = ctot3 + preco
verifica_compra("prod1:=6", cpr3, cindice3, cident3, cpr3_atrs, cpr3_itens, ctot3)  

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
