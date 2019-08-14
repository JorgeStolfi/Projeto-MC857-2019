import requests

def login(usuario, senha):
    """Busca usuário na base e verifica se a senha informada está correta"""
    s = requests.session()
    jar = requests.cookies.RequestsCookieJar()
    jar.set("NOME USUARIO", usuario)
    jar.set("PASSWORD", senha)

    s.cookies = jar

    print(s.cookies)
    print('login realizado com sucesso')

def logout():
    s = requests.session()
    try:
        jar = requests.cookies.RequestsCookieJar()
        jar.pop("NOME USUARIO")
        jar.pop("PASSWORD")
        s.cookies = jar
    except KeyError:
        print('Usuario nao esta logado')

    print('logout realizado com sucesso')


def recuperar_senha():
    raise Exception('recuperar_senha nao implementado')