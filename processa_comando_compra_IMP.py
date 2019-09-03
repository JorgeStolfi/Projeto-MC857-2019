import gera_html_pag, compra, produto

def processa_compra(bas, compra, codigo_produto, quantidade):
    compra.acrescenta_item(bas,codigo_produto, quantidade)
    return gera_html_pag.lista_compra(compra)