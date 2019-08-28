#! /usr/bin/python3

import sys

import produto
from produto import Produto

def valida_resultados(esperado, obtido):
  if(esperado != obtido):
    print("ERRO: o resultado " + str(obtido) + " é diferente do esperado " + str(esperado))  
  else:
    print("Sucesso")

atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
  
prod = produto.cria(atrs)

print("Testando metodo obter_identificador")
obtido = prod.obtem_identificador()
esperado = "P-00012345"
valida_resultados(obtido, esperado)

print("Testando metodo calcula_preco")
obtido = prod.calcula_preco(10)
esperado = 3.1415926
valida_resultados(obtido, esperado)

print("Testando metodo obtem_atributos")
obtido =  prod.obtem_atributos()
esperado = {"atrs": atrs, "id": "P-00012345"}
valida_resultados(obtido, esperado)

print("Testando metodo muda_atributos")
prod.muda_atributos({'preco': 150.00})
obtido = prod.obtem_atributos().get('preco')
esperado = 150.00
valida_resultados(obtido, esperado)
