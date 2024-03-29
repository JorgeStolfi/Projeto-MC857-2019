# Interface do módulo {gera_html_elem}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5, usados em várias páginas.

# Implementação desta interface:
import gera_html_elem_IMP

# Funções exportadas por este módulo:

# ELEMENTOS PRINCIPAIS DE UMA PÁGINA

def cabecalho(title, grande):
  """Retorna o cabecalho padrão site, com o strin {title} no titulo da página .
  O parâmetro booleano {grande} especifica o tamanho do título e do cabeçalho:
  {True} é apropriado para a página de entrada, {False} para as demais páginas."""
  return gera_html_elem_IMP.cabecalho(title, grande)

def rodape():
  """Retorna o rodapé padrão do site."""
  return gera_html_elem_IMP.rodape()

def menu_geral(logado, nome_usuario, admin):
  """Retorna o menu geral, que será mostrado no alto da maioria das páginas do site.  
  
  O parâmetro {logado} deve ser {True} se o usuário estiver logado; 
  nesse caso {nome_usuario} deve ser seu nome.  Se for {False}, o nome
  será ignorado.
  O parâmetro booleano {admin} diz se o usuário é administrador"""
  return gera_html_elem_IMP.menu_geral(logado, nome_usuario, admin)
  
# ELEMENTOS ESPECÍFICOS

def bloco_de_erro(msg):
  """Retorna um fragmento de HTML que contém a mensagem {msg},
  e um botão "OK" que retorna para a página principal da loja.
  A mensagem pode incluir quebras de linha '\n'."""
  return gera_html_elem_IMP.bloco_de_erro(msg)

def bloco_de_produto(id_compra, prod, qtd, detalhe):
  """Devolve um fragmento HTMP que decreve o produto {prod}, um objeto da classe {ObjProduto}.
  
  Se {detalhe} for {False}, mostra apenas o identificador do produto,
  a descrição curta e a descrição média, com uma imagem pequena,
  e um botão "Ver" que permite ver mais detalhes. Se {detalhe} for {True}, mostra também
  a descrição detalhada, a quantidade em estoque, etc., com uma imagem maior,
  e um botão "Comprar".
  
  O parâmetro {id_compra}, se não for {None}, será incluído nos argumentos do POST
  gerado pelo botão "Comprar".  Nesse caso, deve ser o identificador do pedido de
  compra ao qual o produto deve ser acrescentado.
  
  Em qualquer caso, se {qtd} não for {None}, mostra a quantidade {qtd}
  e o preço para essa quantidade.  Se {qtd} for {None},
  mostra apenas o preço unitário, sem a quantidade."""
  return gera_html_elem_IMP.bloco_de_produto(id_compra, prod, qtd, detalhe)

def bloco_de_usuario(user):
  """Devolve um fragmento HTML que decreve o usuãrio {user}, um objeto da classe {ObjUsuario}."""
  return gera_html_elem_IMP.bloco_de_usuario(user)

def bloco_de_lista_de_produtos(idents):
  """Dada uma lista {idents} de identificadores de produtos,
  retorna o HTML da descrição resumida de todos esses produtos.

  Cada descrição será gerada por
  {gera_html_elem.bloco_de_produto(None, prod, qtd, False)},
  e terá um botão 'Ver' para mostrar a descrição detalhada."""
  return gera_html_elem_IMP.bloco_de_lista_de_produtos(idents)

def bloco_de_lista_de_usuarios(idents):
  """Dada uma lista {idents} de identificadores de usuarios,
  retorna o HTML da descrição resumida de todos esses usuarios.

  Cada descrição será gerada por
  {gera_html_elem.bloco_de_usuario(user)},
  e terá um botão 'Ver' para mostrar a descrição detalhada."""
  return gera_html_elem_IMP.bloco_de_lista_de_usuarios(idents)

def bloco_de_compra(cpr, detalhe):
  """Devolve um fragmento HTML que mostra os dados da compra {cpr}, um objeto 
  da classe {ObjCompra}.   
  
  Se {detalhe} for {False}, mostra apenas os dados principais da compra:  seu 
  identificador "C-{NNNNNNNN}", o status do pedido, a data da última 
  alteração de status, o número de itens, o valor total a pagar (incluindo frete),
  e um botão "Ver detalhes" que emite ao servidor um comando 'ver_compra'.
    
  Se {detalhe} for {True}, mostra também o endereço e CEP de entrega,
  o meio de pagamento escolhido, os itens da compra, o preço total dos 
  itens (sem frete) e o custo do frete. Para cada item da lista será apresentado 
  um bloco como descrito em {gera_html_elem.bloco_de_produto(id_compra,prod,qtd,detalhe=False)}.
  
  Se {detalhe} for {True} e o estado da compra for 'aberto', mostra também
  um botão 'Alterar endereço' que emite o comando 'solicitar_form_de_endereco';
  um botão 'Alterar meio de pagamento', que manda
  o comado 'solicitar_form_de_meio_de_pagamento' para o servidor; e um botão 'Finalizar'
  que manda o comando 'finalizar_compra' para o servidor.
  
  Além disso, se o estado da compra for 'aberto', qualquer que seja o valor de {detalhe}, 
  mostra também um botão 'Definir carrinho' que emite o comando 'botao_definir_carrinho'
  para o servidor."""
  return gera_html_elem_IMP.bloco_de_compra(cpr, detalhe)

# ELEMENTOS SIMPLES

def bloco_texto(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo):
  """Retorna un string que é um fragmento HTML consistindo do {texto}
  dado, que pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>'). O fragmento todo é um domínio  {span(estilo,texto)}
  com o {estilo} apropriado.
  
  O parâmetro {disp} é o valor do atributo 'display' do estilo, por exemplo 
  'block' ou 'inline-block'. 

  Os parâmetros {fam_fonte}, {tam_fonte} e {peso_fonte} especificam a família e o
  tamanho do fonte a usar (por exemplo 'Helvetica','18px','bold').

  O parâmetro {pad}, especifica a largura do espaço extra ('padding') em
  volta do texto como um todo.

  O parâmetro {halign} especifica o alinhamento das linhas do texto;
  pode ser 'left', 'center', ou 'right'.

  Os parâmetros {cor_texto} e {cor_fundo} devem ser cores aceitáveis no
  CSS (por exemplo, '#ff8800').

  Cada parâmetro de estilo pode ser {None} para indicar a omissão
  do atributo no estilo. O atributo então herda o defô
  do contexto ou de especificações de estilo CSS globais."""
  return gera_html_elem_IMP.bloco_texto(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo)

def input(rotulo, tipo, nome, val_ini, dica, cmd):
  """Gera o HTML para um campo de dados "<input ... />" com atributos dados.
  Este fragmento geralmente é incluído em um formulário "<form>...</form>".
  
  O parâmetro {rotulo} é um rótulo opcional. Se não for {None}, será inserido na frente
  do elemento "<input.../>" na meio de um elemento "<label>{rotulo}</label>".
  
  O parâmetro {tipo} é o tipo de campo, por exemplo "text", "email", "readonly",
  "hidden", "password", "number", etc. (resulta em "<input type='{tipo}'.../>").
  
  O parâmetro {nome} é o nome do campo, que será usado para enviar 
  o valor do mesmo ao servidor (resulta em "<input ... name='{nome}' id='{nome}'.../>"). 
  Quando o comando POST do formulário for emitido, este campo
  será enviado como um par {nome}: {val_fin} nos argumentos do POST,
  onde {val_fin} é o valor fornecido pelo usuário.
  
  O parâmetro {val_ini} é o valor inicial do campo (resulta em 
  "<input ... value='{val_ini}'.../>"). Se for {None}, esse atributo é omitido e o
  valor do campo será inicialmente nulo. Senão, {val_ini} deve ser
  uma string.  Se o usuário não editar o campo, {val_ini}
  será devolvido ao servidor no POST do formulário, como valor desse campo.
  
  O parâmetro {dica} é um texto que será mostrado no campo, se {val_ini} for {None},
  para orientar o preenchimento (resulta em "<input ... placeholder='{dica}' .../>").
  Este campo NÃO será devolvido ao servidor Se for {None}, o campo estará inicialmente em branco.
  
  O parâmetro {cmd}, se não for {None}, é o comando que será enviado ao 
  servidor via POST, quando o usuário alterar este campo, em vez do
  "action" default do formulário."""  
  return gera_html_elem_IMP.input(rotulo, tipo, nome, val_ini, dica, cmd)

def label(rotulo, sep):
  """Deolve o elemento HTML "<label>{rotulo}{sep}</label>",
  ou "" se o {rotulo} for {None} ou a cadeia vazia ."""
  return gera_html_elem_IMP.label(rotulo, sep)

def tabela(linhas):
  """Gera o HTML para uma tabela "<table>...</table>".
  
  O parâmetro {linhas} deve ser uma lista ou tupla cujos elementos descrevem as linhas.
  Cada elemento de {linhas} deve ser uma list ou tupla de fragmentos HTML, que são 
  inseridos nas células da linha correspondente da tabela."""
  return gera_html_elem_IMP.tabela(linhas)

# FORMATAÇÃO HTML GENÉRICA

# Nas funções desta seção, o parâmetro {estilo} é uma série de especificações 
# de estilo HTML, como "font-size: 12px; color: 'ff2200'", e pode ser vazio.

# O parâmetro {conteudo} pode conter tags de HTML (como '<b>', '<i>') e quebras de
# linha ('<br/>').

def span(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como um domínio ('<span style="{estilo}">...</span>')."""
  return gera_html_elem_IMP.span(estilo, conteudo)
 
def div(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como uma divisão '<div style="{estilo}">...</div>')."""
  return gera_html_elem_IMP.div(estilo, conteudo)
 
def paragrafo(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como um parágrafo ('<p style="{estilo}">...</p>')."""
  return gera_html_elem_IMP.paragrafo(estilo, conteudo)

def form(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo de um <form>...</form>
  com método "post" e o {conteudo} dado (que deve ter os <input>s necessários).
  Note que um <form> não pode ocorrer dentro de um parágrafo."""
  return gera_html_elem_IMP.form(estilo, conteudo)
