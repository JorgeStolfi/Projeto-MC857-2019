# Este módulo processa o acionamento por um novo usuário do botão "Acrescentar" dentro do formulário com os dados para cadastramento de um produto na loja (pelo administrador)

import comando_submit_acrescentar_produto_IMP

def processa(ses, args):
  """Esta função é chamada quando o administrador aperta o botão "Acrescentar"
  em um formulário para cadastrar um novo produto, após ter preenchido
  os campos do mesmo.  
  
  Os dados para cadastro devem estar definidos no dicionário {args}. 
  
  Se os dados forem aceitáveis, a função cria o novo produto {prod},
  acrescentando-o à base de dado.
  
  Se os dados nao forem aceitáveis,a função devolve o
  mesmo formulário de cadastro de produto, com os mesmos
  dados nos campos preenchidos, mais uma mensagem de erro adequada."""
  return comando_submit_acrescentar_produto_IMP.processa(ses, args)
