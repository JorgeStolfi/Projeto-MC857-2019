# Este módulo processa o acionamento do botão "Ver Carrinho" do menu geral pelo usuário.

import comando_ver_carrinho_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário que está logado na sessão {ses} aperta o 
  botão "Ver Carrinho" no menu geral.
  
  A sessão não pode ser {None} e deve estar aberta, e o usuário {usr} deve ser
  dono do pedido de compras {cpr}. 
  
  A função retorna uma página HTML {pag} que mostra os itens atualmente no
  carrinho {cpr} dessa sessão. Para cada item do pedido, mostra uma
  imagem pequena a descrição curta do produto, a quantidade pedida, e o
  preço unitário e total do item. Se o usuário clicar na imagem ou na
  descrição do produto, deve ser emitido um comando HTTP
  "ver_produto" com a quantidade que consta do pedido.
  
  O campo de quantidade deve ser alterável, e alteração no mesmo deve
  causar um comando HTTP "alterar_qtd_de_produto". Deve tabém haver um botão
  "Excluir" em cada item, que gera o comando
  "excluir_item_de_compra."""
  return comando_ver_carrinho_IMP.processa(ses, args)
