# Este módulo processa a acao do usuário que consiste em alterar a quantidade
# de um produto numa compra ou numa página que mostra a decrição detalhada do produto.

import comando_alterar_qtd_de_produto_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário modifica o campo "Quantidade" 
    de um produto {prod}, em uma descrição de produto ou em um item de compras.  
    
    O identificador do produto "P-{NNNNNNNN}" deve estar em {args['id_produto']},
    a nova quantidade deve estar em {args['quantidade']} (na forma de um string).
    
    Se o campo {args['id_compra']} estiver definido, a função supõe que este
    produto é um item de um carrinho de compras {cpr} com esse identificador,
    que deve ter a forma "C-{MMMMMMMM}".  Essa compra deve estar aberta,
    e deve pertencer ao usuário que está logado na sessão {ses}, que não deve ser
    {None}.  Nesse caso, a função altera a quantidade do produto {prod}
    na lista de itens dessa compra.  A função então devolve uma página
    contendo a descrição detalhada da compra {cpr}, como produzida
    por {gera_html_pag.mostra_compra(ses,cpr)}.
    
    Se o campo {args['id_compra']} não existir, a função supõe que o usuário
    alterou o campo "Quantidade" numa descrição de produto, para 
    ver o preço total e possivelmente comprar o mesmo.  Nesse caso, a 
    função não modifica nenhum pedido de compras, e devolve uma página HTML com 
    a descrição completa do produto, como {gera_html_pag.mostra_produto(ses,None,prod,qtd)}
    mostrando a nova quantidade e o preço calculado correspondente.  Neste caso, 
    a sessão {ses} é ignorada e pode ser {None} (ou seja, o usuário não precisa estar 
    logado)."""
    return comando_alterar_qtd_de_produto_IMP.processa(ses, args)

