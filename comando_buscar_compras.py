# Este módulo processa a acao do usuario que consiste em pedir para ver a lista de todos os 
# pedidos de compras do usuário, em qualquer estado.

import comando_buscar_compras_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário {usr} da sessão {ses} 
    aperta o botão "Ver meus pedidos" ou similar. 
    
    A sessão {ses} não pode ser {None} e deve estar aberta.
    
    Ela devolve uma página HTML {pag} que mostra a lista de pedidos de compras associadas ao 
    usuário, incluindo seu(s) carrinho(s) de compras.  A página relaciona um pedido por linha,
    mostrando seu identificador "C-{NNNNNNNN}", o número de itens, o valor total,
    o status do pedido, e um botão "Ver detalhes" para mostrar o conteúdo do mesmo."""
    return comando_buscar_compras_IMP.processa(ses, args)
