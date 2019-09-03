import base_sql
import tabela_de_sessoes
import identificador

class ObjSessao_IMP:
    def __init__(self):
        self.id_sessao = None
        self.usr = None

    def aberta(self):
        return self.usr is not None

    def login(self, usr):
        self.usr = usr

    def logout(self):
        self.usr = None
        
    def obtem_usuario(self):
        return self.usr

    def obtem_identificador(self):
        return self.id_sessao

def cria(bas):
    ses = ObjSessao_IMP()
    ids = tabela_de_sessoes.acrescenta(bas,ses)
    ses.id_sessao = ids
    return ses
