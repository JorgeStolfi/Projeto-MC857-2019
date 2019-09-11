import tabela_generica as tabela

def inicializa():
    tabela.cria_tabela("sessoes", ["id_sessao", "usr", "aberta"])

class ObjSessao_IMP:
    def __init__(self, usr):
        self.id_sessao = None
        self.usr = usr
        self.aberta = True

def cria(usr):
    sessao = ObjSessao_IMP(usr)
    tabela.atualiza("sessoes", sessao)
    return sessao

def obtem_identificador(sessao):
    return sessao.id_sessao

def obtem_usuario(sessao):
    return sessao.usr

def busca_por_identificador(id_sessao):
    sessao = tabela.busca_por_identificador("sessoes", id_sessao)
    return sessao

def aberta(sessao):
    return sessao.aberta

#obtem_atributos

def muda_atributos(sessao, alts):
    sessao.usr = alts.usr
    sessao.aberta = alts.aberta
    sessao.id_sessao = alts.id_sessao
    tabela.atualiza("sessoes", sessao)


def logout(sessao):
    sessao.usr = None
    tabela.atualiza("sessoes", sessao)

#campos
