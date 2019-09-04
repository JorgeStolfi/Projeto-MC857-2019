import base_sql

def cria_tabela(bas):
  campos = \
    "indice integer NOT NULL PRIMARY KEY,"
    "id_usuario char(10) NOT NULL," + \
    "status varchar(10) NOT NULL" + \
  bas.executa_comando_CREATE_TABLE("compras",campos);

def busca_por_identificador(bas,compra_id):
  res = bas.executa_comando_SELECT("compras", 'indice', ind, ('id_usuario','status'))
  return res

def acrescenta(bas,cpr):
  cmd = "INSERT INTO compras (id_compra, cliente, status) VALUES ("
  + f"{cpr.id_compra},{cpr.cliente}, {cpr.status})"
  sucesso = bas.executa_comando_INSERT("compras",...)
  ind = bas.indice_inserido()
  return ind

def atualiza(bas,cpr):
  cmd = f'UPDATE compras SET "cliente" = {cpr.cliente}, SET "status" = {cpr.status} WHERE "id_compra" = {cpr.id_compra}'
  sucesso = bas.executa_comando(cmd)
  return sucesso
