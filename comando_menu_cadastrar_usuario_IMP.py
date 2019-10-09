# Implementação do módulo {comando_menu_cadastrar_usuario}.

import gera_html_pag

def processa(ses, args):
  pag = gera_html_pag.cadastrar_usuario(ses)
  return pag
