# Implementação desta interface:
import processa_comando_compra_IMP

def processa_compra(sessao, codigo_produto, quantidade):
    """Processa pedido de compra de uma quantidade de um certo produto
    referenciado pelo codigo_produto."""
    return processa_comando_compra_IMP.processa_compra(sessao, codigo_produto, quantidade)
