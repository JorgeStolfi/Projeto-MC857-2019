# !!! Escrever !!!

import gera_html_pag
from utils_testes import erro_prog
import sys

def processa(ses, args):
  # Só válido se logado:
  if ses == None or not session.aberta(ses):
    pag = gera_html_pag.entrar(ses, ["Favor se identificar primeiro",])
  else:
    # Obtem o identificador da compra a alterar:
    if 'id_compra' not in args:
      # Não deveria acontecer:
      erro_prog("falta campo 'id_compra'")
    id_compra = args['id_compra']
    # Hack because GET arguments are lists:
    if type(id_compra) is list:
      assert len(id_compra) == 1
      id_compra = id_compra[0]
    sys.stderr.write("id_compra = '" + str(id_compra) + "'\n")
    pag = gera_html_pag.alterar_endereco(ses, id_compra, args, None)
  return pag
