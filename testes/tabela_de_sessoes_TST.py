#! /usr/in/python3

import tabela_de_sessoes
import sessao; from sessao import ObjSessao
import usuario; from usuario import ObjUsuario

def valida_busca_por_indice(bas):
    ses = sessao.cria(bas)
    ind = tabela_de_sessoes.acrescenta(bas,ses)
    res = tabela_de_sessoes.busca_por_indice(ind)
    if ses != res:
        print("O resultado esperado era " + str(ses) + " mas foi retornado " + str(res))
        return False
    else:
        print("Foi retornado o resultado esperado")
        return True

def valida_acrescenta(bas):
    ultimo = bas.indice_inserido()
    ses = sessao.cria(bas)
    novo = tabela_de_sessoes.acrescenta(ses)
    if novo <= ultimo:
        print("O ID inserido esta incorreto")
        return False
    else:
        print("A entrada inserida está correta")
        return True

def valida_atualiza(bas):
    ult_id = bas.indice_inserido()
    ult_ses = tabela_de_sessoes.busca_por_indice(ult_id)
    if ult_ses.aberta() == True:
        ult_ses.logout()
    else:
        usr = usuario.cria(bas)
        ult_ses.login(usr)
    nova_aberta = ult_ses.aberta()
    bas.atualiza(ult_ses)

    res = bas.busca_por_indice(ult_id)
    if res.aberta() != nova_aberta:
        print("O resultado esta errado")
        return False
    else:
        print("O resultado está correto")
        return True

def valida_cria_tabela(bas):
    cmd = "SELECT * FROM sessao"
    if bas.executa_comando(cmd):
        print("Tabela existe")
        return True
    else:
        print("Tabela nao existe")
        return False

def valida_busca_por_identificador(bas, id_sessao):
    ses = sessao.cria(bas)
    id_sessao = tabela_de_sessoes.acrescenta(bas, ses)
    res = tabela_de_sessoes.busca_por_indice(id_sessao)
    if ses != res:
        print("O resultado esperado era " + str(ses) + " mas foi retornado " + str(res))
        return False
    else:
        print("Foi retornado o resultado esperado")
        return True
