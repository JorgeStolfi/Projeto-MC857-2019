#! /usr/bin/python3

# Este módulo define a classe {Compra}.

# Interfaces importadas por esta interface:
import usuario; from usuario import Usuario

# Implementaçao deste módulo:
import compra_IMP
from compra_IMP import Compra_IMP

# Funções exportadas por este módulo:

class Compra(Compra_IMP):
  """Um objeto desta classe representa e descreve um pedido de compra
  de um ou mais produtos em diversas quantidades, feito por um
  cliente da loja, que pode estar em várias etapas de execução.

  Em particular, o pedido pode ainda estar sendo construído e alterado
  pelo usuário -- ou seja, pode ser um "carrinho de compras"."""

  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'C-{NNNNNNNN}', onde
    {NNNNNNNN} é um número de 8 algarismos
    que identifica unicamente o pedido de compra. Este identificador é
    atribuído na criação do objeto e não pode ser alterado."""
    return Compra_IMP.obtem_identificador(self)

  def obtem_usuario(self):
    """ Esta função retorna o cliente do pedido de compra
    (um objeto da classe {Usuario})."""
    return Compra_IMP.obtem_usuario(self)

  def obtem_status(self):
    """Retorna o status do pedido de compra, um string que, por enquanto, pode ser:
       1) 'aberto': O cliente ainda está montando o pedido.
       2) 'pagando':  O cliente fechou o pedido, e a loja está aguardando o pagamento.
       3) 'pago': A loja já recebeu o pagamento e mandou para despacho.
       4) 'despachado': A loja já colocou o pedido no correio ou transportadora.
       5) 'entregue': O pedido foi entregue ao cliente.
    Outros estados podem ser acrescentados no futuro."""
    return Compra_IMP.obtem_status(self)

  def lista_itens(self):
    """Retorna uma cópia da lista de itens no pedido de compra.  Cada item é uma lista
    {[prod, qt, prc]}, onde {prod} é o produto (um objeto da classe {Produto}),
    {qt} é a quantidade (um float), e {prc} é o preço total do item (um float).
    
    Os produtos são todos distintos."""
    return Compra_IMP.lista_itens(self)

  def calcula_total(self):
    """ Retorna um float que é o preco total do pedido de compra"""
    return Compra_IMP.calcula_total(self)

  def acrescenta_item(self, prod, qt):
    """
        Acrescenta um novo item no pedido de compra

        Parametros
        -----------
        prod : Produto
            Objeto produto que será acrescentado no pedido de compra

        qt : int
            Quantidade de itens que serão comprados do produto
    """
    return Compra_IMP.acrescenta_item(self, prod, qt)

  def troca_qtd(self, prod, qt):
    """
        Modifica a quantidade de um item

        Parametros
        -----------
        prod : Produto
            Objeto produto que terá sua quantidade trocada

        qt : int
            Nova quantidade do produto
    """
    return Compra_IMP.troca_qtd(self, prod, qt)

  def elimina_prod(self, prod):
    """
        Remove um produto do pedido de compra

        Parametro
        -----------
        prod : Produto
            Objeto produto que será removido do pedido compra
    """
    return Compra_IMP.elimina_prod(prod)

def cria(bas,usr):
  """Esta função cria um objeto da classe {Compra} que representa um novo pedido de
  compra para o cliente {usr} (um objeto da classe {Usuario}), inicialmente vazio
  (sem nenhum produto). O pedido é acrescentado à tabela de compras da base {bas},
  e recebe um identificador único."""
  return compra_IMP.cria(bas,usr)
