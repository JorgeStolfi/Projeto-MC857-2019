# Este módulo processa a seleção pelo usuário de um compra numa página 
# com uma lista de vários compras, a fim de ver a descrição detalhada
# do mesmo.

import comando_submit_ver_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário {usr} logado na sessão {ses} 
  aperta o botao "Ver detalhes" ou equivalente numa linha da lista de seus 
  pedidos de compra, para ver os itens de um determinado pedido {cpr}.
  
  O identificador "C-{NNNNNNNN}" do pedido de compra {cpr} desejado 
  deve estar em {args['id_compra']}.
  
  A função devolve uma página HTML que mostra os itens desse pedido de
  compra. Para cada item do pedido, mostra uma imagem pequena, a
  descrição curta do produto, a quantidade pedida, e o preço unitário e
  total do item.  Se o usuário clicar na imagem ou na descrição do
  produto, deve ser emitido um comando HTTP "submit_ver_produto" com a
  quantidade que consta do pedido.

  Se a compra ainda estiver aberta (isto é, for um carrinho de compras),
  a página deve ser a mesma que seria devolvida por
  {comando_menu_ver_carrinho.processa}: ou seja, a quantidade deve ser
  alterável, e deve haver um botão para e excluir o item.
  
  A sessão não pode ser {None} e deve estar aberta, e o usuário {usr} deve ser
  dono do pedido de compras {cpr}."""
  return comando_submit_ver_compra_IMP.processa(ses, args)
