# Implementação do módulo {comando_solicitar_form_de_acrescentar_produto}

import gera_html_pag
import sys

def processa(ses, args):
  pag = gera_html_pag.acrescentar_produto(ses, args, None)
  return pag
