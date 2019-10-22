# Este módulo processa o acionamento pelo usuário do botão "Comprar" numa página
# de um produto, depois de preencher a quantidade desejada.

import comando_comprar_produto_IMP

def processa(ses, dados):
    """Esta função é chamada quando o usuário aperta o botão "Comprar"
    numa descrição de um produto {prod}.  
    
    O identificador "P-{NNNNNNNN}" do produto {prod} deve estar em {dados['id_produto']},
    e a quantidade desejada {qtd} deve estar em {dados['quantidade']} (na forma de um string).
    
    A função acrescenta a quantidade {qtd} do produto {prod} ao carrinho de compras da sessao
    {ses} dada, e devolve uma página com a descrição completa do produto, mostrando a 
    quantidade comprada."""
    return comando_comprar_produto_IMP.processa(ses, dados)
