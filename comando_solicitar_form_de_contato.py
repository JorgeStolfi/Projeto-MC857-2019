# Este módulo processa o acionamento do botão "Entrar" (login) do menu principla pelo usuário.

import comando_solicitar_form_de_contato_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Contato"
  no menu geral de uma página qualquer.

  A sessão corrente {ses} e o dicionário de argumentos {args}
  são irrelevantes e podem ser {None}.

  A função retorna a página HTML {pag}, com o formulário para o usuário mandar uma mensagem
  (com campos "mensagem" e "senha", e um botão de sumbissão)."""
  return comando_solicitar_form_de_contato_IMP.processa(ses, args)
