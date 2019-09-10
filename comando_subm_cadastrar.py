# Este módulo processa o acionamento por um novo usuário do botão "Cadastrar" dentro
# do formulário com os dados para cadastramento, que devem estar preenchidos.

import comando_subm_cadastrar_IMP

def processa(bas, sessao, args):
  """Esta função espera que os dados do usuário estejam definidos no 
  dicionário {args}.  Cadastra o novo usuário, acrescentando-o à base de 
  dados {bas}.  Retorna a página que mostra os dados do usuário."""
  return comando_subm_cadastrar_IMP.processa(bas, sessao, args)