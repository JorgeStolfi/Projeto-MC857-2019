#! /usr/bin/python3
# Last edited on 2019-08-13 00:32:21 by stolfilocal

# Este módulo define a classe {Pedido}. Um objeto desta 
# classe representa e descreve um pedido de compra de um 
# ou mais produtos em diversas quantidades, feito por um 
# cliente da loja, que pode estar em várias etapas de execução.

# Interfaces importadas por esta interface:
import carrinho; from carrinho import Carrinho
import usuario; from usuario import Usuario

# Implementaçao deste módulo:
import pedido_IMP
from pedido_IMP import Pedido_IMP

# Funções exportadas por este módulo:

class Pedido(Pedido_IMP):
    def lista_itens(self):
        """Esta função lista dos produtos do pedido. Retorna uma lista de itens: itens é uma tupla do tipo (produto, quantidade, preco)"""
        return Pedido_IMP.lista_itens(self)

def cria(c):
    """Esta função cria um pedido. Para isso, recebe como parametro um carrinho:"""
    """E cria um pedido com os produtos do carrinho"""
    return pedido_IMP.cria(c)

def obtem_usuario(self):
    """ Esta função retorna um objeto do tipo { Usuario }. """
    return self

def obtem_status(self):
    """ Essa função retorna o status do pedido. Os status podem ser: """
    """ 1) 'incompleto': Quando o usuário jpa realizou a compra, porém o pagamento não foi efetuado. """
    """ 2) 'pagando': Quando a pagamento do produto já foi efetuado e aprovado, mas ainda não foi enviado. """
    """ 3) 'depachado': Quando o pedido estiver indo para o usuário com a transportadora. """
    return self
