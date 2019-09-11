# Este módulo processa o acionamento do botão "Sair" do menu principal pelo usuário. 

import comando_botao_sair_IMP
import sessao

def processa(sessao):
  """Encerra a {sessao} dada e retorna o HTML da página de entrada"""
  return comando_botao_sair_IMP.processa(sessao)

