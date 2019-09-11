# Este módulo processa a acao do usuario que consiste em pedir para ver a lista de pedidos de compras do usuário, em qualquer estado.

import comando_subm_ver_compras_IMP

def processa(bas, id_usuario):
    """Esta função espera o identificador do usuario que faz a requisição.
    Devolve a lista de pedidos que o usuário já realizou"""
    
    return comando_subm_ver_compras_IMP.processa(bas, id_usuario)
