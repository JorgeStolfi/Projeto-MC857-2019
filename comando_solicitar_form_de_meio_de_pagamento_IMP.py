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
    usr = usuario.busca_por_identificador(args['id_usuario'])
    cpr = compra.busca_por_identificador(args['id_compra'])
    assert ses != None and usr == sessao.obtem_usuario(ses) and compra.obtem_status(cpr) == "aberto" and compra.obtem_endereco(cpr) != None
    pag = gera_html_form.escolher_pagamento()
  else:
    # Supõe que o objetivo é cadastrar um novo usuário:
    pag = gera_html_pag.mensagem_de_erro(ses, "Nenhuma compra feita.")
  return pag
