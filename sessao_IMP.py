import requests

class Sessao_IMP:

    def aberta(self):
        """Verifica se a sessão está aberta"""
        return self.sessao_aberta

    def login(self, usr):
        """Faz o login do usuário"""
        self.sessao_aberta = True
        self.usr = usr

    def logout(self):
        """Faz o logout do usuario"""
        self.sessao_aberta = False
        self.usr = None
        
    def obtem_usuario(self):
        """Retorna o usuário logado na sessão"""
        return self.usr
    
    def cria(self):
        """ Cria uma nova sessao """
        self.sessao_aberta = False
        return self
