# Implementação do módulo {comando_subm_entrar}.

import usuario

def processa(email, senha):
    if(usuario.busca_por_email(email)):
        return True
    else:
        return False