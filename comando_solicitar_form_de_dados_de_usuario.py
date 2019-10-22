# Este módulo processa o acionamento do botão "Cadastrar" ou "Minha conta" do menu geral 
# pelo usuário.

import comando_solicitar_form_de_dados_de_usuario_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Cadastrar usuário"
  ou "Minha conta" ou equivalente do menu geral.
  
  Se o campo {args['id_usuario']} não existir, a função retorna um formulário
  para cadastrar um novo usuário. Nesse caso, a sessão {ses} é irrelevante e pode
  ser {None}.  O formulário é definido por {gera_html_pag.cadastrar_usuario(ses)}.
  
  Se o campo {args['id_usuario']} estiver definido, a função retorna um formulário
  que mostra os dados do usuário {usr} com esse identificador, menos a senha. 
  Neste caso a sessão {ses} não pode ser {None} e deve estar aberta (isto é, o usuário
  precisa estar logado). A sessão deve pertencer a esse usuário, ou a um usuário
  com privilégios de administrador.  Vide {gera_html_pag.mostrar_usuario(ses,usr)}.
  """
  return comando_solicitar_form_de_dados_de_usuario_IMP.processa(ses, args)
