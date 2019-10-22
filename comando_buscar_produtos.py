# Este módulo processa o acionamento pelo usuário do botão "Buscar" (busca de
# produtos pelo nome) do menu geral, depois de preencher o campo com
# o critério de busca.

import comando_buscar_produtos_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar"
  no menu geral (ou digita ENTER no campo de busca).
  
  A condição de busca deve estar no campo {args['condicao']}.
  A função localiza todos os produtos do catálogo que satisfazem a condição
  de busca especificada, e gera uma página que mostra os mesmos em forma compacta.
  
  Por enquanto, a condição deve ser apenas uma palavra, que 
  será buscada nos campos 'descr_curta' e  'descr_media' dos 
  produtos.  A condição não pode ser vazia."""
  return comando_buscar_produtos_IMP.processa(ses, args)
