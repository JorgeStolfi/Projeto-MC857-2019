# Implementação do módulo {comando_botao_sair}.

import gera_html_pag

def processa(sessao):
  while sessao.aberta():
      objeto_sessao = sessao.logout()
  return gera_html_pag.entrada()
    