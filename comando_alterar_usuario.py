# Este módulo processa o acionamento por um novo usuário do botão "Cadastrar" dentro
# do formulário com os dados para cadastramento, que devem estar preenchidos.

import comando_alterar_usuario_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Confirmar"
  em um formulário para alterar dados da sua conta, após ter preenchido 
  os campos do mesmo.
  
  Os novos dados devem estar definidos no dicionário {args}, e
  o ID do usuário {usr} a alterar estará em {args['id_usuario']}.
  
  A sessão {ses} não pode ser {None} e deve estar aberta.
  Se o usuário dessa conta não for um administrador, ele deve ser
  o próprio {usr}.
  
  Se os dados forem aceitáveis, a função altera os atributos do {usr},
  inclusive na base de dados; e retorna um formulário para o usuário 
  fazer login.
  
  Se os dados não forem aceitáveis, a função devolve o
  mesmo formulário de alterar usuário, com os mesmos
  dados nos campos preenchidos, mais uma ou mais mensagens
  de erro adequadas."""
  return comando_alterar_usuario_IMP.processa(ses, args)
