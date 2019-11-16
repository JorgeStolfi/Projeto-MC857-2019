# Este módulo processa a acao do usuario que consiste em pedir para adicionar uma nova compra
# e alterar seu carrinho pra essa compra vazia.

import comando_nova_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Nova Compra", 
  na página "Minhas Compras".
  
  A função cria uma nova compra vazia e altera o carrinho pra essa compra.
  
  Em qualquer caso, se a operação der certo, devolve uma página HTML que mostra a
  lista atualizada de compras do usuário"""
  return comando_nova_compra_IMP.processa(ses, args)
