# Implementação do módulo {comando_subm_buscar_produtos}.

import gera_html_pag
import produto

def processa(bas, sessao, args):
  cond = args['cond']
  prods = produto.busca_por_palavra(cond)
  return gera_html_pag.lista_de_produtos(prods)
  
