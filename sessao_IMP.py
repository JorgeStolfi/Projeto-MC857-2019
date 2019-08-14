import requests

def login(usuario, senha):
    #TODO: Fazer a busca do usuario na base

    s = requests.session()

    jar = requests.cookies.RequestsCookieJar()
    
    #TODO: Adicionar o cookie da forma correta
    jar.set("NOME USUARIO", usuario)
    jar.set("PASSWORD", senha)

    s.cookies = jar
    print('login realizado com sucesso')

def logout():
    s = requests.session()
    try:
        jar = requests.cookies.RequestsCookieJar()
        jar.pop("NOME USUARIO")
        jar.pop("PASSWORD")
        s.cookies = jar
    except KeyError:
        print('o usuario nao esta logado')

    print('logout realizado com sucesso')

def recuperar_senha(usuario):
    #TODO: Verificar se essa funcao irá existir
    print(usuario + ',', 'sua senha é:', '321teste')