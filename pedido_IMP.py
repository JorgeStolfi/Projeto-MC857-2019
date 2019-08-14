#! /usr/bin/python3
# Last edited on 2019-08-13 00:32:21 by stolfilocal

# Interface do módulo {pedido}.
# As funções deste módulo retornam os pedidos

# Interfaces importadas por esta interface:
import carrinho

class Pedido_IMP:
    def __init__(self, pedido_id, itens):
        self.pedido_id = pedido_id
        self.itens = itens

    def lista_itens(self):
        return self.itens

def cria(pedido_id, car):
    itens = car.pega_itens()
    prod = Pedido_IMP(pedido_id, itens)

    return prod
