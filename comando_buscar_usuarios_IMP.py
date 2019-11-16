# Implementação do módulo {comando_buscar_usuarios}.

import gera_html_pag
import usuario

def processa(ses, args):
 if 'condicao' in args:
  cond = args['condicao'].strip()
 else:
  cond = ""
 if cond != "":  
  ids_usr = usuario.busca_por_palavra(cond)
  pag = gera_html_pag.bloco_de_lista_de_usuarios(ses, ids_usr, None)
 else:
  pag = gera_html_pag.mensagem_de_erro(ses, "Insira nome a ser buscado!")
 return pag
