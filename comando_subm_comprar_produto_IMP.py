# Implementação do módulo {comando_subm_comprar_produto}.

import gera_html_pag
import compra
import produto
import tabela_de_produtos

def processa(bas, sessao, args):
  id_produto = args['id_produto']
  prod = tabela_de_produtos.busca_por_identificador(bas, id_produto)
  quantidade = float(args['quantidade'])
  carrinho = sessao.obtem_carrinho()
  carrinho.acrescenta_item(bas, prod, quantidade)
  return gera_html_pag.lista_compra(carrinho)
