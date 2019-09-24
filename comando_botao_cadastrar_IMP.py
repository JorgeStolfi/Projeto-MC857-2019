# Implementação do módulo {comando_botao_cadastrar}.

import gera_html_pag

def processa(ses, args):
  pag = gera_html_pag.cadastrar_usuario()
  return pag
