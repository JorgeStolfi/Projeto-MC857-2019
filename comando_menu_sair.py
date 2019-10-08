# Este módulo processa o acionamento do botão "Sair" do menu geral pelo usuário. 

import comando_menu_sair_IMP


def processa(ses):
    """Esta função é chamada quando o usuário aperta o botão "Sair" (logout)
  no menu geral de uma página da loja.
  
  A função fecha a sessão corrente {ses} dada e retorna o HTML da página 
  principal (homepage) da loja.
  
  A sessão {ses} não pode ser {None}, e deve estar aberta."""
    return comando_menu_sair_IMP.processa(ses)
