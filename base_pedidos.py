#! /usr/bin/python3
#Por LKT

#Funcoes para busca de pedidos na base de dados
#Estas funcoes devolvem objetos(classe  Pedido) ou {none} caso 
#a busca invalida.Os argumentos são atributos da classe Pedido 
#(usuario,pedido_id,data,etc..) armazenada nas tabelas do banco.

#A busca pode filtrar por diferentes argumentos.
import base_pedidos_IMP.py

#retorna a lista de pedidos do usuario(s?) fornecido(s?)
def busca_pedidos_usuario(usuario)
    return  base_pedidos_IMP.busca_pedidos_usuario(dados)

#retorna o pedido com o id fornecido
def busca_pedidos_id(pedido_id)
    return base_pedidos_IMP.busca_pedidos_id(dados)

#retorna os pedidos de certa data
def busca_pedidos_data(data)
    return base_pedidos_IMP.busca_pedidos_data(dados)

#retorna a busca entre os valores fornecidos e cruza no banco
def busca_pedidos_valor(valor_min,valor_max)
    return base_pedidos_IMP.busca_pedidos_valor(dados)

#funcoes basicas de banco de dados
def create(pedido)
    return base_pedidos_IMP.create(dados)

def retrieve(pedido)
    return base_pedidos_IMP.retrieve(dados)

def update(pedido)
    return base_pedidos_IMP.update(dados)

def delete(pedido)
    return base_pedidos_IMP.delete(dados)
