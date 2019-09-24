# Este módulo processa o acionamento do botão "Ver Carrinho" do menu principal pelo usuário.

import comando_botao_ver_carrinho_IMP

def processa(ses, args):
  """Este módulo processa o acionamento pelo usuário do botão "Ver Carrinho" do menu principal.
  Retorna uma página HTML contendo o carrinho usuário."""
  return comando_botao_ver_carrinho_IMP.processa(ses, args)
