# Este módulo processa o acionamento do botão "Minha conta" do menu geral 
# pelo usuário.

import comando_solicitar_form_de_alterar_usuario_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Minha conta" 
  ou equivalente do menu geral.
  
  O identificador do usuário {usr} a alterar dever estar em 
  {args['id_usuario']}.  O formulário vai mostrar os atributos correntes
  desse usuário (menos a senha) em campos editáveis.
  
  A sessão {ses} não pode ser {None} e deve estar aberta (isto é, o usuário
  precisa estar logado). A sessão deve pertencer a esse usuário, ou a um usuário
  com privilégios de administrador.  Vide {gera_html_pag.alterar_usuario}."""
  return comando_solicitar_form_de_alterar_usuario_IMP.processa(ses, args)
