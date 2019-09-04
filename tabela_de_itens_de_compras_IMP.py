import base_sql
import identificador

def cria_tabela(bas):
  cmd = "CREATE TABLE itens_compras (" + \
    "id_item int(8) NOT NULL AUTO_INCREMENT," +\
    "id_compra int(8) NOT NULL AUTO_INCREMENT," +\
    "id_produto int(8) NOT NULL AUTO_INCREMENT," +\
    "qt float NOT NULL AUTO_INCREMENT," +\
    "preco float NOT NULL AUTO_INCREMENT," +\
    "PRIMARY KEY id_item"
  bas.executa_comando(cmd)
  
def acrescenta(bas,atrs):
   campos="id_compra,id_produto,qt,preco"
   valores = \
   atrs["id_compra"] + ", " + \
   atrs["id_produto"] + ", " + \
   atrs["qt"] + ", " + \
   atrs["preco"]
       
   cmd = "INSERT INTO itens_compras(" + campos + ") VALUES (" + valores + ");"
   sucesso = bas.executa_comando(cmd)
   ind = bas.indice_inserido() 
   return   identificador.de_indice("I",ind)


def busca_por_compra(bas,id_compra):
   cmd = "SELECT id_item FROM itens_compras WHERE id_compra = " + str(id_compra) + ";"
   cpr = bas.executa_comando(cmd)
   return cpr

def busca_por_produto(bas,id_produto):
   cmd = "SELECT id_item FROM compras WHERE id_produto = " + id_produto + ";"
   cpr = bas.executa_comando(cmd)
   return cpr



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
