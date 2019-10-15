# Este módulo processa a acao do usuario que consiste em pedir para ver a lista de todos os
# pedidos de compras do usuário, em qualquer estado.

import comando_submit_finalizar_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Finalizar" ou equivalente, 
  numa página que mostra um pedido de compras {cpr} em aberto (isto é, um carrinho de compras).

  O campo {args['id_compra']} deve existir e deve ser o identificador
  "C-{NNNNNNNN}" da compra {cpr} a fechar.
  
  O usuário associado à compra {cpr} deve ser o mesmo associado à sessão {ses}
  (que não pode ser {None}, e deve estar aberta).
  
  A função muda o status do pedido {cpr} para 'pagando' Se a compra
  {cpr} for o carrinho de compras da sessão {ses}, também troca este por
  por um novo carrinho vazio.
  
  Em qualquer caso, se a operação der certo, devolve uma página HTML que mostra o
  pedido de compra {cpr}, no seu novo estado."""
  return comando_submit_finalizar_compra_IMP.processa(ses, args)
