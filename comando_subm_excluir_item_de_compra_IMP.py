# Implementação do módulo {comando_subm_excluir_item_de_compra}.

import gera_html_pag
import produto
import compra

def processa(ses, args):
  id_produto = args['id_produto']
  id_compra = args['id_compra']
  #verifica se os ids de compra e produto recebidos existem.
  #caso existam, elimina-se o produto da compra
  if (id_produto!=None and id_compra!=None):
  	prod = produto.busca_por_identificador(id_produto)
  	cpr = compra.busca_por_identificador(id_compra)
        # !!! Tem que ver se esses identificadores existem. !!!
  	compra.elimina_prod(cpr,prod)
	return gera_html_pag.lista_compra(cpr)
  else:
        # !!! Deve devolver uma página HTML !!!
  	return None
