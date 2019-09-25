# Implementação do módulo {comando_botao_sair}.

import gera_html_pag
import sessao

def processa(ses, args):
  if(ses == None):
    pagina = gera_html_pag.generica("Erro, essa sessao nao existe!")
  else:
    nova_sessao = ses.fechar(ses)
    pagina = gera_html_pag.entrada_da_loja(ses, args)
  return pagina