# Implementação do módulo {comando_solicitar_form_de_acrescentar_produto}

import gera_html_form
import sys

def processa(ses, args):
  sys.stderr.write("sessao = " + str(ses) + "\n")
  sys.stderr.write("args = " + str(args) + "\n")
  pag = gera_html_form.acrescentar_produto(ses)
  return pag