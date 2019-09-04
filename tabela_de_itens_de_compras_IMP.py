import base_sql
import identificador

def cria_tabela(bas):
  campos =  \
    "indice integer NOT NULL PRIMARY KEY," + \
    "id_compra char(10) NOT NULL," + \
    "id_produto char(10) NOT NULL," + \
    "qt float NOT NULL," + \
    "preco float NOT NULL"
  bas.executa_comando_CRIA_TABELA("itens_de_compras", campos)
  
def acrescenta(bas, atrs):
   ind = bas.executa_comando_INSERT("itens_de_compras", atrs)
   return   identificador.de_indice("I", ind)

def busca_por_compra(bas, id_compra):
   res = bas.executa_comando_SELECT("itens_de_compras", "id_compra = '" + id_compra "'", ('id_produto','qt','preco'))
   return cpr

def busca_por_produto(bas, id_produto):
   res = bas.executa_comando_SELECT("itens_de_compras", "id_produto = '" + id_produto "'", ('id_compra','qt','preco'))
   return cpr
   
def atualiza(bas, id_item, atrs):
   res = bas.executa_comando_UPDATE("itens_de_compras", "indice = " + str(ind), atrs);
   return
