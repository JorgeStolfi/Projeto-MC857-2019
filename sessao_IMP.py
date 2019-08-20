import requests

#TODO: Importar usuário. Por causa de um erro nessa classe, a importação não foi feita
#import usuario
#from usuario import Usuario


class Sessao_IMP:
    def __self__(self):
        self.sessao_aberta = False

    def aberta(self):
        return self.sessao_aberta

    def login(self):
        self.sessao_aberta = True
        print('login realizado com sucesso')

    def logout(self):
        self.sessao_aberta = False
        print('logout realizado com sucesso')
    
    #TODO: Descomentar esse método quando a classe Usuario estiver corrigida
    # def obtem_usuario(self):
    #     if self.sessao_aberta:
    #         return Usuario()
    #     else:
    #         return None