# Este módulo processa o acionamento do botão "Cadastrar" do menu geral 
# pelo usuário.

import comando_solicitar_form_de_cadastrar_usuario_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Cadastrar usuário"
  do menu geral.  Ela retorna um formulário para cadastrar um novo usuário.
  Vide {gera_html_pag.cadastrar_usuario}.
  
  A sessão {ses} pode ser {None}. Se não for {None} e o usuário 
  dessa sessão for administrador, o formulário tem campos adicionais."""
  return comando_solicitar_form_de_cadastrar_usuario_IMP.processa(ses, args)
