# Implementação do módulo {comando_ver_ofertas}. 

import gera_html_pag
import tabela_generica
import produto

def processa(ses, args):
    lista_ids = produto.busca_ofertas()
    pag = gera_html_pag.lista_de_produtos(ses, lista_ids)
    return pag

def processa_container(ses, args):
    lista_ids = produto.busca_ofertas()
    pag = gera_html_pag.container_de_produtos(ses, lista_ids)
    return pag
