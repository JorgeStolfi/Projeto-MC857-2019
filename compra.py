# Este módulo define a classe de objetos {ObjCompra}, que
# representa um pedido de compra (em particular, um carrinho de
# compras).
# 
# Nas funções abaixo, o parãmetro {prod} é um objeto
# da classe {ObjProduto}; {usr} é um objeto da classe {ObjUsuario};
# e {qt} é um float não-negativo, a quantidade do produto a comprar.

# Interfaces importadas por esta interface:
import usuario
import produto

# Implementaçao deste módulo:
import compra_IMP; from compra_IMP import ObjCompra_IMP

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de compras na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor.
  Não retorna nenhum valor.  Se o parâmetro booleano {limpa} for {True},
  apaga todas as linhas da tabela SQL, resetando o contador em 0."""
  compra_IMP.inicializa(limpa)

class ObjCompra(ObjCompra_IMP):
  """Um objeto desta classe representa e descreve um pedido de compra
  de um ou mais produtos em diversas quantidades, feito por um
  cliente da loja, que pode estar em várias etapas de execução.
  Em particular, o pedido pode ainda estar sendo construído e alterado
  pelo usuário -- ou seja, pode ser um "carrinho de compras".
  
  Por enquanto, os atributos de um objeto desta classe são:
  
    'cliente' um {ObjUsuario} que representa o cliente que fez ou está montando a compra.
    'itens'   uma lista Python de itens no pedido.
    'status'  uma string que indica o estado do pedido. 
    
  Cada elemento da lista 'itens' é uma lista de tres elementos {[prod,
  qt,preco]} onde {prod} é um objeto da classe {ObjProduto}, {qt} é
  um float que indica a quantidade comprada, e {preco} é um float que
  indica o preço total do item.  Os produtos na lista são sempre
  todos distintos.
  
  O atributo 'status' por enquanto, pode ser:
  
   'aberto': O cliente ainda está montando o pedido.
   'pagando':  O cliente fechou o pedido, e a loja está aguardando o pagamento.
   'pago': A loja já recebeu o pagamento e está mandando para despacho.
   'despachado': A loja já colocou o pedido no correio ou transportadora.
   'entregue': O pedido foi entregue ao cliente.
   
  Mais campos e/ou estados poderão ser acrescentados no futuro.
  
  Cada pedido de compra no sistema é representado por uma linha na tabela "compras" da base SQL em
  disco. Apenas algumas dessas linhas são representadas também na memória por objetos
  da classe {ObjCompra}. 
  
  Cada linha da tabela de compras tem um índice inteiro (chave primária) distinto, que é atribuído
  quando a linha é criada.  Neste sistema, esse índice é manipulado na forma de 
  um identificador de compra, uma string da forma "C-{NNNNNNNN}"
  onde {NNNNNNNN} é o índice formatado em 8 algarismos."""

def cria(atrs):
  """Cria um novo objeto da classe {ObjCompra}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de compras da base de dados.
  Atribui um identificador único à compra, derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return compra_IMP.cria(atrs)

def obtem_identificador(cpr):
  """Devolve o identificador 'C-{NNNNNNNN}' da compra {cpr}."""
  return compra_IMP.obtem_identificador(cpr)

def obtem_indice(cpr):
  """Devolve o índice inteiro da compra {cpr} na tabela de compras da base de dados."""
  return compra_IMP.obtem_indice(cpr)

def obtem_atributos(cpr):
  """Retorna um dicionário Python que é uma cópia dos atributos do pedido de
  compra {cpr}, exceto identificador."""
  return compra_IMP.obtem_atributos(cpr)

def obtem_cliente(cpr):
  """Retorna o cliente da compra {cpr}, um objeto da classe {Objusuario}.
  Equivale a {obtem_atributos(cpr)['cliente']}."""
  return compra_IMP.obtem_cliente(cpr)

def obtem_status(cpr):
  """Retorna o status da compra {cpr}. Equivale a {obtem_atributos(cpr)['status']}."""
  return compra_IMP.obtem_status(cpr)

def obtem_itens(cpr):
  """Retorna uma cópia da lista de itens da compra {cpr}. Equivale a 
  {obtem_atributos(cpr)['itens'].copy()}."""
  return compra_IMP.obtem_itens(cpr)

def muda_atributos(cpr, mods):
  """Modifica alguns atributos do objeto {cpr} da classe {ObjCompra},
  registrando as alterações na base de dados.  Não pode ser 
  usado para alterar os itens das compras.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos da compra (excluindo o identificador
  e 'itens'). Os valores atuais desses atributos são substituídos pelos valores 
  correspondentes em {mods}."""
  return compra_IMP.muda_atributos(cpr, mods)

def obtem_quantidade(cpr, prod):
  """Retorna a quantidade atual do produto {prod} no pedido de
  compras {cpr}.  Se o produto não está no pedido, devolve zero."""

def calcula_total(cpr):
  """ Retorna um float que é o preco total do pedido de compra, ou seja a
  soma dos campos {qt} nos elementos da lista de itens."""
  return compra_IMP.calcula_total(cpr)
    
def acrescenta_item(cpr, prod, qt):
  """Acrescenta um novo item no pedido de cpr, consistindo da quantidade 
  {qt} do produto {prod}, acrescentando-o também a tabela de itens de compra.
  Não retorna nenhum resultado.
  
  Se o produto já está na lista de itens, soma {qt} à quantidade que
  consta nessa lista. Também recalcula o preço do item. 
  Se {qt} for zero, o efeito é nulo."""
  compra_IMP.acrescenta_item(cpr,prod,qt)

def troca_quantidade(cpr, prod, qt):
  """Modifica a lista de itens da compra, trocando a quantidade
  atual do produto {prod} por {qt}. Altera também a linha correspondente
  da tabela de itens_de_compras.
  Não retorna nenhum resultado.
  
  Se {qt} for zero, elimina o produto {prod} da lista. 
  Se o produto {prod} não está na lista, acrescenta-o com 
  quantidade {qt}. Também recalcula o preço do item"""
  compra_IMP.troca_quantidade(cpr, prod, qt)

def elimina_prod(cpr, prod):
  """Modifica a lista de itens da compra, eliminando a entrada
  com produto {prod}. Também elimina a linha correspondente da tabela de itens_de_compras.
  O produto deve estar na lista. Não retorna nenhum resultado."""
  compra_IMP.elimina_prod(cpr,prod)

def busca_por_identificador(id_compra):
  """Localiza uma compra com identificador {id_compra} (uma string da forma
  'C-{NNNNNNNN}'), e devolve a mesma na forma de um objeto da classe {ObjCompra}.
  Se tal compra não existe, devolve {None}."""
  return compra_IMP.busca_por_identificador(id_compra)

def busca_por_produto(id_produto):
  """Localiza algumas compras cujo produto é {id_produto} 
  e devolve uma lista de identificadores das compras (não uma lista de objetos);
  ou lista vazia se não existir tal compra."""
  return compra_IMP.busca_por_produto(id_produto)

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjCompra}, menos o identificador e a lista de itens.  
  O resultado é adequado para o parâmetro {cols} das funções do módulo
  {tabela_generica}."""
  return compra_IMP.campos()
