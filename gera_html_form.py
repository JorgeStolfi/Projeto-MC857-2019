# Interface do módulo {gera_html_form}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem formularios <form>...</form>.

# Para devolver um destes formulários ao browser do usuário,
# é necessário acrescentar pelo menos um cabeçalho e rodapé HTML;
# por exeplo incluindo-o como conteúdo de {gera_html_pag.generica}.

# Implementação desta interface:
import gera_html_form_IMP

# Funções exportadas por este módulo:

def buscar_produtos():
  """Retorna HTML de um formulario para busca textual no cadastro de produtos.
  O formulário contém um campo editável onde o usuário entra a palavra a
  procurar, e um botão de 'Buscar' que solicita a busca ao servidor."""
  return gera_html_form_IMP.buscar_produtos()


def compras_de_produto():
  """Retorna HTML de um formulario para busca textual de compras de produtos.
  O formulário contém um campo editável onde o usuário entra o identificador do
  produto a ser procurado, e um botão de 'Compras de Produtos' 
  que solicita a busca ao servidor."""
  return gera_html_form_IMP.compras_de_produto()

def buscar_objeto():
  """Retorna HTML de um formulario para busca textual de objetos.
  O formulário contém um campo editável onde o usuário entra a palavra a
  procurar, e um botão de 'Buscar' que solicita a busca ao servidor."""
  return gera_html_form_IMP.buscar_objeto()

def ver_produto(id_produto, qtd_produto):
  """Retorna o HTML de do formulário que mostra o identificador
  de produto {id_produto} e a quantidade {qtd_produto} (não editáveis)
  e um botão 'Ver' (de tipo 'submit').

  Quando o usuário clicar no botão 'Ver', será emitido um comando POST
  com ação {ver_produto}.  Os argumentos desse
  POST serão { 'id_produto': {id_produto}, 'quantidade': {qtd_produto} }.

  Se {qtd_produto} for {None}, esse campo é omitido do formulário
  e dos argmentos."""
  return gera_html_form_IMP.ver_produto(id_produto, qtd_produto)

def comprar_produto(id_compra, id_produto, qtd_produto):
  """Retorna o HTML de do formulário que mostra o identificador
  de produto {id_produto} (não editável), um campo com quantidade editável,
  e um botão 'Comprar' (de tipo 'submit'). Esta função NÃO mostra os dados do produto.

  A quantidade é apresentada em um campo numérico editável, com conteúdo
  inicial {qtd_produto}. Qualquer alteração feita pelo usuário nesse campo
  vai causar a emissão de um comando POST com ação {alterar_qtd_de_produto}.

  Quando o usuário clicar no botão 'Comprar', será emitido um comando
  POST com ação {comprar_produto}.

  Nos dois casos, os argumentos incluídos no POST são
  { 'id_compra': {id_compra}, 'id_produto': {id_produto}, 'quantidade': {qtd1} },
  onde {qtd1} é a quantidade escolhida pelo usuário.  Se {id_compra} for {None},
  esse argumento é omitido no comando POST."""
  return gera_html_form_IMP.comprar_produto(id_compra, id_produto, qtd_produto)

def alterar_quantidade(id_compra, id_produto, qtd_produto):
  """Retorna o HTML de do formulário que mostra o identificador de
  produto {id_produto} (não editável), um campo com quantidade (editável),
  e botões 'Ver' e 'Excluir' (de tipo 'submit'). Esta função NÃO mostra
  os dados do produto ou da compra.

  A quantidade é apresentada em um campo numérico editável, com conteúdo
  inicial {qtd_produto}. Qualquer alteração feita pelo usuário nesse campo
  vai causar a emissão de um comando POST com ação {alterar_qtd_de_produto}.

  Quando o usuário clicar no botão 'Excluir', será emitido um comando POST com
  ação {excluir_item_de_compra}.

  Quando o usuário clicar no botão 'Ver', será emitido um comando POST com
  ação {ver_produto}.

  Nos três casos, os argumentos incluídos no POST são
  { id_compra': {id_compra}, 'id_produto': {id_produto}, 'quantidade': {qtd1} },
  onde {qtd1} é a quantidade escolhida pelo usuário (irrelevante
  no caso de excluir).

  O campo {id_compra} não é mostrado no formulário. Se {id_compra} for {None},
  esse argumento tambem é excluído dos argumentos do comando POST."""
  return gera_html_form_IMP.alterar_quantidade(id_compra, id_produto, qtd_produto)

def ver_compra(id_compra):
  """Retorna o HTML de um formulário que mostra o identificador de compra {id_compra}
  (não editável) e um botão 'Ver' (de tipo 'submit'). Esta função NÃO mostra os dados da compra.

  Quando o usuário clicar no botão 'Ver', será emitido um comando POST
  com ação {ver_compra}.  O único argumento desse
  POST é { 'id_compra': {id_compra} }.  O {id_compra}
  não pode ser {None}."""
  return gera_html_form_IMP.ver_compra(id_compra)

def trocar_carrinho(id_compra):
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'Carrinho',
  para uso em uma página com a descrição detalhada de um pedido de compra em aberto (carrinho).
  Por este botão o usuário pede ao servidor a troca do seu carrinho de compras."""
  return gera_html_form_IMP.trocar_carrinho(id_compra)

def fechar_compra(id_compra):
  """Retorna o HTML de um formulário que mostra o identificador de compra {id_compra}
  (não editável) e um botão 'Fechar' (de tipo 'submit'). Esta função NÃO mostra
  os dados da compra.

  Quando o usuário clicar no botão 'Fechar', será emitido um comando POST
  com ação {submit_fechar_compra}.  O único argumento desse
  POST é { 'id_compra': {id_compra} }."""
  return gera_html_form_IMP.fechar_compra(cpr)

def excluir_item_de_compra(prod_id, compr_id):
  # !!! Documentar !!!
  return gera_html_form_IMP.excluir_item_de_compra(prod_id, compr_id)

def alterar_qtd_de_produto(qtd, prod_id, compr_id):
  # !!! Documentar !!!
  return gera_html_form_IMP.alterar_qtd_de_produto(qtd, prod_id, compr_id)

def entrar():
  """Retorna o HTML do formulário para login do usuário.
  O formulário contém campos editáveis onde o usuário deverá digitar
  o email e a senha, e um botão 'Entrar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Entrar', será emitido um comando POST
  com ação {fazer_login}.  Os argumentos desse
  POST são { 'email': {email}, 'senha': {senha} }."""
  return gera_html_form_IMP.entrar()

def contato():
  """Retorna o HTML do formulário para contato.
  O formulário contém campos editáveis onde o usuário deverá digitar
  a mensagem, e um botão 'Enviar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Enviar', será emitido um comando POST
  com ação {enviar_mensagem}.  Os argumentos desse
  POST são { 'email': {email}, 'mensagem': {mensagem} }."""
  return gera_html_form_IMP.contato()

def cadastrar_usuario(atrs, admin):
  """Retorna o formulário de cadastrar novo usuario.

  O formuláro contém campos editáveis para as informações que o usuário
  deve preencher.  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos.

  O parâmetro {admin} diz que o usuário que pediu a criação do usuário
  (NÃO o usuário que está sendo cadastrado!) é administrador. Se for {True}, o
  formulário vai mostrar um checkbox para definir o novo usuário como
  administrador.

  O formulário conterá um botão 'Cadastrar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {cadastrar_usuario}.  Os argumentos desse POST são todos os atributos da classe {ObjUsuario},
  com os valores de {atrs} que o usuário deve ter preenchido.  Um argumento
  adicional 'conf_senha' conterá a confirmação de senha.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return gera_html_form_IMP.cadastrar_usuario(atrs, admin)

def alterar_usuario(id_usuario, atrs, admin):
  """Retorna o formulário de alterar dados da conta
  do usuario {usr} cujo identificador é {id_usuario}.

  O formuláro contém campos editáveis com os atributos
  correntes do usuário, especificados no dicionário {atrs}.
  O valor de {atrs['senha']} não será mostrado, e haverá um
  campo adicional 'conf_senha'.

  O parâmetro {admin} diz que o usuário que pediu a alteração (NÃO o
  usuário que está sendo alterado!) é administrador. Se for {True}, o
  formulário vai mostrar um checkbox para definir o usuário {usr} como
  administrador, e vai mostrar também o campo {id_usuario} como "readonly".

  Se {admin} for {False}, supõe-se que o formulário foi
  pedido pelo próprio {usr}, que é um cliente comum.

  O formulário conterá um botão 'Alterar' (de tipo 'submit').
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  {alterar_usuario}.  Os argumentos desse POST são todos os atributos da classe
  {ObjUsuario}, com os valores de {atrs} a menos de altetações feitas pelo
  usuário, mais o atributo 'conf_senha'.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'principal'."""
  return gera_html_form_IMP.alterar_usuario(id_usuario, atrs, admin)

def escolher_pagamento(id_compra, atrs):
  """Retorna o HTML de um formulário para escolher o meio de pagamento, e entrar os
  dados do cartão de crédito.
  O formulário contém a seleção do meio de pagamento, os campos
  editaveis relacionados ao cartão de crédito(nome,numero, data de validade e
  codigo de segurança) e um botão "Confirmar".

  Os valores iniciais dos campos serão obtidos do dicionário {atrs}, se não
  for {None}.

  Quando o usuário clicar no botão "Confirmar" ,será emitido um comando POST com ação
  {definir_meio_de_pagamento}.Os argumentos desse POST serão as informações do
  cartão de crédito."""
  return gera_html_form_IMP.escolher_pagamento()

def preencher_endereco(id_compra, atrs):
  """Retorna o HTML de um formulário para preenchimento do endereço do pedido de
  compra com identificador {id_compra}. O formulário contém campos editáveis
  com nomes 'endereco_1', 'endereco_2', 'cidade_UF', e 'CEP', cujos valores iniciais
  devem ser obtidos do dicionário {atrs}; e um botão "Confirmar".

  Quando o usuário clicar no botão "Confirmar" ,será emitido um comando POST com ação
  {definir_endereco}. Os argumentos desse POST serão os campos acima. """
  return gera_html_form_IMP.preencher_endereco(id_compra, atrs)

def buscar_identificador():
  """Retorna HTML de um formulario para busca textual no identificador do
  cadastro de produtos.  O formulário contém um campo editável onde o usuário entra
  o identificador na forma "{L}-{NNNNNNNN}", onde {L} pode ser "P", "C", "S", ou "U"
  que deseja procurar, e um botão de 'Ver' que solicita o produto ao servidor."""
  return gera_html_form_IMP.buscar_identificador()

def acrescentar_produto(ses):
  """Retorna o HTML de um formulario para acrescentar algum produto"""
  return gera_html_form_IMP.acrescentar_produto(ses)

