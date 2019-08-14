#! /usr/bin/python3
#Por LKT

#Funcoes para busca de pedidos na base de dados
#Estas funcoes devolvem objetos(classe  Pedido) ou {none} caso 
#a busca invalida.Os argumentos são atributos da classe Pedido 
#(usuario,pedido_id,data,etc..) armazenada nas tabelas do banco.

#A busca pode filtrar por diferentes argumentos.
import base_pedidos_IMP.py


def busca_pedidos_usuario(usuario):
    '''
    retorna a lista de pedidos do usuario(s?) fornecido(s?)
    '''
    return  base_pedidos_IMP.busca_pedidos_usuario(usuario)


def busca_pedidos_id(pedido_id):
    '''
    retorna o pedido com o id fornecido
    '''
    return base_pedidos_IMP.busca_pedidos_id(pedido_id)


def busca_pedidos_data(data):
    '''
    retorna os pedidos de certa data
    '''
    return base_pedidos_IMP.busca_pedidos_data(data)


def busca_pedidos_valor(valor_min,valor_max):
    '''
    retorna a busca entre os valores fornecidos e cruza no banco
    '''
    return base_pedidos_IMP.busca_pedidos_valor(valor_min,valor_max)

#funcoes basicas de banco de dados
def create(pedido):
    '''
    cria entrada no banco
    '''
    return base_pedidos_IMP.create(pedido)

def retrieve(pedido):
    return base_pedidos_IMP.retrieve(pedido)

def update(pedido):
    return base_pedidos_IMP.update(pedido)

def delete(pedido):
    return base_pedidos_IMP.delete(pedido)
