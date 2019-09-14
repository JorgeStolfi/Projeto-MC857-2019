#! /usr/bin/python3

import produto; from produto import ObjProduto
import produto_IMP; from produto_IMP import ObjProduto_IMP
import tabela_generica
import base_sql
import sys
import identificador

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {produto}: \n")
produto.inicializa()

colunas = produto.campos()

sys.stderr.write("Limpando a tabela \"produtos\":\n")
res = tabela_generica.limpa_tabela("produtos", colunas)
sys.stderr.write("  res = " + str(res) + "\n")

# ----------------------------------------------------------------------
def mostra_produto(rotulo, prod, id, atrs):
  """Imprime produto {prod} e compara seus atributos com {id,atrs}."""
  sys.stderr.write(rotulo + " = \n")
  if prod == None:
    sys.stderr.write("None\n")
  elif type(prod) is ObjProduto_IMP:
    sys.stderr.write("  id = " + str(produto.obtem_identificador(prod)) + "\n")
    sys.stderr.write("  atrs = " + str(produto.obtem_atributos(prod)) + "\n")
    if atrs != None:
      id_confere = (produto.obtem_identificador(prod) == id)
      atrs_conferem = (produto.obtem_atributos(prod) == atrs)
      sys.stderr.write("  CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")

def testa_cria_produto(rotulo, id, atrs):
  """Testa criação de produto com atributos com {atrs}. Retorna o produto."""
  prod = produto.cria(atrs)
  mostra_produto(rotulo, prod, id, atrs)
  return prod

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.acrescenta}:\n")
prod1_atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': float("120.00"),
  'unidade': '1 aparelho'
}
uid1 = "P-0000000"
prod = testa_cria_produto("prod1", uid1, prod1_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.obtem_identificador}:\n")

prod1_a = produto.busca_por_identificador(uid1)
mostra_produto("prod1_a", prod1_a, uid1, prod1_atrs)


# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.calcula_preco}:\n")

prod1_a_preco = produto.calcula_preco()
mostra_produto("prod1_a", prod1_a, uid1, prod1_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.obtem_atributos}:\n")

prod1_a_atrs =  produto.obtem_atributos()
mostra_produto("prod1_a", prod1_a, uid1, prod1_a_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.muda_atributos}:\n")

prod1_mods = {
  'descr_curta': "Escovador de ouriço 2.0 Power Blaster",
  'preco': 1200.00,
}
prod1_a.muda_atributos(prod1_a, prod1_mods)
prod1_b = produto.busca_por_identificador(uid1)
prod1_b_atrs = prod1_a_atrs

# ----------------------------------------------------------------------
sys.stderr.write("testando {produto.busca_por_palavra}:\n")

palavra = "ouriço"
prod2_a = produto.busca_por_palavra(palavra)
prod2_a_atrs = produto.obtem_atributos()

mostra_produto("prod2_a", prod2_a, uid1, prod2_a_atrs)
