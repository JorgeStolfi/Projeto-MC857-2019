# Implementação do módulo {comando_buscar_produtos}.

import gera_html_pag
import produto

def processa(ses, args):
  if 'condicao' in args:
    cond = args['condicao'].strip()
  else:
    cond = ""
    
  if cond != "":  
    ids_prods = produto.busca_por_palavra(cond)
    pag = gera_html_pag.lista_de_produtos(ses, ids_prods, None)
  else:
    pag = gera_html_pag.mensagem_de_erro(ses, "Favor informar palavra para busca do produto.")
  return pag

