# Implementação do módulo {comando_menu_sair}.

import gera_html_pag
import sessao

def processa(ses, args):
  if ses == None:
    pagina = gera_html_pag.mensagem_de_erro("Essa sessao nao existe!")
  else:
    nova_sessao = sessao.fecha(ses)
    # !!! A sessão não é mais {ses} !!!
    pagina = gera_html_pag.principal(ses)
  return pagina
