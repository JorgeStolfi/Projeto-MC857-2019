#! /usr/bin/python3
#Por LKT

#Funcoes para busca de pedidos na base de dados
#Estas funcoes devolvem objetos(classe  Pedido) ou {none} caso 
#a busca invalida. Os argumentos são atributos da classe Pedido 
#(usuario,pedido_id,data,etc..) armazenada nas tabelas do banco.

#A busca pode filtrar por diferentes argumentos.
import base_pedidos_IMP.py


def busca_por_usuario(usr):
    '''
    Devolve uma lista de objetos da classe {Pedido} associados ao usuário {usr} na base de dados. Se não houver nenhum pedido associado a esse usuário, devolve {None}.
    '''
    return  base_pedidos_IMP.busca_pedidos_usuario(usr)


def busca_por_id(pedido_id):
    '''
    Devolve uma um objetos da classe {Pedido} cujo id na base é  {id}. Se não houver nenhum pedido com esse {id}, devolve {None}.
    '''
    return base_pedidos_IMP.busca_pedidos_id(pedido_id)


def busca_por_data(data):
    '''
    Devolve uma lista de objetos da classe {Pedido} realizados na data {data}. Se não houver nenhum pedido nessa {data}, devolve {None}.
    '''
    return base_pedidos_IMP.busca_pedidos_data(data)


#funcoes basicas de banco de dados
def cria(ped):
    '''
    Cria uma entrada no banco de dados com as informações pertencentes ao objeto {ped}.
    '''
    return base_pedidos_IMP.create(ped)

def recupera(ped):
    '''
    Recupera uma entrada no banco de dados com as informações pertencentes ao objeto {ped}.
    '''
    return base_pedidos_IMP.retrieve(ped)

def atualiza(ped):
    '''
    Atualiza os dados da entrada referente ao objeto {ped} no banco.
    '''
    return base_pedidos_IMP.update(ped)

def deleta(ped):
    '''
    Deleta do banco a entrada referente ao objeto {ped}.
    '''
    return base_pedidos_IMP.delete(ped)
