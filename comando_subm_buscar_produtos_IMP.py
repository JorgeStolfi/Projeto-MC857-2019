# Implementação do módulo {comando_subm_buscar_produtos}.

import gera_html_pag
import produto

def processa(sessao, args):
  if (len(args) > 0 and args['condicao'].strip() != ""):  
    cond = args['condicao']
  
    prods = produto.busca_por_palavra(cond)
    return gera_html_pag.lista_de_produtos(prods)
  
  # !!! Se a condicao for a string vazia, deve devolver uma página de erro. !!!
  return gera_html_pag.erro_busca_produto("Favor informar palavra para busca do produto.")

