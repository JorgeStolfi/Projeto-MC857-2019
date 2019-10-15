# Este módulo processa a acao do usuario que consiste em pedir para ver a lista de todos os 
# pedidos de compras do usuário, em qualquer estado.

import comando_menu_ver_todas_as_compras_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário {usr} da sessão {ses} 
    aperta o botão "Ver meus pedidos" ou similar. 
    
    Ela devolve uma página HTML que mostra a lista de pedidos de compras associadas ao 
    usuário, incluindo seu carrinho de compras.  A página relaciona um pedido por linha,
    mostrando seu identificador "C-{NNNNNNNN}", o número de itens, o valor total,
    o status do pedido, e um botão "Ver detalhes" para mostrar o conteúdo do mesmo.
    
    A sessão {ses} não pode ser {None} e deve estar aberta."""
    return comando_menu_ver_todas_as_compras_IMP.processa(ses, args)
