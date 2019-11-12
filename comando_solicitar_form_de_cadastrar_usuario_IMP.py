# Implementação do módulo {comando_solicitar_form_de_cadastrar_usuario}

import sessao
import usuario
import gera_html_pag
from utils_testes import erro_prog
import sys

def processa(ses, args):
  sys.stderr.write("sessao = " + str(ses) + "\n")
  sys.stderr.write("args = " + str(args) + "\n")
  pag = gera_html_pag.cadastrar_usuario(ses, None, None)
  return pag
