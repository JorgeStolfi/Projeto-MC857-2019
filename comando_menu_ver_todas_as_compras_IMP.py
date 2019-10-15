# Implementação do módulo {comando_menu_ver_todas_as_compras}.

import usuario
import sessao
import gera_html_pag
import compra

def processa(ses, args):
  usr = sessao.obtem_usuario(ses)
  idents = compra.busca_por_usuario(usuario.obtem_identificador(usr))
  return gera_html_pag.lista_de_compras(ses, idents)
