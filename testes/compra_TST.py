#! /usr/bin/python3

import sys
from compra import Compra
from usuario import Usuario
from produto import Produto

cp = Compra()
produto = Produto()

usuario_atr = {
    "nome": "Alberto Nogueira",
    "senha": "1234",
    "email": "alberto@nogueira.com",
    "cpf": "1234567890",
    "endereço": "Av. Dr. Romeu Tórtima 992",
    "CEP": "{13083}-{440}",
    "telefone": "+55(19)9999-9999"
}

usr = Usuario()

usuario = usr.cria(atrs)
compra = cp.cria(usuario)

sys.stderr.write(compra.obtem_identificador() + "\n")
sys.stderr.write(prod.obtem_usuario() + "\n")
sys.stderr.write(prod.obtem_status() + "\n")
sys.stderr.write(prod.lista_itens() + "\n")
sys.stderr.write(prod.calcula_total() + "\n")

atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }

prod = produto.cria(atrs)


sys.stderr.write(prod.acrescenta_item(produto) + "\n")

sys.stderr.write(prod.torca_qtd(produto, 4) + "\n")

sys.stderr.write(prod.lista_itens() + "\n")

sys.stderr.write(prod.elimina_prod(produto) + "\n")

sys.stderr.write(prod.lista_itens() + "\n")
