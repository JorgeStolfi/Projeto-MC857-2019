#!/usr/bin/python3

#Carlos Eduardo da Silva Santos (humanolaranja)
#195396
#Última Atualização: 20/08

import base

def busca_por_nome(nome):
	query = 'select * from produtos where nome like "%' + nome '"'
	response = base.executa_query(query)
	return response

def busca_por_id(id):
	query = 'select * from produtos where id = ' + id
	response = base.executa_query(query)
	return response