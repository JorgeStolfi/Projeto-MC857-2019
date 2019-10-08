# Este módulo processa a acao do usuario que consiste em pedir para ver a lista de todos os 
# pedidos de compras do usuário, em qualquer estado.

import comando_submit_finalizar_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário {urs} que está logado na sessão {ses}
  aperta o botão "Finlizar compra" ou equivalente, numa página que mostra
  um pedido de compras {cpr} em aberto (isto é, um carrinho de compras).
  
  A função localiza o pedido de compras {cpr} pelo seu identificador "C-{NNNNNNNN}",
  que deve estar em {args['id_compra']}.  O usuário associado ao pedido 
  deve ser {usr} e (por enquanto) o pedido associado à sessão deve ser {cpr}. 
  A sessão {ses} não pode ser {None}, e deve estar aberta
  
  A função muda o status do pedido {cpr} para 'pagando', e troca 
  o carrinho da sessão {ses} por um novo carrinho vazio.
  Finalmente, devolve uma página HTML que mostra o pedido de
  compra {cpr}, no seu novo estado."""
  return comando_submit_finalizar_compra_IMP.processa(ses, args)
    
