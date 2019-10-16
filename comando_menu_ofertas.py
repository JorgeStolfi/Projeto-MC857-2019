# Este módulo processa o acionamento do botão "Entrar" (login) do menu principla pelo usuário.

import comando_menu_ofertas_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Ofertas" 
  no menu geral de uma página qualquer.  
  
  A função retorna a página HTML com uma lista de 10 produtos cujo 
  preço é menor que R$20.00
  
  A sessão corrente {ses} e o dicionário de argumentos {args}
  são irrelevantes e podem ser {None}."""
  return comando_menu_ofertas_IMP.processa(ses, args)
