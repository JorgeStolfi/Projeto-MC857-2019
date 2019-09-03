#! /usr/bin/python3

import sys
import compra; from compra import ObjCompra
import usuario; from usuario import ObjUsuario
import produto; from produto import ObjProduto
import base_sql
import tabela_de_compras
import identificador

bas = base_sql.conecta("DB",None,None)

usr_atrs = {
    "nome": "Alberto Nogueira",
    "senha": "1234",
    "email": "alberto@nogueira.com",
    "CPF": "123.456.789-10",
    "endereço": "Av. Dr. Romeu Tórtima 992",
    "CEP": "13083-440",
    "telefone": "+55(19)9999-9999"
}

usr = usuario.cria(bas,usr_atrs)
cpr = compra.cria(bas,usr)

sys.stderr.write(cpr.obtem_identificador() + "\n")
sys.stderr.write(str(cpr.obtem_usuario()) + "\n")

sys.stderr.write(str(cpr.obtem_status()) + "\n")
sys.stderr.write(str(cpr.lista_itens()) + "\n")
sys.stderr.write(str(cpr.calcula_total()) + "\n")

prod_atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }

prod = produto.cria(bas,prod_atrs)

cpr.acrescenta_item(prod,3)

sys.stderr.write(str(cpr.lista_itens()) + "\n")

cpr.troca_qtd(prod, 4)

sys.stderr.write(str(cpr.lista_itens()) + "\n")

cpr.elimina_prod(prod)

sys.stderr.write(str(cpr.lista_itens()) + "\n")
