# Implementação desta interface:
import processa_comando_compra_IMP

def processa_compra(compra):
    """Processa pedido de compra de uma quantidade de uma certa quantidade de produtos
    referenciados pelo codigo_produto."""
    sessao = compra.obtem_identificador()
    produtos = compra.lista_itens()
    total = compra.calcula_total()
    return processa_comando_compra_IMP.processa_compra(sessao, produtos, total)
