# Implementação do módulo {comando_subm_buscar_produtos}.

import gera_html_pag, tabela_de_produtos

def processa(bas, sessao, args):
  cond = args['cond']
  prods = tabela_de_produtos.busca_por_nome(bas, cond)
  return gera_html_pag.lista_de_produtos(prods)
  
