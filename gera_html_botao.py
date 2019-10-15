# -*- coding: utf-8 -*-

# Interface do módulo {gera_html_botao}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem elementos do tipo "<button>" ou
# "<input type=submit>", para uso em várias páginas.

# Implementação desta interface:
import gera_html_botao_IMP

# As funções abaixo geram botões de tipo "<button>" que emitem comandos "GET":

def principal():
  """Retorna um fragmento de HTML que produz o botao "Principal" que 
  manda o usuário para a página principal (homepage) da loja."""
  return gera_html_botao_IMP.principal()

def menu_entrar():
  """Retorna um fragmento de HTML que produz o botao de "Entrar" (login) para uso no menu
  principal.  
  
  Este botão permite que o usuário solicite ao servidor um formulário para fazer login.
  Ele será exibido em todas as páginas quando o usuário estiver navegando 
  pelo site sem estar logado. """
  return gera_html_botao_IMP.menu_entrar()

def menu_sair():
  """Retorna um fragmento de HTML que produz o botao "Sair" (logout) para uso no menu geral.
  
  Este botão permite que o usuário faça o logout da sessao corrente.
  Ele será exibido em todas as páginas enquanto o usuário estiver logado."""
  return gera_html_botao_IMP.menu_sair()

def menu_cadastrar():
  """Retorna um fragmento de HTML que produz o botao "Cadastrar" para uso no menu geral.
  Este botão permite que o usuário solicite ao servidor um formulário para 
  cadastrar um novo usuário. Ele será exibido em todas as páginas."""
  return gera_html_botao_IMP.menu_cadastrar()

def menu_carrinho():
  """Retorna um fragmento de HTML que produz o botao "Carrinho" para uso no menu geral.
  Este botão permite que o usuário solicite ao servidor uma página que mostra o estado
  atual do seu carrinho de compras."""
  return gera_html_botao_IMP.menu_carrinho()

def menu_ofertas():
  """Retorna um fragmento de HTML que produz o botao "Ofertas" para uso no menu geral.
  Este botão permite que o usuário solicite ao servidor uma página que mostra as ofertas
  atualmente disponíveis."""
  return gera_html_botao_IMP.menu_ofertas()

def erro_ok():
  """Retorna um fragmento de HTML que produz o botao de botão que vai ser incluído em páginas de erro.
  Quando o usuário clica nesse botão, ele é redirecionado para a página principal
  (homepage) da loja."""
  return gera_html_botao_IMP.erro_ok()

# As funções abaixo geram botões "<input type=submit>" para uso dentro de "<form>...</form>":

def submit_ver_produto():
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'VER', 
  para uso em um bloco de descrição resumida do produto.  Por este botão
  o usuário pede ao servidor uma página mostrando o produto em detalhe."""
  return gera_html_botao_IMP.submit_ver_produto()

def submit_comprar_produto():
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'COMPRAR',
  para uso em uma página com descrição detalhada de um produto.  Por este botão
  o usuário pede ao servidor a inclusão do produto no seu carrinho de compras. """
  return gera_html_botao_IMP.submit_comprar_produto()

def submit_excluir_produto():
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'EXCLUIR',
  para uso em uma página com a descrição detalhada de um pedido de compra em aberto (carrinho).
  Por este botão o usuário pede ao servidor a exclusão do produto do seu carrinho de compras. """
  return gera_html_botao_IMP.submit_excluir_produto()

def submit_buscar_produtos():
  """Retorna HTML um fragmento HTML que descreve um botão <submit> com o texto 'BUSCAR',
  para uso em formulario de busca de produtos por palavras. Por este botão
  o usuário pede ao servidor que mostre a lista de todos os produtos que 
  satisfazem um critério especificado."""
  return gera_html_botao_IMP.submit_buscar_produtos()
  
def submit_cadastrar_usuario():
  """Gera apenas o o botão "cadastrar" que vai estar dentro de um <form>...</form>, dentro da página de cadastrar novo usuário"""
  return gera_html_botao_IMP.submit_cadastrar_usuario()

def submit_entrar():
  """Retorna o botão para a submissão de entrar"""
  return gera_html_botao_IMP.submit_entrar()
