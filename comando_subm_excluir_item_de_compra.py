# Este módulo processa a ação do usuário que consiste em apertar o botão
#  "excluir" em um item de uma compra em aberto (carrinho de compras)

import comando_subm_excluir_item_de_compra_IMP

def processa(ses, args):
    """Esta função recebe o identificador do produto "P-{NNNNNNNN}"
    em {args['id_produto']} e o identificador de compra {args['id_compra']} associado. Aleḿ disso, reve a sessao {ss}.
    Devolve uma página HTML com o carrinho de compras atualizado."""
    return comando_subm_excluir_item_de_compra_IMP.processa(ss, args)
