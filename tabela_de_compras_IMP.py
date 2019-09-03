import base_sql

# done
def cria_tabela(bas,):
  cmd = "CREATE TABLE compras (" + \
    "indice int(8) NOT NULL AUTO_INCREMENT,"
    " id_compra int(8) NOT NULL," + \
    " cliente varchar(60) NOT NULL," + \
    " status varchar(10) NOT NULL," + \
    " PRIMARY KEY indice" + \
    ")"
    bas.executa_comando(cmd);

#done
def busca_por_usuario(bas,usr):
   cmd = "SELECT * FROM compras WHERE user_id = " + usr.id
   usr = bas.executa_comando(cmd)
   return usr

#done
def busca_por_identificador(bas,compra_id):
   cmd = "SELECT * FROM compras WHERE compra_id = " + compra_id
   cpr = bas.executa_comando(cmd)
   return cpr

#done
def busca_por_data(bas,data):
   cmd = "SELECT * FROM compras WHERE data = " + data
   lista_compras = bas.executa_comando(cmd)
   return lista_compras

# done
def acrescenta(bas,cpr):
   cmd = "INSERT INTO compras (id_compra, cliente, status) VALUES ("
   + f"{cpr.id_compra},{cpr.cliente}, {cpr.status})"
   sucesso = bas.executa_comando(cmd)
   ind = bas.indice_inserido()
   return ind

#done
def recupera(bas,cpr):
   cmd = "SELECT * FROM compras WHERE id = " + cpr.id
   cpr = bas.executa_comando(cmd)
   return cpr

#done
def atualiza(bas,cpr):
   cmd = f'UPDATE compras SET "cliente" = {cpr.cliente}, SET "status" = {cpr.status} WHERE "id_compra" = {cpr.id_compra}'
   sucesso = bas.executa_comando(cmd)
   return sucesso

#done
def deleta(bas,cpr):
   cmd = "DELETE FROM compras WHERE compra_id = " + cpr
   sucesso = bas.executa_comando(cmd)
   return sucesso
