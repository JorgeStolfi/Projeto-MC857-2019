# Este módulo processa o acionamento pelo usuário do botão "Buscar" (busca de
# produtos pelo nome) do menu principal, depois de preencher o campo com
# o critério de busca.

import comando_subm_buscar_produtos_IMP

def processa(bas, sessao, args):
  """A condição de busca deve estar no campo {args['condicao']}.
  Localiza todos os produtos do catálogo que satisfazem essa condição,
  e gera uma página que mostra os mesmos em forma compacta.
  
  Por enquanto, a condição deve ser apenas uma palavra que 
  deve aparecer nos campos 'descr_curta' e  'descr_media' dos 
  produtos."""
  return comando_subm_buscar_produtos_IMP.processa(bas, sessao, args)
