# Este módulo processa a seleção pelo usuário de um produto numa página 
# com uma lista de vários produtos, a fim de ver a descrição detalhada
# do mesmo.

import comando_subm_ver_produto_IMP

def processa(bas, sessao, args):
    """Esta função espera o identificador do produto "P-{NNNNNNNN}"
    em {args['id_produto']}, e opcionalmente a quantidade
    desejada em {args['quantidade']} (na forma de um string).
    Se a quantidade não for especificada, supõe "1".
    Devolve uma página HTML com a descrição detalhada desse
    produto, um campo para preencher a quantidade, e um 
    botão para "Comprar" (isto é, adicionar ao carrinho)."""
    return comando_subm_ver_produto_IMP.processa(bas, sessao, args)
