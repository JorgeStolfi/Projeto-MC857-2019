import sessao
import usuario
import compra
import gera_html_pag
import gera_html_form
from utils_testes import erro_prog
import sys

def processa(ses, args):
  sys.stderr.write("sessao = " + str(ses) + "\n")
  sys.stderr.write("args = " + str(args) + "\n")
  if 'id_compra' in args:
    # Supõe que o objetivo é mostrar/alterar um usuário existente:
    id_usuario = args['id_usuario']
    id_compra = args['id_compra']
    usr = usuario.busca_por_identificador(id_usuario)
    cpr = compra.busca_por_identificador(id_compra)
    assert ses != None and usr == sessao.obtem_usuario(ses)
    assert compra.obtem_status(cpr) == "aberto" and compra.obtem_endereco(cpr) != None
    pag = gera_html_pag.escolher_pagamento(ses, id_compra, cpr_atrs, None)
  else:
    # Supõe que o objetivo é cadastrar um novo usuário:
    pag = gera_html_pag.mensagem_de_erro(ses, "Nenhuma compra feita.")
  return pag
