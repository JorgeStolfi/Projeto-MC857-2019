# Implementação do módulo {comando_fazer_logout}.

import gera_html_pag
import sessao
import processa_comando_http

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    # Isto nunca deveria acontecer, mas em todo caso:
    pag = gera_html_pag.mensagem_de_erro(ses, "Precisa entrar no site antes de sair")
    ses_nova = ses
  else:
    sessao.fecha(ses)
    ses_nova = None
    pag = gera_html_pag.principal(ses_nova, None)
  return pag, ses_nova
