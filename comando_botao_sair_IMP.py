# Implementação do módulo {comando_botao_sair}.

import gera_html_pag
import sessao

def processa(ses, args):
  if(ses == None):
    pagina = gera_html_pag.generica("Erro, essa sessao nao existe!")
  else:
    sessao.fechar(ses)
    # !!! Está retornando a página errada. !!!
    pagina = gera_html_pag.entrar()
  return pagina
