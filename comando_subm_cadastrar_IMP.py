# Implementação do módulo {comando_subm_cadastrar}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import gera_html_pag

def processa(sessao, args):
  usr = usuario.cria(args)
  # !!! Deveria verificar se a criação deu certo, e mostrar página de erro caso contrário. !!!
  return gera_html_pag.mostra_usuario(usr)
