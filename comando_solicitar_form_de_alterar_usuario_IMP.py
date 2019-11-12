# Implementação do módulo {comando_solicitar_form_de_alterar_usuario}

import sessao
import usuario
import gera_html_pag
from utils_testes import erro_prog
import sys

def processa(ses, args):
  sys.stderr.write("sessao = " + str(ses) + "\n")
  sys.stderr.write("args = " + str(args) + "\n")
  
  # Obtém o usuário a alterar, e seus dados correntes:
  if 'id_usuario' in args:
    id_usuario = args['id_usuario']
    usr = usuario.busca_por_identificador(id_usuario)
  elif ses != None:
    usr = sessao.obtem_usuario(ses)
    id_usuario = usuario.obtem_identificador(usr)
  else:
    # Não deveria acontecer:
    erro_prog("falta campo 'id_usuario'")
  atrs_usr = usuario.obtem_atributos(usr)
  pag = gera_html_pag.alterar_usuario(ses, id_usuario, atrs_usr, None)
  return pag
