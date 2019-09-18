# Implementação do módulo {comando_subm_comprar_produto}.

import gera_html_pag
import compra
import produto

def processa(bas, sessao, args):
  id_produto = args['id_produto']
  prod = produto.busca_por_identificador(id_produto)
  quantidade = float(args['quantidade'])
  carrinho = sessao.obtem_carrinho()
  carrinho.acrescenta_item(bas, prod, quantidade)
  return gera_html_pag.lista_compra(carrinho)
