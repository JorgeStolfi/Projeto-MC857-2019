#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import comando_subm_comprar_produto_IMP
import sys
import tabela_de_compras as tb_cpr
import tabela_de_usuarios as tb_usr
import compra; from compra import ObjCompra
import usuario; from usuario import ObjUsuario

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

# COPIADO DO COMPRA_TST
usr = {
    "nome": "Vinicius Souza",
    "senha": "aaa",
    "email": "vinicius.souza@teste.com",
    "CPF": "049.522.741-28",
    "endereço": "nao tenho casa",
    "CEP": "13083-440",
    "telefone": "+55(19)9999-9999"
}
cpr = compra.cria(bas,usr)

prod_atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
'unidade': '1 aparelho' }

prod = ObjProduto(prod_atrs)      

cpr.acrescenta_item(prod,3)

res = tb_cpr.cria_tabela(bas)


html = comando_subm_comprar_produto_IMP.processa(bas, res, carrinho)
html = html + "\n"

sys.stdout.buffer.write(html.encode('utf-8'))
