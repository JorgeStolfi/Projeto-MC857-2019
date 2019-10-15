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

def ver_produto(id_produto, qtd_produto):
  """Retorna o HTML de do formulário que mostra o identificador
  de produto {id_produto} e a quantidade {qtd_produto} (não editáveis)
  e um botão 'Ver' (de tipo 'submit').

  Quando o usuário clicar no botão 'Ver', será emitido um comando POST
  com ação {submit_ver_produto}.  Os argumentos desse
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
  vai causar a emissão de um comando POST com ação {submit_alterar_quantidade}.

  Quando o usuário clicar no botão 'Comprar', será emitido um comando
  POST com ação {submit_comprar_produto}.

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
  vai causar a emissão de um comando POST com ação {submit_alterar_quantidade}.

  Quando o usuário clicar no botão 'Excluir', será emitido um comando POST com
  ação {submit_excluir_produto}.

  Quando o usuário clicar no botão 'Ver', será emitido um comando POST com
  ação {submit_ver_produto}.

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
  com ação {submit_ver_compra}.  O único argumento desse
  POST é { 'id_compra': {id_compra} }.  O {id_compra}
  não pode ser {None}."""
  return gera_html_form_IMP.ver_compra(id_compra)

def submit_trocar_carrinho(id_compra):
  """Retorna um fragmento HTML que descreve um botão <submit> com o texto 'Carrinho',
  para uso em uma página com a descrição detalhada de um pedido de compra em aberto (carrinho).
  Por este botão o usuário pede ao servidor a troca do seu carrinho de compras."""

  return gera_html_form_IMP.submit_trocar_carrinho(id_compra)

def fechar_compra(id_compra):
  """Retorna o HTML de um formulário que mostra o identificador de compra {id_compra}
  (não editável) e um botão 'Fechar' (de tipo 'submit'). Esta função NÃO mostra
  os dados da compra.

  Quando o usuário clicar no botão 'Fechar', será emitido um comando POST
  com ação {submit_fechar_compra}.  O único argumento desse
  POST é { 'id_compra': {id_compra} }."""
  return gera_html_form_IMP.fechar_compra(cpr)

def entrar():
  """Retorna o HTML do formulário para login do usuário.
  O formulário contém campos editáveis onde o usuário deverá digitar
  o email e a senha, e um botão 'Entrar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Entrar', será emitido um comando POST
  com ação {submit_entrar}.  Os argumentos desse
  POST são { 'email': {email}, 'senha': {senha} }."""
  return gera_html_form_IMP.entrar()

def cadastrar_usuario():
  """Retorna o HTML de um formulário para para cadastro de um novo
  usuario.  O formuláro contém campos editáveis para as informações
  que o usuário deve preencher, e um botão 'Cadastrar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Cadastrar', será emitido um comando POST
  com ação {submit_cadastrar_usuario}.  Os argumentos desse
  POST são todos os atributos da classe {ObjUsuario}, exceto o identificador,
  com os valores que o usuário preencheu.  Um campo adicional 'conf_senha'
  contém a confirmação de senha."""
  return gera_html_form_IMP.cadastrar_usuario()

def alterar_usuario(usr):
  """Retorna o HTML de um formulário para para alterar dados de um novo
  usuario.  O formuláro inclui o identificador do usuário (não editável)
  e campos com as informações do usuário (editáveis, exceto 'email' e 'CPF'),
  e um botão 'Alterar' (de tipo 'submit').

  Quando o usuário clicar no botão 'Alterar', será emitido um comando POST
  com ação {submit_alterar_usuario}.  Os argumentos desse
  POST são todos os atributos da classe {ObjUsuario},
  com os valores modificados. Haverá também dois campos adicionais
  'id_usuario' com o identificador do usuário, e
  'conf_senha' com a confirmação de senha."""
  return gera_html_form_IMP.alterar_usuario(usr)
