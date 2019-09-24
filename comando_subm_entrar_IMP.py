# Implementação do módulo {comando_subm_entrar}.

import usuario
import secrets

def processa(email, senha):
    # !!! Não está de acordo com a interface -- deve devolver uma página HTML !!!
    cookie = secrets.token_urlsafe(32)
    if(usuario.busca_por_email(email)):
        return "True"
    else:
        return "False"
