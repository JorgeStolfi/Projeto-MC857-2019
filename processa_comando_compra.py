# Implementação desta interface:
import processa_comando_compra_IMP

def processa_compra(bas, compra, codigo_produto, quantidade):
    """Processa pedido de compra de uma quantidade de um certo produto referenciado pelo codigo_produto.
    Recebe um obj do tipo Obj {Compra}, identificador do produto, quantidade de produtos(float) e a 
    referencia para a base de dados.
    O produto deve ser adicionado, com a quantidade correta no pedido/carrinho de compras."""
    return processa_comando_compra_IMP.processa_compra(bas, compra, codigo_produto, quantidade)