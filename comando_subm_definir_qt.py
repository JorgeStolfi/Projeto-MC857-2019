# Este módulo processa a acao do usuário que consiste em alterar a quantidade
# de um produto numa página que mostra a decrição detalhada do produto.

import comando_subm_definir_qt_IMP

# !!! A função abaixo não deve alterar o carrinho. Deve apenas recalcular o preço para a nova quantidade, e mostrar novamente a descrição detalahada do produto {gera_html_pag.mostra_produto} com a nova quantidade e com o preço correspondente. !!!

def processa(ses, args):
    """Espera o identificador do produto "P-{NNNNNNNN}" em {args['id_produto']}
    e a quantidade a ser alterada em {args['quantidade']} (na forma de um string).
    Modifica a quantidade desse produto no carrinho de compras da {sessao} dada."""
    return comando_subm_definir_qt_IMP.processa(ses, args)
