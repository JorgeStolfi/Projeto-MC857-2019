# Implementação do módulo {comando_subm_ver_compras}.

import usuario
import sessao

def processa(ses, args):
  id_compra = args['id_compra']
  comp = compra.busca_por_identificador(id_compra)
  return gera_html_elem.bloco_de_compra(comp)
