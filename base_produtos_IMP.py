#!/usr/bin/python3

#Carlos Eduardo da Silva Santos (humanolaranja)
#195396
#Última Atualização: 20/08

import base

# Pendente transformar o response em um objeto Produto e chamar a Página que gera a lista de produtos
# Aguardando implementação da base de dados para saber como ẽ o retorno da função
def busca_por_nome(nome):
	query = 'select * from produtos where nome like "%' + nome '%"'
	response = base.executa_query(query)
	return response

def busca_por_id(id):
	query = 'select * from produtos where id = ' + id
	response = base.executa_query(query)
	return response