# Este módulo processa o acionamento do botão "Cadastrar" do menu geral pelo usuário.

import comando_menu_cadastrar_usuario_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Cadastrar" do menu geral.
  
  Retorna uma página HTML contendo o formulario de dados para cadastrar um novo cliente,
  que deve ser preenchido pelo usuário.  A sessão {ses} e or argumentos {args} são irrelevantes
  e podem ser {None}."""
  return comando_menu_cadastrar_usuario_IMP.processa(ses, args)
