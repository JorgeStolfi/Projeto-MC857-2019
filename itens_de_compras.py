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
#  'qt':      um float, a quantidade do produto nessa compra.
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

def busca_por_compra(id_compra):
  """Extrai da tabela de itens de compras todas as entradas referente
  ao pedido com identificador {id_compra}. 
  
  Devolve uma lista de triplas ({prd}, {qt}, {prc}), onde {prd} é um
  objeto da classe {ObjProduto}, {qt} é um {float}, a quantidade do
  produto nessa compra. e {prc} é um {float}, o preço dessa quantidade
  desse produto.
  
  Nessa lista, não haverá duas entradas com o mesmo produto,
  nem entradas com {qt} nulo ou negativo."""
  return itens_de_compras_IMP.busca_por_compra(id_compra)

def atualiza_lista(id_compra, lit, prod, qt_velho, qt_novo):
  """Atualiza a lista de itens {lit} de um pedido de compra com
  identificador {id_compra}, trocando a quantidade do produto {prod}
  nessa lista do valor atual, que deve ser {qt_velho}, para {qt_novo}, 
  e recalculando o preço. Também atualiza a tabela de itens na base SQL.
  Não retorna nenhum resultado.
  
  O parâmetro {lit} deve ser uma lista de triplas ({prd}, {qt}, {prc}), 
  como a devolvida por {busca_por_compra}. O parâmetro {prod} deve ser um 
  objeto da classe {ObjProduto}. Os parâmetros {qt_velho} e {qt_novo}
  devem ser {float}s não-negativos.
  
  Em particular, o produto {prod} deve ocorrer na lista se e somente se
  {qt_velho > 0}. Se {qt_velho > 0} e {qt_novo == 0}, a tripla
  desse produto é eliminada da lista com {del lit[...]}. Se {qt_velho == 0} e
  {qt_novo > 0}, a nova tripla é acrescentada com {lit.append(...)}. Se {qt_velho
  > 0} e {qt_novo > 0}, a tripla é substituída com atribuição.
  O preço é recalculado mesmo se {qt_novo == qt_velho}."""
  itens_de_compras_IMP.atualiza_lista(id_compra, lit, prod, qt_velho, qt_novo)

def posicao_do_item(prod, lit):
  """Obtem o índice do item com produto {prod} na lista de itens de compra {lit}. Se não 
  existir, devolve {None}."""
  return itens_de_compras_IMP.posicao_do_item(prod, lit)

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  itens_de_compras_IMP.diagnosticos(val)
