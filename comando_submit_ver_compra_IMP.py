# Implementação do módulo {comando_submit_ver_compra}.

import usuario
import sessao
import compra
import gera_html_elem

def processa(ses, args):
  id_compra = args['id_compra']
  cpr = compra.busca_por_identificador(id_compra)
  return gera_html_elem.bloco_de_compra(cpr, True)
