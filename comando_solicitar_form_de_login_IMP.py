# Implementação do módulo {comando_solicitar_form_de_login}. 

import gera_html_pag

def processa(ses, args):
  pag = gera_html_pag.entrar(ses, None)
  return pag
    
