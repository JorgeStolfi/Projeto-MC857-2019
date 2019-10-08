import comando_submit_entrar_IMP

# !!! Testar este módulo !!!

def processa(ses, dados):
  """Esta função é chamada quando o usuário (que não deve estar cadastrado) 
  aperta o botão "Entrar" no formulário de login.  Recebe no dicionário {dados}
  os campos 'email' e 'senha' que o usuário preencheu nesse formulário. 
  Deve criar uma nova uma sessão para esse usuário, com um novo cookie; 
  e devolver a página de entrada."""
  return comando_submit_entrar_IMP.processa(ses, dados)
