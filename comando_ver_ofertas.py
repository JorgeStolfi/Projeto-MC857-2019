# Este módulo processa o acionamento do botão "Entrar" (login) do menu principla pelo usuário.

import comando_ver_ofertas_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Ofertas" 
  no menu geral de uma página qualquer.
  
  A sessão corrente {ses} e o dicionário de argumentos {args}
  são irrelevantes e podem ser {None}.  
  
  A função retorna a página HTML {pag}, com uma lista de produtos 
  que tem o atributo 'oferta' com valor {True}."""
  return comando_ver_ofertas_IMP.processa(ses, args)
