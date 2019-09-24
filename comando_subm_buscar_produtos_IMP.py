# Implementação do módulo {comando_subm_buscar_produtos}.

import gera_html_pag
import produto

def processa(sessao, args):
  cond = args['condicao']
  # !!! Se a condicao for a string vazia, deve devolver uma página de erro. !!!
  prods = produto.busca_por_palavra(cond)
  return gera_html_pag.lista_de_produtos(prods)
  
