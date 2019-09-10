#! /usr/bin/python3

import sys
import compra; from compra import ObjCompra
import usuario; from usuario import ObjUsuario
import produto; from produto import ObjProduto
import base_sql
import tabela_de_compras
import identificador


sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Criando tabela de compras...\n")
res = tabela_de_compras.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

usr_atrs = {
    "nome": "Alberto Nogueira",
    "senha": "1234",
    "email": "alberto@nogueira.com",
    "CPF": "123.456.789-10",
    "endereço": "Av. Dr. Romeu Tórtima 992",
    "CEP": "13083-440",
    "telefone": "+55(19)9999-9999"
}

# usr = usuario.cria(bas,usr_atrs)
""" Ignorando usuario a fim de teste """
usr = None
cpr = compra.cria(bas,usr)

sys.stderr.write(str(cpr.obtem_identificador()) + "\n")
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


# prod = produto.cria(bas,prod_atrs)
""" Criando objeto produto"""
prod = ObjProduto(prod_atrs)      

cpr.acrescenta_item(prod,3)

sys.stderr.write(str(cpr.lista_itens()) + "\n")

cpr.troca_qtd(prod, 4)

sys.stderr.write(str(cpr.lista_itens()) + "\n")

cpr.elimina_prod(prod)

sys.stderr.write(str(cpr.lista_itens()) + "\n")
# ======================================================================
#! /usr/bin/python3

import tabela_de_compras as tb_cpr
import tabela_de_usuarios as tb_usr
import compra; from compra import ObjCompra
import usuario; from usuario import ObjUsuario

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Criando tabela de usuarios...\n")
res = tb_usr.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

sys.stderr.write("Criando tabela de compras...\n")
res = tb_cpr.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

def valida_busca_por_identificador(bas):
    cpr = compra.cria(bas)
    ind = cpr.acrescenta(bas,cpr)
    res = cpr.busca_por_identificador(ind)
    if cpr != res:
        print("O resultado esperado era " + str(cpr) + " mas foi retornado " + str(res))
    else:
        print("Foi retornado o resultado esperado")

def valida_acrescenta(bas):
    ultimo = bas.indice_inserido()
    cpr = compra.cria(bas)
    novo = cpr.acrescenta(cpr)
    if novo <= ultimo:
        print("O ID inserido esta incorreto")
    else:
        print("A entrada inserida está correta")

def valida_atualiza(bas):
    ult_id = bas.indice_inserido()
    ult_cpr = cpr.busca_por_identificador(ult_id)
    if ult_cpr.aberta() == True:
        ult_cpr.logout()
    else:
        usr = usuario.cria(bas,atrs)
        ult_cpr.login(usr)
    nova_aberta = ult_cpr.aberta()
    bas.atualiza(ult_cpr)

    res = bas.busca_por_identificador(ult_id)
    if res.aberta() != nova_aberta:
        print("O resultado esta errado")
    else:
        print("O resultado está correto")


valida_busca_por_identificador(bas)
valida_acrescenta(bas)
valida_atualiza(bas)
# ======================================================================
#! /usr/bin/python3

import tabela_de_sessoes
import sessao; from sessao import ObjSessao
import usuario; from usuario import ObjUsuario

import tabela_de_itens_de_compras as tb_itens
import base_sql
import identificador
import sys

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Criando tabela de itens de compras...\n")
res = tb_itens.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

#Teste acrescenta
atrs = {
  "id_compra" : "00000001",
  "id_produto" : "00000002",
  "qt" : "32",
  "preco" : "3.50"
}
#acrescenta linha
tb_itens.acrescenta(bas,atrs)
id_compra = int("00000001")
lista = tb_itens.busca_por_compra(bas,id_compra)
for i in lista:
  sys.stderr.write(str(i[0]))



def valida_busca_por_indice(bas):
    ses = sessao.cria(bas)
    ind = tabela_de_sessoes.acrescenta(bas,ses)
    res = tabela_de_sessoes.busca_por_indice(ind)
    if ses != res:
        print("O resultado esperado era " + str(ses) + " mas foi retornado " + str(res))
    else:
        print("Foi retornado o resultado esperado")

def valida_acrescenta(bas):
    ultimo = bas.indice_inserido()
    ses = sessao.cria(bas)
    novo = tabela_de_sessoes.acrescenta(ses)
    if novo <= ultimo:
        print("O ID inserido esta incorreto")
    else:
        print("A entrada inserida está correta")

def valida_atualiza(bas):
    ult_id = bas.indice_inserido()
    ult_ses = tabela_de_sessoes.busca_por_indice(ult_id)

    if ult_ses.aberta() == True:
        ult_ses.logout()
    else:
        usr = usuario.cria(bas,atrs)
        ult_ses.login(usr)
    nova_aberta = ult_ses.aberta()
    bas.atualiza(ult_ses)

    res = bas.busca_por_indice(ult_id)
    if res.aberta() != nova_aberta:
        print("O resultado esta errado")
    else:
        print("O resultado está correto")


