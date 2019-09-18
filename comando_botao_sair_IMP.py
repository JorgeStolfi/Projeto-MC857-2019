# Implementação do módulo {comando_botao_sair}.

import gera_html_pag
import sessao

def processa(ses, args):
  
  if(ses == None):
    pagina = gera_html_pag.generica("Erro, essa sessao nao existe!")
  else:
    sessao.logout(ses)
    pagina = gera_html_pag.entrada()
    
  return pagina