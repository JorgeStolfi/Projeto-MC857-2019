#! /usr/bin/python3

import sys
import produto; from produto import Produto

atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
  
prod = produto.cria(atrs)

sys.stderr.write(prod.obtem_identificador() + "\n")
sys.stderr.write(str(prod.calcula_preco(10)) + "\n")
sys.stderr.write(str(prod.obtem_atributos()) + "\n")
prod.muda_atributos({'preco': 150.00})
sys.stderr.write(str(prod.obtem_atributos()) + "\n")
