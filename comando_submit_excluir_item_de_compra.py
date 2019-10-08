# Este módulo processa a ação do usuário de excluir um produto de 

import comando_submit_excluir_item_de_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário clica num botão de "Excluir" 
  na linha de um produto {prod}, em uma página que mostra os itens de um pedido
  de compras {cpr} em aberto (um carrinho de compras).
  
  O identificador "P-{NNNNNNNN}" do produto {prod} deve estar em {args['id_produto']},
  e o identificador "C-{NNNNNNNN}" da compra {cpr} em {args['id_compra']}.
  
  A função elimina do carrinho {cpr} o item referente ao produto {prod},
  e devolve uma página HTML mostrando os itens dessa compra, atualizada.
  
  A sessão {ses} não pode ser {None}, e deve estar aberta. Além disso,
  {cpr} deve ser o carrinho de compras da sessão {ses}, e o usuário
  associado ao pedido {cpr} deve ser o usuário logado nessa sessão."""
  return comando_submit_excluir_item_de_compra_IMP.processa(ses, args)
