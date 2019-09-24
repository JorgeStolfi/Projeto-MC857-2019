# Implementação do módulo {comando_botao_ver_carrinho}.

import gera_html_pag

def processa(ses, args):
  pag = gera_html_pag.carrinho()
  return pag
