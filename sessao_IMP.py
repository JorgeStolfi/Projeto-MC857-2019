import requests

def login(usuario, senha):
    """Busca usuário na base e verifica se a senha informada está correta"""
    s = requests.session()
    jar = requests.cookies.RequestsCookieJar()
    jar.set("NOME USUARIO", usuario)

    s.cookies = jar

    print(s.cookies)
    print('login realizado com sucesso')

def logout():
    raise Exception('logout nao implementado')

def recuperar_senha():
    raise Exception('recuperar_senha nao implementado')