# Implementação do módulo {comando_subm_ver_compras}.

import tabela_de_usuarios

def processa(bas, id_usuario):
  lista = tabela_de_usuarios.busca_compras(bas, id_usuario)
 
  return lista
