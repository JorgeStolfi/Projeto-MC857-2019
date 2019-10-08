# Implementação do módulo {comando_submit_ver_todas_as_compras}.

import usuario
import sessao

def processa(ses, args):
  id_usuario = args['id_usuario']
  usr = compra.busca_por_identificador(id_usuario)
  return gera_html_pag.lista_de_compra(cpr)
