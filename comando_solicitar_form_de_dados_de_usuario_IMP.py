# Implementação do módulo {comando_solicitar_form_de_dados_de_usuario}

import sessao
import usuario
import gera_html_pag
from utils_testes import erro_prog
import sys

def processa(ses, args):
  sys.stderr.write("sessao = " + str(ses) + "\n")
  sys.stderr.write("args = " + str(args) + "\n")
  if ses is None or sessao.obtem_usuario(ses) is None:
    # Supõe que o objetivo é cadastrar um novo usuário:
    pag = gera_html_pag.cadastrar_usuario(ses)
  else:
    # Supõe que o objetivo é mostrar/alterar um usuário existente:
    usr = sessao.obtem_usuario(ses)
    pag = gera_html_pag.mostra_usuario(ses,usr)
  return pag
