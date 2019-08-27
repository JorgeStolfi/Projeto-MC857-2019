
def cria():
    sessao = Sessao_IMP()
    return sessao


class Sessao_IMP:
    def __init__(self):
        self.usr = None

    def aberta(self):
        return self.usr is not None

    def login(self, usr):
        self.usr = usr

    def logout(self):
        self.usr = None
        
    def obtem_usuario(self):
        return self.usr

    def obtem_identificador(selfs):
        return ''

