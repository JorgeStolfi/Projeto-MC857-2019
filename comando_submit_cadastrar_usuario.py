# Este módulo processa o acionamento por um novo usuário do botão "Cadastrar" dentro
# do formulário com os dados para cadastramento, que devem estar preenchidos.

import comando_submit_cadastrar_usuario_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Cadastrar"
  em um formulário para cadastrar um novo usuário, após ter preenchido
  os campos do mesmo.  
  
  Os dados para cadastro devem estar definidos no dicionário {args}. 
  
  Se os dados forem aceitáveis, a função cria o novo usuário {usr},
  acrescentando-o à base de dado; e retorna um formulário 
  para o usuário fazer login (com campos para email e senha,
  e um botão "Entrar").
  
  Se os dados nao forem aceitáveis,a função devolve o
  mesmo formulário de cadastrar usuário, com os mesmos
  dados nos campos preenchidos, mais uma mensagem de erro adequada."""
  return comando_submit_cadastrar_usuario_IMP.processa(ses, args)
