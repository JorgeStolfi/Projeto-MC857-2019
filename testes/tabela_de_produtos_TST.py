#! /usr/bin/python3

import sys

import produto
import base_sql
import tabela_de_produtos as tbpr
from produto import ObjProduto

bas = base_sql.conecta("DB",None,None)

def valida_resultados(esperado, obtido):
  if(esperado != obtido):
    sys.stderr.write("ERRO: o resultado " + str(obtido) + " é diferente do esperado " + str(esperado) + "\n")  
  else:
    sys.stderr.write("Sucesso\n")

# Cria um produto para teste. 
# Isto testa {produto.cria()} e {tabela_de_produtos.acrescenta()}:
atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
prod = produto.cria(bas,atrs)

# Testa métodos da classe {ObjProduto}:
sys.stderr.write("Testando metodo obter_identificador\n")
obtido = prod.obtem_identificador()
esperado = "P-00012345"
valida_resultados(obtido, esperado)

sys.stderr.write("Testando metodo calcula_preco\n")
obtido = prod.calcula_preco(10)
esperado = 3.1415926
valida_resultados(obtido, esperado)

sys.stderr.write("Testando metodo obtem_atributos\n")
obtido =  prod.obtem_atributos()
esperado = {"atrs": atrs, "id": "P-00012345"}
valida_resultados(obtido, esperado)

# Testa método {muda_atributos}. Também testa {tabela_de_produtos.atualiza}.
sys.stderr.write("Testando metodo muda_atributos\n")
prod.muda_atributos(bas,{'preco': 150.00})
obtido = prod.obtem_atributos().get('preco')
esperado = 150.00
valida_resultados(obtido, esperado)
obtido = tbpr.busca_por_identificador(bas, prod.obtem_identificador()).get('preco')
esperado = prod.obtem_atributos().get('preco')
valida_resultados(obtido, esperado)

# Testa busca de produtos por índice:
obtido = tbpr.busca_por_identificador(bas, prod.obtem_identificador())
esperado = produto.obtem_atributos()
valida_resultados(obtido, esperado)

# Testa busca de produtos por palavra:
pal = "ouriço"
obtido = tbpr.busca_por_palavra(bas, pal)[0]
esperado = prod.obtem_identificador()
valida_resultados(obtido, esperado)
