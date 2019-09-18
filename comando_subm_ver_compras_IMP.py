# Implementação do módulo {comando_subm_ver_compras}.

import usuario
import sessao

def processa(ses, args):
  id_usuario = sessao.obtem_usuario(ses)
  lista = usuario.busca_por_identificador(id_usuario)
  return lista
