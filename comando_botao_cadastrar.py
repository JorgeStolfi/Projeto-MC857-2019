# Este módulo processa o acionamento do botão "Cadastrar" do menu principal pelo usuário.

import comando_botao_cadastrar_IMP

def processa(ses, args):
  """Este módulo processa o acionamento do botão "Cadastrar" do menu principal pelo usuário."""
  """Retorna uma página HTML com o formulario de dados para cadastrar
  um novo usuário."""
  return comando_botao_cadastrar_IMP.processa(ses, args)
