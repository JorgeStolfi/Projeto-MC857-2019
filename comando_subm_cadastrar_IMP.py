# Implementação do módulo {comando_subm_cadastrar}.

import gera_html_pag

def processa(bas, sessao, args):
  usr = usuario.cria(bas, args);
  return gera_html_pag.mostra_usuario(usr)
