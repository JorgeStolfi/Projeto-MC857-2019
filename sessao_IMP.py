# Imprementação da classe {Sessao}.

import tabela_generica

class Sessao_IMP:

    def __init__(self, bas, usr):
        self.id_sessao = None
        self.usr = usr
        self.bas = bas
        self.colunas = (
            ('id_usuario', 'char(10)'),
            ('aberta', 'boolean')
        )
        campos = "indice integer NOT NULL PRIMARY KEY"
        for c in self.colunas:
            campos = campos + ", " + c[0] + " " + c[1]
        self.bas.executa_comando_CREATE_TABLE("sessoes", campos);

    def busca_por_identificador(self, id_sessao):
        cmd = "SELECT * FROM sessoes WHERE id = " + id_sessao
        sessao = self.bas.executa_comando_SELECT("sessoes", cmd)
        return sessao

    def aberta(self):
        return self.usr is not None

    def obtem_usuario(self):
        return self.usr

    def atualiza(self, ind, ses):
        usr = ses.obtem_usuario()
        uid = (usr.obtem_identificador() if usr != None else None)
        pares = \
            "usr=" + str(uid) + ", " + \
            "sessao_aberta=" + str(ses.aberta())
        cmd = "UPDATE sessoes SET " + pares + " WHERE id=" + str(ind)
        self.bas.executa_comando_UPDATE("sessoes", )

    def acrescenta(self, ses):
        id = bas.executa_comando_INSERT("sessoes", self)
        return id

    def logout(self, bas):
        self.usr = None
        tabela_de_sessoes.atualiza(bas, self.id_sessao, self)
        

def cria(bas,usr):
    ses = Sessao_IMP()
    ids = ses.acrescenta(bas)
    ses.usr = usr
    ses.id_sessao = ids
    return ses
