# Este módulo processa a acao do usuário que consiste em alterar a quantidade
# de um produto numa página que mostra a decrição detalhada do produto.

import comando_submit_definir_qt_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário modifica o campo "Quantidade" 
    em uma descrição de produto.  
    
    O identificador do produto "P-{NNNNNNNN}" deve estar em {args['id_produto']},
    a nova quantidade deve estar em {args['quantidade']} (na forma de um string).
    
    A função devolve uma página HTML com a descrição completa do produto, mostrando a
    nova quantidade e o preço calculado correspondente. 
    
    Este comando não modifica nenum pedido de compras.  A sessão {ses}
    é ignorada e pode ser {None} (ou seja, o usuário não precisa estar 
    logado)."""
    return comando_submit_definir_qt_IMP.processa(ses, args)
