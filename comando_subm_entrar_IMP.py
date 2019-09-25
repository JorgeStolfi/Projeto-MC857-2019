# Implementação do módulo {comando_subm_entrar}.

import usuario
import sessao
import secrets
import gera_html_pag

def processa(email, senha):
    usr_id = usuario.busca_por_email(email)
    if(usr_id != None):
        usr = usuario.busca_por_identificador(usr_id)
        atrs_usr = usuario.obtem_atributos(usr)
        if(atrs_usr["senha"] == senha):
            cookie = secrets.token_urlsafe(32)      
            return gera_html_pag.entrada_da_loja(sessao.cria(usr,cookie),None)
    else:
        return gera_html_pag.generica("Usuario ou senha invalidos")
