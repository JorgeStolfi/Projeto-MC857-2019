# Este módulo define funções para manipular itens de pedidos de compra
# e sua tabela na base de dados.

# ATENÇÃO: Estas funções devem ser usadas apenas pela implementação do 
# módulo {compra}.  Outros módulos devem usar as funções apropriadas
# desse módulo.

# Como a base SQL não permite listas em campos, os itens dos pedidos de compra
# são armazenados em disco em uma tabela separada da base SQL,
# "itens_de_compras". Cada item de cada pedido de compra no sistema é
# representado por uma linha nesta tabela. Cada linha desta tablea tem
# um índice inteiro (chave primária) distinto, que é atribuído quando a
# linha é criada. Cada linha também tem um identificador de item de
# compra, uma string da forma "I-{NNNNNNNN}" onde {NNNNNNNN} é o índice
# formatado em 8 algarismos.
#
# Alem do índice do item, cada tabela na base de dados tem quatro colunas:
#
#  'compra':  índice inteiro do objeto {ObjCompra} que representa o pedido.
#  'produto': índice inteiro do objeto {ObjProduto} que representa o produto.
#  'qtd':      um float, a quantidade do produto nessa compra.
#  'preco':   um float, o preço dessa quantidade desse produto.

# Interfaces importadas por esta interface:
import produto

# Implementaçao deste módulo:
import itens_de_compras_IMP

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela "itens_de_compras" na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor, 
  depois de chamar {base_sql.conecta}. Não retorna nenhum valor.  
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  itens_de_compras_IMP.inicializa(limpa)

def busca_por_identificador(id_item):
  """Localiza uma compra com identificador {id_item} (uma string da forma
  'I-{NNNNNNNN}'), e devolve a mesma na forma de uma tupla ({id_compra},
  {id_produto},{qtd}, {preco}).
  Se tal item não existe, devolve {None}."""
  return itens_de_compra.busca_por_identificador(id_item)

def busca_por_compra(id_compra):
  """Extrai da tabela de itens de compras todas as entradas referente
  ao pedido com identificador {id_compra}. 
  
  Devolve uma lista de triplas ({prd}, {qtd}, {prc}), onde {prd} é um
  objeto da classe {ObjProduto}, {qtd} é um {float}, a quantidade do
  produto nessa compra. e {prc} é um {float}, o preço dessa quantidade
  desse produto.
  
  Nessa lista, não haverá duas entradas com o mesmo produto,
  nem entradas com {qtd} nulo ou negativo."""
  return itens_de_compras_IMP.busca_por_compra(id_compra)

def busca_por_produto(id_produto):
  """Extrai da tabela de itens de compras todas as entradas referente
  ao produto com identificador {id_produto}.

  Devolve uma lista de triplas ({cpr}, {qtd}, {prc}), onde {cpr} é um
  objeto da classe {ObjCompra}, {qtd} é um {float}, a quantidade do
  produto nessa compra. e {prc} é um {float}, o preço dessa quantidade
  do produto.
  
  Nessa lista, não haverá duas entradas com a mesma compra,
  nem entradas com {qtd} nulo ou negativo."""
  return itens_de_compras_IMP.busca_por_produto(id_produto)

def atualiza_lista(id_compra, lit, prod, qtd_velho, qtd_novo):
  """Atualiza a lista de itens {lit} de um pedido de compra com
  identificador {id_compra}, trocando a quantidade do produto {prod}
  nessa lista do valor atual, que deve ser {qtd_velho}, para {qtd_novo}, 
  e recalculando o preço. Também atualiza a tabela de itens na base SQL.
  Não retorna nenhum resultado.
  
  O parâmetro {lit} deve ser uma lista de triplas ({prd}, {qtd}, {prc}), 
  como a devolvida por {busca_por_compra}. O parâmetro {prod} deve ser um 
  objeto da classe {ObjProduto}. Os parâmetros {qtd_velho} e {qtd_novo}
  devem ser {float}s não-negativos.
  
  Em particular, o produto {prod} deve ocorrer na lista se e somente se
  {qtd_velho > 0}. Se {qtd_velho > 0} e {qtd_novo == 0}, a tripla
  desse produto é eliminada da lista com {del lit[...]}. Se {qtd_velho == 0} e
  {qtd_novo > 0}, a nova tripla é acrescentada com {lit.append(...)}. Se {qtd_velho
  > 0} e {qtd_novo > 0}, a tripla é substituída com atribuição.
  O preço é recalculado mesmo se {qtd_novo == qtd_velho}."""
  itens_de_compras_IMP.atualiza_lista(id_compra, lit, prod, qtd_velho, qtd_novo)

def posicao_do_item(lit, prod):
  """Obtem o índice do item com produto {prod} na lista de itens de compra {lit}. Se não 
  existir, devolve {None}."""
  return itens_de_compras_IMP.posicao_do_item(lit, prod)

def obtem_quantidade(lit, prod):
  """Retorna a quantidade atual do produto {prod} na lista de itens de
  compras {lit}.  Se o produto não está na lista de itens, devolve zero."""
  return itens_de_compras_IMP.obtem_quantidade(lit, prod)

def obtem_preco(lit, prod):
  """Retorna o preco total do produto {prod} na lista de itens de
  compras {lit}.  Se o produto não está na lista de itens, devolve zero."""
  return itens_de_compras_IMP.obtem_preco(lit, prod)

def calcula_total(lit):
  """ Retorna um float que é o preco total do pedido de compra, ou seja a
  soma dos campos {qtd} nos elementos da lista de itens."""
  return itens_de_compras_IMP.calcula_total(lit)

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  itens_de_compras_IMP.diagnosticos(val)
