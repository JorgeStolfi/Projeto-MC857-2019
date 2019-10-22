# Este módulo processa o acionamento do botão "Acrescentar produto" do menu geral pelo usuário.

import comando_solicitar_form_de_dados_de_produto_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Acrescentar produto" 
  do menu geral. Retorna uma página HTML {pag}, contendo o formulario de dados para acrescentar
  um novo produto ao catálogo, que deve ser preenchido pelo usuário.
  
  A sessão {ses} deve estar aberta, isto é, o usuário deve estar logado;
  e ele deve ter privilégio de administrador do website."""
  return comando_solicitar_form_de_dados_de_produto_IMP.processa(ses, args)
