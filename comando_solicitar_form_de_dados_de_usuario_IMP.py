# Implementação do módulo {comando_solicitar_form_de_dados_de_usuario}

import sessao
import usuario
import gera_html_pag
from utils_testes import erro_prog
import sys

def processa(ses, args):
  sys.stderr.write("sessao = " + str(ses) + "\n")
  sys.stderr.write("args = " + str(args) + "\n")
  if 'id_usuario' in args:
    # Supõe que o objetivo é mostrar/alterar um usuário existente:
    usr = usuario.busca_por_identificador(args['id_usuario'])
    assert ses != None and usr == sessao.obtem_usuario(ses)
    pag = gera_html_pag.mostrar_usuario(ses,usr)
  else:
    # Supõe que o objetivo é cadastrar um novo usuário:
    pag = gera_html_pag.cadastrar_usuario(ses)
  return pag
