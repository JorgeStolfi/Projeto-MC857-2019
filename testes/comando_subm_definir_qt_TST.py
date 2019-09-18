#! /usr/bin/python3

# Teste comando_subm_definir_qt

import comando_subm_definir_qt
import sys
import produto; from produto import ObjProduto

prod_atrs = {
  'descr_curta': "Tenis nike",
  'descr_media': "Tenis preto",
  'descr_longa': "Fabricante: Nike SA\nOrigem: China\nModelo: NKX\nDimensões: 300 x 200 x 100 mm",
  'preco': 300.00,
  'unidade': '1 tenis',
  'estoque': 500,
  'quantidade': "50" }

# prod = produto.cria(bas,prod_atrs)
""" Criando objeto produto"""
prod = produto.cria(prod_atrs)

# TODO usar id_produto valido
args_tabela = {
  'id_produto': "12345",
  'quantidade': "50" }

# bas e sessao ainda nao tem efeito
html = comando_subm_definit_qt.processa(bas, sessao, args_tabela)
html = html + "\n"

sys.stdout.buffer.write(html.encode('utf-8'))
