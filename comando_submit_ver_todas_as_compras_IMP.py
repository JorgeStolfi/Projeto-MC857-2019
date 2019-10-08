# Implementação do módulo {comando_submit_ver_todas_as_compras}.

import usuario
import sessao
import gera_html_pag
import compra

def processa(ses, args):
  id_usuario = args['id_usuario']
  idents = compra.busca_por_usuario(id_usuario)
  return gera_html_pag.lista_de_compras(ses, idents)
