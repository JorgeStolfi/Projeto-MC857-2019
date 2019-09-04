#! /usr/bin/python3

import tabela_de_sessoes
import sessao; from sessao import ObjSessao
import usuario; from usuario import ObjUsuario

import tabela_de_itens_de_compras as itens
import base_sql
import identificador
import sys

# Conexao com a base de dados:
bas = base_sql.conecta("ITEM",None,None)

sys.stderr.write("Testando tabela_de_itens_de_compras ...\n")

#cria a a tabela_de_itens_de_compras
itens.cria_tabela(bas)

#Teste acrescenta
atrs = {
  "id_compra" : "00000001",
  "id_produto" : "00000002",
  "qt" : "32",
  "preco" : "3.50"
}
#acrescenta linha
itens.acrescenta(bas,atrs)
id_compra = int("00000001")
lista = itens.busca_por_compra(bas,id_compra)
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


