#! /usr/bin/python3

import sys

import produto
import base
import base_produtos as baspr
from produto import Produto
import identificador

bas = base.conecta("DB",None,None)

def valida_resultados(esperado, obtido):
  if(esperado != obtido):
    sys.stderr.write("ERRO: o resultado " + str(obtido) + " é diferente do esperado " + str(esperado) + "\n")  
  else:
    sys.stderr.write("Sucesso\n")

# Cria um produto para teste. 
# Isto testa {produto.cria()} e {base_produtos.acrescenta()}:
atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
prod = produto.cria(bas,atrs)

# Testa métodos da classe {Produto}:
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

# Testa método {muda_atributos}. Também testa {base_produtos.atualiza}.
sys.stderr.write("Testando metodo muda_atributos\n")
prod.muda_atributos(bas,{'preco': 150.00})
obtido = prod.obtem_atributos().get('preco')
esperado = 150.00
valida_resultados(obtido, esperado)

# Testa busca de produtos por índice:
ind = identificador.para_indice("P",prod.obtem_identificador())
sys.stderr.write("Teste de busca_por_indice: " + str(baspr.busca_por_indice(bas, ind)) + "\n")

# Testa busca de produtos por palavra:
pal = "ouriço"
sys.stderr.write("Teste de busca_por_palavra: " + str(baspr.busca_por_palavra(bas, pal)) + "\n")
