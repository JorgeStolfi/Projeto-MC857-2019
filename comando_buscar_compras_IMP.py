# Implementação do módulo {comando_buscar_compras}.

import usuario
import sessao
import gera_html_pag
import compra

from utils_testes import erro_prog

def processa(ses, args):
  if ses == None or (not sessao.aberta(ses)):
    # Não deveria acontecer, mas:
    pag = gera_html_pag.mensagem_de_erro(ses, "Favor se identificar primeiro")
  else:
    usr = sessao.obtem_usuario(ses)

    admin = usuario.obtem_atributos(usr)['administrador']
    if admin:
      erro_prog("O administrador não pode buscar compras")

    idents = compra.busca_por_usuario(usuario.obtem_identificador(usr))
    pag = gera_html_pag.lista_de_compras(ses, idents, None)
  return pag
