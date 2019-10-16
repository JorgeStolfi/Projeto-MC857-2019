# Implementação do módulo {comando_menu_ver_usuario}

import sessao
import usuario
import gera_html_form

def processa(ses, args):
    usuario = args ['usuario']
    pag = gera_html_form.alterar_usuario(usuario)
    return pag