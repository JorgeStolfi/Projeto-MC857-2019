# Este módulo processa o acionamento do botão "Cadastrar" do menu principal pelo usuário.

import comando_botao_cadastrar_IMP

def processa(ses, args):
  """Este módulo processa o acionamento pelo usuário do botão "Cadastrar" do menu principal.
  Retorna uma página HTML contendo o formulario de dados para cadastrar um novo cliente,
  que deve ser preenchido pelo usuário."""
  return comando_botao_cadastrar_IMP.processa(ses, args)
