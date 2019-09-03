# Este módulo define a classe {ObjCompra}.
# 
# Nas funções abaixo, {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja; {prod} é um objeto
# da classe {ObjProduto}; {usr} é um objeto da classe {ObjUsuario};
# e {qt} é um float não-negativo.

# Interfaces importadas por esta interface:
import usuario; from usuario import ObjUsuario
import produto; from produto import ObjProduto
import base_sql; from base_sql import Base_SQL

# Implementaçao deste módulo:
import compra_IMP; from compra_IMP import ObjCompra_IMP

class ObjCompra(ObjCompra_IMP):
  """Um objeto desta classe representa e descreve um pedido de compra
  de um ou mais produtos em diversas quantidades, feito por um
  cliente da loja, que pode estar em várias etapas de execução.
  Em particular, o pedido pode ainda estar sendo construído e alterado
  pelo usuário -- ou seja, pode ser um "carrinho de compras".
  
  Por enquanto, os atributos de um objeto desta classe são:
  
    'usr' {ObjUsuario} - o cliente que fez ou está montando a compra.
    'itens' {lista} - lista de itens no pedido.
    'status' {str} 
    
  Cada elemento da lista 'itens' é uma lista de tres elementos {[prod,
  qt,preco]} onde {prod} é um objeto da classe {ObjProduto}, {qt} é
  um float que indica a quantidade comprada, e {preco} é um float que
  indica o preço do item.  Os produtos na lista são sempre todos distintos.
  
  O atributo 'status' por enquanto, pode ser:
  
   'aberto': O cliente ainda está montando o pedido.
   'pagando':  O cliente fechou o pedido, e a loja está aguardando o pagamento.
   'pago': A loja já recebeu o pagamento e mandou para despacho.
   'despachado': A loja já colocou o pedido no correio ou transportadora.
   'entregue': O pedido foi entregue ao cliente.
   
  Mais campos e/ou estados poderão ser acrescentados no futuro."""

  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'C-{NNNNNNNN}', onde
    {NNNNNNNN} é um número de 8 algarismos
    que identifica unicamente o pedido de compra. Este identificador é
    atribuído na criação do objeto e não pode ser alterado."""
    return ObjCompra_IMP.obtem_identificador(self)

  def obtem_usuario(self):
    """ Esta função retorna o cliente do pedido de compra
    (um objeto da classe {ObjUsuario})."""
    return ObjCompra_IMP.obtem_usuario(self)

  def obtem_status(self):
    """Retorna o atributo 'status' do pedido de compra."""
    return ObjCompra_IMP.obtem_status(self)

  def obtem_itens(self):
    """Retorna uma cópia da lista de itens no pedido de compra."""
    return ObjCompra_IMP.lista_itens(self)

  def calcula_total(self):
    """ Retorna um float que é o preco total do pedido de compra"""
    return ObjCompra_IMP.calcula_total(self)

  def acrescenta_item(self,bas,prod,qt):
    """Acrescenta um novo item no pedido de compra, consistindo da quantidade 
    {qt} do produto {prod}.
    
    Se o produto já está na lista de itens, soma {qt} à quantidade que
    consta nessa lista. Também recalcula o preço do item e registra a
    alteração na tabela de compras da base {bas}. Se {qt} for zero, o
    efeito é nulo."""
    return ObjCompra_IMP.acrescenta_item(self,bas,prod,qt)

  def troca_qtd(self,bas,prod,qt):
    """Modifica a lista de itens da compra, trocando a quantidade
    atual do produto {prod} por {qt}.
    Se {qt} for zero, elimina o produto {prod} da lista. 
    Se o produto {prod} não está na lista, acrescenta-o com 
    quantidade {qt}. Também recalcula o preço do item e registra
    a alteração na tabela de compras da base {bas}."""
    return ObjCompra_IMP.troca_qtd(self, prod, qt)

  def elimina_prod(self,bas,prod):
    """Modifica a lista de itens da compra, eliminando a entrada
    com produto {prod}.  Se o produto não aparece na lista,
    não faz nada e devolve {False}; caso contrário devolve {True}."""
    return ObjCompra_IMP.elimina_prod(prod)

def cria(bas,usr):
  """Esta função cria um objeto da classe {ObjCompra} que representa um novo pedido de
  compra para o cliente {usr}, inicialmente vazio (sem nenhum produto). 
  O pedido é acrescentado à tabela de compras da base {bas}, e recebe 
  um identificador único."""
  return compra_IMP.cria(bas,usr)
