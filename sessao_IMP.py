import requests

#TODO: Importar usuário. Por causa de um erro nessa classe, a importação não foi feita
#import usuario
#from usuario import Usuario


class Sessao_IMP:
    def aberta(self):
        s = requests.session()
        try:
            jar = requests.cookies.RequestsCookieJar()
            aberta = jar.get("aberta")
            return aberta
        except KeyError:
            return False

    def login(self, usuario, senha):
        s = requests.session()
        jar = requests.cookies.RequestsCookieJar()
        jar.set("aberta", True)
        s.cookies = jar
        print('login realizado com sucesso')

    def logout(self):
        s = requests.session()
        try:
            jar = requests.cookies.RequestsCookieJar()
            jar.pop("aberta")
            s.cookies = jar
        except KeyError:
            print('o usuario nao esta logado')

        print('logout realizado com sucesso')

    def recuperar_senha(self, usuario):
        #TODO: Verificar se essa funcao irá existir
        print(usuario + ',', 'sua senha é:', '321teste')