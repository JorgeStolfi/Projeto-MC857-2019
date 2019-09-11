# Implementação do módulo {comando_subm_excluir_item_de_compra}.

import gera_html_pag
import produto
import compra
import tabela_de_produtos

def processa(bas, sessao, args):
  id_produto = args['id_produto']
  compra = args['compra']
  prod = tabela_de_produtos.busca_por_identificador(bas, id_produto)
  compra.elimina_prod(prod)
  return gera_html_pag.lista_compra(compra)
