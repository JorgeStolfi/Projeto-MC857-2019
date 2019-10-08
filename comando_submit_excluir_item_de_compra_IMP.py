# Implementação do módulo {comando_submit_excluir_item_de_compra}.

import gera_html_pag
import produto
import compra

def processa(ses, args):
  id_produto = args['id_produto']
  id_compra = args['id_compra']
  #verifica se os ids de compra e produto recebidos existem.
  #caso existam, elimina-se o produto da compra
  prod = produto.busca_por_identificador(id_produto)
  cpr = compra.busca_por_identificador(id_compra)
  if prod != None and cpr != None:
    compra.elimina_prod(cpr, prod)
    return gera_html_pag.lista_compra(ses, cpr)
  else:
    # !!! Deve devolver uma página HTML !!!
    return None
