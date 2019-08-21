import base.py

#Retorna todos os pedidos do usuario
def busca_por_usuario(usr):
   query = "SELECT * FROM pedidos WHERE user_id = " + usr.id
   usuario = base.executa_query(query)
   return usuario

#Busca o pedido pelo id
def busca_por_id(pedido_id):
   query = "SELECT * FROM pedidos WHERE pedido_id = " + pedido_id
   pedido = base.executa_query(query)
   return pedido

#Busca todos os pedidos daquela data
def busca_por_data(data):
   query = "SELECT * FROM pedidos WHERE data = " + data
   lista_pedidos = base.executa_query(query)
   return lista_pedidos

#Envia o pedido para o banco de dados
def cria(ped):
   query = "INSERT INTO pedidos"
   sucesso = base.executa_query(query)
   return sucesso

#Recupera o pedido do banco de dados pelo id do pedido
def recupera(ped):
   query = "SELECT * FROM pedidos WHERE id = " + ped.id
   pedido = base.executa_query(query)
   return pedido

#Atualiza o pedido no banco de dados
def atualiza(ped):
   query = "UPDATE pedidos"
   sucesso = base.executa_query(query)
   return sucesso

#Deleta o pedido no banco de dados
def deleta(ped):
   query = "DELETE FROM pedidos WHERE pedido_id = " + ped
   sucesso = base.executa_query(query)
   return sucesso