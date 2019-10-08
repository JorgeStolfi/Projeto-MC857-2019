# Este módulo processa a seleção pelo usuário de um produto numa página 
# com uma lista de vários produtos, a fim de ver a descrição detalhada
# do mesmo.

import comando_submit_ver_produto_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário apertou um botão 
    "Ver" ou equivalente em um bloco que especifica ou descreve
    um produto {prod}.
    
    Ela devolve uma página HTML com a descrição detalhada desse
    produto, um campo para preencher a quantidade, e um 
    botão para "Comprar" (isto é, adicionar ao carrinho).
    
    O identificador "P-{NNNNNNNN}" do produto {prod} deve estar
    em {args['id_produto']}.  Opcionalmente, a quantidade
    desejada pode estar em {args['quantidade']} (na forma de um string).
    Se a quantidade não for especificada, supõe "1".
    
    Por enquanto, a sessão {ses} é irrelevante e pode ser {None}
    (isto é, o usuário não precisa estar logado)."""
    return comando_submit_ver_produto_IMP.processa(ses, args)
