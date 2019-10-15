# Este módulo processa o acionamento do botão "Acrescentar produto" do menu geral pelo usuário.

import comando_menu_acrescentar_produto_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Acrescentar produto" do menu geral.
  
  Retorna uma página HTML contendo o formulario de dados para acrescentar um novo produto ao catálogo,
  que deve ser preenchido pelo usuário.  A sessão {ses} e or argumentos {args} são irrelevantes
  e podem ser {None}."""
  return comando_menu_acrescentar_produto_IMP.processa(ses, args)
