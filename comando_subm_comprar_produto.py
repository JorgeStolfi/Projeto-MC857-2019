# Este módulo processa o acionamento pelo usuário do botão "Comprar" numa página
# de um produto, depois de preencher a quantidade desejada.

import comando_subm_comprar_produto_IMP

def processa(sessao, dados):
    """Espera o identificador do produto "P-{NNNNNNNN}" em {dados['id_produto']} e a quantidade
    desejada em {dados['quantidade']} (na forma de um string).
    Acrescenta esse item ao carrinho de compras da {sessao} dada."""
    return comando_subm_comprar_produto_IMP.processa(sessao, dados)
