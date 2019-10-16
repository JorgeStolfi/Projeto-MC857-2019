# Implementação do módulo {comando_menu_sair}.

import gera_html_pag
import sessao

def processa(ses, args):
  ident = "S-00000004"
  ses = sessao.busca_por_identificador(ident)
  if not sessao.aberta(ses):
    pagina = gera_html_pag.mensagem_de_erro(ses, "Essa sessao nao existe!")
  else:
    sessao.fecha(ses)
    pagina = gera_html_pag.principal(None)
  return pagina
