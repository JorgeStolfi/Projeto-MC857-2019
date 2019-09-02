# Versão fajuta do módulo {mysql}, para uso enquanto o módulo
# real não for instalado nas máquinas dos laboratórios.

import sys

Error = "mysql_bobo.Error"

class MySQLCursor:
  """Um objeto desta classe é um apontador para um ponto dentro da base de dados.
  Comandos são geralmente executados relativamente a tal objeto."""

  def __init__(self,conex):
    """O argumento {conex} deve ser um objeto da classe {MySQLConnection}."""
    sys.stderr.write("mysql_bobo: MySQLCursor.__init__(...)\n")
    return
    
  def execute(self,query):
    """Executa o comando SQL {query}, devolve o resultado do mesmo."""
    sys.stderr.write("mysql_bobo: MySQLCursor.execute(\"" + query + "\")\n")
    # Resultado fajuto:
    return "BOBO"
    
  def fetchall(self):
    """Se for chamado logo após {execute("SELECT ...")},
    devolve uma lista de tuplas com o resultado da busca."""
    sys.stderr.write("mysql_bobo: MySQLCursor.fetchall()\n")
    # Resultado fajuto:
    return [ ( "juca", 23.0 ), ("zeca", 34.0), ("caco", 56.0) ]
    
  def close(self):
    sys.stderr.write("mysql_bobo: MySQLCursor.close()\n")
    return
    

class MySQLConnection:
  """Um objeto desta classe representa uma conexão com a base de dados.""" 

  def __init__(self):
    sys.stderr.write("mysql_bobo: MySQLConnection.__init__()\n")
    return
    
  def cursor(self,buffered):
    """Retorna um cursor para percorrer a base de dados."""
    sys.stderr.write("mysql_bobo: MySQLConnection.cursor()\n")
    return MySQLCursor(self)
    
  def commit(self):
    """Finaliza um conjuto de operações UPDATE e/ou INSERT."""
    sys.stderr.write("mysql_bobo: MySQLConnection.commit()\n")
    return
   
  def insert_id(self):
    """Devolve o índice da entrada criada pelo último comando INSERT."""
    sys.stderr.write("mysql_bobo: MySQLConnection.insert_id()\n")
    # Resultado fajuto:
    return 12345


def connect(user,password,database):
  """Abre a base de dados e devolve um objeto da classe {MySQLConnection} que
  representa a mesma."""
  sys.stderr.write("mysql_bobo: MySQLConnection.connect()\n")
  return MySQLConnection()
