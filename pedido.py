#! /usr/bin/python3
# Last edited on 2019-08-13 00:32:21 by stolfilocal

# Interface do módulo {pedido}.
# As funções deste módulo retornam os pedidos

# Interfaces importadas por esta interface:

# Implementaçao deste módulo:
import pedido_IMP
from pedido_IMP import Pedido_IMP

# Funções exportadas por este módulo:

class Pedido(Pedido_IMP):
    def lista_itens(self):
        """Esta função lista dos produtos do pedido. Retorna uma lista de itens: itens é uma tupla do tipo (produto, quantidade, preco)"""
        return Pedido_IMP.lista_itens(self)

def cria(carrinho):
    """Esta função cria um pedido. Para isso, recebe como parametro um carrinho:"""
    """E cria um pedido com os produtos do carrinho"""
    return pedido_IMP.cria(carrinho)