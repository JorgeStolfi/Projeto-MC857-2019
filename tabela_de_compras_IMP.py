import base_sql

def cria_tabela(bas,chaves):
  cmd = "CREATE TABLE compras (" + \
    "indice int(8) NOT NULL AUTO_INCREMENT,"
    
  for ch in chaves:
    cmd = cmd + ch + " varchar(,"

def busca_por_usuario(bas,usr,abr):
   cmd = "SELECT * FROM compras WHERE user_id = " + usr.id
   usr = bas.executa_comando(cmd)
   return usr

def busca_por_id(bas,compra_id):
   cmd = "SELECT * FROM compras WHERE compra_id = " + compra_id
   cpr = bas.executa_comando(cmd)
   return cpr

def busca_por_data(bas,data):
   cmd = "SELECT * FROM compras WHERE data = " + data
   lista_compras = bas.executa_comando(cmd)
   return lista_compras

def acrescenta(bas,cpr):
   cmd = "INSERT INTO compras"
   sucesso = bas.executa_comando(cmd)
   ind = bas.indice_inserido()
   return ind

def recupera(bas,cpr):
   cmd = "SELECT * FROM compras WHERE id = " + cpr.id
   cpr = bas.executa_comando(cmd)
   return cpr

def atualiza(bas,cpr):
   cmd = "UPDATE compras"
   sucesso = bas.executa_comando(cmd)
   return sucesso

def deleta(bas,cpr):
   cmd = "DELETE FROM compras WHERE compra_id = " + cpr
   sucesso = bas.executa_comando(cmd)
   return sucesso
