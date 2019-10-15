#! /usr/bin/python3

import produto
import tabela_generica
import base_sql
import identificador
import utils_testes
import sys
from utils_testes import erro_prog, mostra


# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {produto}, limpando tabela: \n")
produto.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_produto(rotulo, prod, indice, ident, atrs):
  """Testes básicos de consistência do obleto {prod} da classe {produto.ObjProduto}, dados {indice},
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando produto %s\n" % rotulo)
  ok = utils_testes.verifica_objeto(produto, produto.ObjProduto, prod, indice, ident, atrs)
  
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

def testa_cria_produto(rotulo, indice, ident, atrs):
  """Testa criação de produto com atributos com {atrs}. Retorna o produto."""
  prod = produto.cria(atrs)
  verifica_produto(rotulo, prod, indice, ident, atrs)
  return prod

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.cria}:\n")

prod1_atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex LTD\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nAcessórios: cabo de força de 50 m, 10 pentes finos, 10 pentes grossos, valise em ABS\nDimensões: 300 x 200 x 3000 mm",
  'preco': float(120.50),
  'imagem': '160519.png',
  'estoque': 500,
  'unidade': '1 aparelho'
}
pindice1 = 1
pident1 = "P-00000001"
prod1 = testa_cria_produto("prod1", pindice1, pident1, prod1_atrs)

prod2_atrs = {
  'descr_curta': "Furadeira telepática",
  'descr_media': "Duas furadeiras telepáticas 700 W para canos de até 2 polegadas com acoplador para guarda-chuva e cabo de força",
  'descr_longa': "Fabricante: Ferramentas Tres Dedos SA\nOrigem: Brasil\nModelo: FT7T\nTensão: insuportável\nPotência: 700 W\nMaterial: Alumínio, policarbonato, chiclete.\nAcessórios: 1 acoplador para guarda-chuvas, 1 jogo de 5 pedais, cabo de força de 2 m.\nDimensões: 150 x 400 x 250 mm",
  'preco': float(420.00),
  'imagem': '160519.png',
  'estoque': 500,
  'unidade': 'caixa de 2'
}
pindice2 = 2
pident2 = "P-00000002"
prod2 = testa_cria_produto("prod2", pindice2, pident2, prod2_atrs)

prod3_atrs = {
  'descr_curta': "Luva com 8 dedos",
  'descr_media': "Luva para mão esquerda com 8 dedos, em camurça, com forro de bom-bril",
  'descr_longa': "Fabricante: United Trash Inc.\nOrigem: USA\nModelo: 8-EB\nNormas: ANSI 2345, ABNT 2019-857\nMaterial: Camurça artificial 1 mm, lã de aço.\nTamanho: G\nPeso: 120 g",
  'preco': float(19.95),
  'imagem': '160519.png',
  'estoque': 500,
  'unidade': '1 unidade'
}
pindice3 = 3
pident3 = "P-00000003"
prod3 = testa_cria_produto("prod3", pindice3, pident3, prod3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.calcula_preco}:\n")

prod1_qt = 10.0
prod1_preco_un = prod1_atrs['preco']
prod1_preco_tot_esp = prod1_qt * prod1_preco_un
prod1_preco_tot_cmp = produto.calcula_preco(prod1, 10)
if prod1_preco_tot_cmp != prod1_preco_tot_esp:
  aviso_prog("resultado foi " + str(prod1_preco_tot_cmp) + " deveria ser " + str(prod1_preco_tot_esp),True)
  ok_global = False

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.muda_atributos}:\n")

prod1_mods = {
  'descr_curta': "Escovador de ouriço 2.0 Power Blaster",
  'preco': 1200.00,
}
produto.muda_atributos(prod1, prod1_mods)
prod1_b = produto.busca_por_identificador(pident1)
prod1_b_atrs = prod1_atrs
for k, v in prod1_mods.items():
  prod1_b_atrs[k] = v
verifica_produto("prod1_b",prod1,pindice1,pident1,prod1_b_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.busca_por_palavra}:\n")

palavra = "de força"
plist5_cmp = produto.busca_por_palavra(palavra)
sys.stderr.write("  resultado = " + str(plist5_cmp) + "\n")
if not type(plist5_cmp) is list:
  aviso_prog("resultado " + str(plist5_cmp) + " deveria ser lista",True)
  ok_global = False
else:
  plist5_cmp = sorted(plist5_cmp)
  plist5_esp = [pident1, pident2]
  if plist5_cmp != plist5_esp:
    aviso_prog("resultado foi " + str(plist5_cmp) + " deveria ser " + str(plist5_esp),True)
    ok_global = False

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
