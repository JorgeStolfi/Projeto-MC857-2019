# Implementação do módulo {comando_submit_excluir_item_de_compra}.

import gera_html_pag
import produto
import compra

def processa(ses, args):
  id_produto = args['id_produto']
  id_compra = args['id_compra']
  prod = produto.busca_por_identificador(id_produto)
  cpr = compra.busca_por_identificador(id_compra)
  if prod != None and cpr != None:
    # Elimina o produto da compra:
    compra.elimina_produto(cpr, prod)
    return gera_html_pag.mostra_compra(ses, cpr)
  else:
    # Retorna página de erro
    # !!! Deveria dar mensagens separadas para as duas condições. !!!
    return gera_html_pag.mensagem_de_erro(ses, "Produto ou compra não localizado!")
