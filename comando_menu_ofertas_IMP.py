# Implementação do módulo {comando_menu_ofertas}. 

import gera_html_pag
import tabela_generica
import produto

def processa(ses, args):
    lista_apresentacao = tabela_generica.busca_por_valor(nome, let, cols, chaves, 20.00)
    return gera_html_pag.lista_de_produtos(ses, lista_apresentacao)
