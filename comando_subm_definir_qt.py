# Este módulo processa a acao do usuário que consiste em alterar a quantidade
# de um produto numa página de ver produto.

import comando_subm_comprar_produto_IMP

def processa(bas, sessao, args):
    """Espera o identificador do produto "P-{NNNNNNNN}" em {args['id_produto']}
    e a quantidade a ser alterada em {args['quantidade']} (na forma de um string).
    Acrescenta esse item ao carrinho de compras da {sessao} dada."""
    return comando_subm_comprar_produto_IMP.processa(bas, sessao, args)