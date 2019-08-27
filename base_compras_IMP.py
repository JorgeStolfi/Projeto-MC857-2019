import base.py

def busca_por_usuario(usr,abr):
   query = "SELECT * FROM compras WHERE user_id = " + usr.id
   usuario = base.executa_query(query)
   return usuario

def busca_por_id(compra_id):
   query = "SELECT * FROM compras WHERE compra_id = " + compra_id
   compra = base.executa_query(query)
   return compra

def busca_por_data(data):
   query = "SELECT * FROM compras WHERE data = " + data
   lista_compras = base.executa_query(query)
   return lista_compras

def acrescenta(ped):
   query = "INSERT INTO compras"
   sucesso = base.executa_query(query)
   return sucesso

def recupera(ped):
   query = "SELECT * FROM compras WHERE id = " + ped.id
   compra = base.executa_query(query)
   return compra

def atualiza(ped):
   query = "UPDATE compras"
   sucesso = base.executa_query(query)
   return sucesso

def deleta(ped):
   query = "DELETE FROM compras WHERE compra_id = " + ped
   sucesso = base.executa_query(query)
   return sucesso
