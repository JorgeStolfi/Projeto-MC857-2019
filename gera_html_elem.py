# Interface do módulo {gera_html_elem}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5, usados em várias páginas.

# Implementação desta interface:
import gera_html_elem_IMP

# Funções exportadas por este módulo:

def cabecalho(title):
  """Retorna o cabecalho padrão site, com titulo da página {title}."""
  return gera_html_elem_IMP.cabecalho(title)

def rodape():
  """Retorna o rodapé padrão do site."""
  return gera_html_elem_IMP.rodape()

def menu_geral():
  """Retorna o menu geral do site."""
  # !!! Precisa acrescentar parâmetro que diz se usuário está logado para saber se mostra botão "Entrar" ou "Sair" !!!
  # !!! Precisa acrescentar botão "Carrinho" para mostrar carrinho, se usuário está logado.  Tem que criar {comando_botao_carrinho.py} !!!
  # !!! Precisa acrescentar botão "Principal" para mostrar página de entrada.  Tem que criar {comando_botao_principal.py} !!!
  return gera_html_elem_IMP.menu_geral()

def span(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como um domínio ('<span style="{estilo}">...</span>').
  
  O {estilo} é uma série de especificações de estilo HTML,
  como "font-size: 12px; color: 'ff2200'", e pode ser vazio.
  
  O {conteudo} pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>').."""
  return gera_html_elem_IMP.span(estilo, conteudo)
 
def div(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como uma divisão '<div style="{estilo}">...</div>').
  
  O {estilo} é uma série de especificações de estilo HTML,
  como "font-size: 12px; color: 'ff2200'", e pode ser vazio.
  
  O {conteudo} pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>').."""
  return gera_html_elem_IMP.div(estilo, conteudo)
 
def paragrafo(estilo, conteudo):
  """Retorna um string que é um fragmento HTML consistindo do {conteudo}
  dado, formatado como um parágrafo ('<p style="{estilo}">...</p>').
  
  O {estilo} é uma série de especificações de estilo HTML,
  como "font-size: 12px; color: 'ff2200'", e pode ser vazio.
  
  O {conteudo} pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>').."""
  return gera_html_elem_IMP.paragrafo(estilo, conteudo)

def bloco_texto(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo):
  """Retorna un string que é um fragmento HTML consistindo do {texto}
  dado, que pode conter tags de HTML (como '<b>', '<i>') e quebras de
  linha ('<br/>'). O fragmento todo é um domínio  {span(estilo,texto)}
  com o {estilo} apropriado.
  
  O parâmetro {disp} é o valor do atributo 'display' do estilo, por exemplo 
  'block' ou 'inline-block'.. 

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

def bloco_de_produto(prod, qt, detalhe):
  """Devolve um fragmento HTMP que decreve o produto {prod}, um objeto da classe {ObjProduto}.
  
  Se {detalhe} for {False}, mostra apenas o identificador do produto,
  a descrição curta e a descrição média, com uma imagem pequena,
  e um botão "Ver" que permite ver mais detalhes. Se {detalhe} for {True}, mostra também
  a descrição detalhada, a quantidade em estoque, etc., com uma imagem maior,
  e um botão "Comprar".
  
  Em qualquer caso, se {qt} não for {None}, mostra a quantidade {qt}
  e o preço para essa quantidade.  Se {qt} for {None},
  mostra apenas o preço unitário, sem a quantidade."""
  return gera_html_elem_IMP.bloco_de_produto(prod, qt, detalhe)

def bloco_de_compra(compra):
  """Devolve um fragmento HTML que decreve a compra {compra}, um objeto da classe {ObjCompra}."""
  return gera_html_elem_IMP.bloco_de_compra(compra)
