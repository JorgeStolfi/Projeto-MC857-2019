# Este módulo processa a acao do usuario que consiste em pedir para ver a lista de todos os 
# pedidos de compras do usuário, em qualquer estado.

import comando_subm_ver_compras_IMP

def processa(ses, args):
    """Esta função espera o identificador do usuario que faz a requisição.
    Devolve a lista de pedidos que o usuário já realizou, um pedido por linha,
    cada um com um botão "Ver" para mostrar o conteúdo do mesmo."""
    return comando_subm_ver_compras_IMP.processa(ses, args)
