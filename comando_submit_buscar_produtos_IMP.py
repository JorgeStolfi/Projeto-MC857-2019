# Implementação do módulo {comando_submit_buscar_produtos}.

import gera_html_pag
import produto

def processa(ses, args):
  cond = args['condicao'].strip()
  # !!! Precisa verificar se a condição não tem caracteres perigosos, como ';'. !!!
  if cond != "":  
    ids_prods = produto.busca_por_palavra(cond)
    return gera_html_pag.lista_de_produtos(ses, ids_prods)
  else:
    return gera_html_pag.mensagem_de_erro("Favor informar palavra para busca do produto.")

