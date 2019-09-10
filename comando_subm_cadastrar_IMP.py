# Implementação do módulo {comando_subm_cadastrar}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import gera_html_pag

def processa(bas, sessao, args):
  usr = usuario.cria(args)
  return gera_html_pag.mostra_usuario(usr)
