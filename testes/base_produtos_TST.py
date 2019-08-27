#! /usr/bin/python3

import sys
import base_produtos
import produto; from produto import Produto

# import base
# bas = base.conecta("base_produtos", "ra155619", "aluno123")

import mysql_bobo as bas  # criando apenas para testes

if bas == None:
    print("A conexão com a base não foi realizada")

atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
  
prod = produto.cria(atrs)

sys.stderr.write("Teste de acrescenta: "+ str(bas.acrescenta(bas, prod)) + "\n")

sys.stderr.write("Teste de atualiza: " + str(bas.atualiza(bas, prod.obtem_identificador(), prod)) + "\n")

sys.stderr.write("Teste de busca_por_indice: " + str(bas.busca_por_indice(bas, prod.obtem_identificador())) + "\n")

sys.stderr.write("Teste de busca_por_palavra: " + str(bas.busca_por_palavra(bas, "Escovador")) + "\n")