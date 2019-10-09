# Implementação do módulo {comando_menu_sair}.

import gera_html_pag
import sessao


def processa(ses):
    if not sessao.aberta(ses):
        pagina = gera_html_pag.mensagem_de_erro(ses, "Essa sessao nao existe!")
    else:
        sessao.fecha(ses)
        pagina = gera_html_pag.principal(ses)
    return pagina
