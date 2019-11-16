# Este módulo processa o acionamento pelo usuário do botão "Buscar" (busca de
# produtos pelo nome) do menu geral, depois de preencher o campo com
# o critério de busca.

import comando_buscar_usuarios_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar"
  no menu geral (ou digita ENTER no campo de busca).

  Retorna uma lista de usuarios.
  """
  return comando_buscar_usuarios_IMP.processa(ses,args)
