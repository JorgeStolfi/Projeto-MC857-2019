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
    def lista_produtos(self):
        """Esta função lista dos produtos do pedido"""
        return Pedido_IMP.lista_produtos(self)

    def deleta(pedido_id):
        """Esta função deleta um pedido. Recebe como parametro o pedido_id e retorna true, para sucesso e false para falha na operacao"""
        return Pedido_IMP.deleta(pedido_id)

def cria(carrinho):
    """Esta função cria um pedido. Para isso, recebe como parametro um carrinho:"""
    """E cria um pedido com os produtos do carrinho"""
    return pedido_IMP.cria(carrinho)