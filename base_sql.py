# Funções para acesso primário à base de dados da loja. 

# O acesso é feito através de comandos SQL, no dialeto da SQLite.
#
# Nas funções e métodos abaixo, o parâmetro {atrs} é um dicionário
# Python cujas chaves devem ser os nomes das colunas da tabela (strings), 
# e os valores de {atrs} serão os valores dessas colunas.  Os tipos dos 
# valores de {atrs} devem ser compatíveis com os tipos das colunas da tabela.

# Implementacao desta interface:
import base_sql_IMP; from base_sql_IMP import Base_SQL_IMP 

class Base_SQL(Base_SQL_IMP):

  """Um objeto desta classe representa uma base de dados no disco
  (possivelmente com espelho ou cache na memória) contendo quatro
  tabelas separadas: 'usuarios', 'produtos', 'compras' e 'sessoes'. O acesso
  à base é feito por meio de comandos SQL."""

  def executa_comando_CREATE_TABLE(self, nome_tb, colunas):
    """Executa um comando "CREATE TABLE IF NOT EMPTY {nome_tb} ( {colunas} )".
    O argumento {colunas} deve ser um string que descreve as colunas da
    tabela na linguagem SQL. Por exemplo,
    
      "indice INTEGER PRIMARY KEY," \
      "CPF CHAR(14) NOT NULL," \
      "valor FIXED(8,2) NOT NULL"
    
    Note que na base SQLite a coluna designada como "PRIMARY KEY" precisa ser
    de tipo "INTEGER" para ter auto-incremento na inserção de novas linhas.
      
    O resultado é {True} em caso de sucesso, {False} em caso de erro."""
    return Base_SQL_IMPL.executa_comando_CREATE_TABLE(self, nome_tb, colunas)
    
  def executa_comando_INSERT(self, nome_tb, atrs):
    """Acrescenta uma nova linha na tabela {nome_tb}, cujo conteúdo 
    é especificado pelo dicionário Python {atrs}. 
    
    Devolve um inteiro que é o índice da nova linha na tabela, ou {None}
    caso a inserção tenha falhado."""
    return Base_SQL_IMPL.executa_comando_CREATE_TABLE(self, nome_tb, atrs)
    
  def executa_comando_UPDATE(self, nome_tb, cond, atrs):
    """Modifica os valores de linhas da tabela {nome_tb}
    segundo especificado pelo dicionário {atrs}.  Altera apenas as colunas cujos 
    nomes são as chaves de {atrs} (que não devem incluir 
    a chave primária da tabela).
    
    As linhas a serem alteradas são as que satisfazem a condição {cond},
    um predicado na linguagem SQL.  Por exemplo, "email = 'foo@bar.com'" ou
    "salario > 2000". O método retorna {True} em caso de sucesso,
    {False} se houver erro."""
    return Base_SQL_IMPL.executa_comando_UPDATE(self, nome_tb, cond, atrs)

  def executa_comando_SELECT(self, nome_tb, cond, colunas):
    """Enumera as linhas da tabela {nome_tb} que satisfazem a condição
    SQL {cond}.
    
    O argumento {colunas} é uma tupla ou lista de strings, que devem
    ser nomes de colunas da tabela.
    
    O resultado é uma lista de tuplas, uma para cada linha da tabela
    que satisfez a condição de busca. Cada tupla contém os valores
    das colunas especificados no comando. Por exmplo, se {cond}
    é "cep = '13083-851'" e {colunas} é ('email','cpf'),
    o resultado poderia ser
    
      [ ("zeca@gmail.com", "123.456.789-00"), 
        ("juca@hotmail.com", "987.654,321-99"),
        ... ]
        
    Se nenhuma entrada satisfizer a condição {cond}, o resultado 
    é uma lista vazia.  Retorna {None} em caso de erro."""
    return Base_SQL_IMP.executa_comando_SELECT(self, nome_tb, nome_col, val_col, colunas)

  def executa_comando_DELETE(self, nome_tb, nome_col, val_col):
    """Eliminas as linhas da tabela {nome_tb} nas quais a coluna {nome_col}
    tem valor {val_col}. O método retorna {True} em caso de sucesso, {False} se houver erro."""
    return Base_SQL_IMP.executa_comando_DELETE(self, nome_tb, nome_col, val_col)

  def executa_comando_CLEAR_TABLE(self, nome_tb):
    """Apaga todas as linhas da tabela {nome_tb} (usando um comando 'DELETE' do SQL
    sem 'WHERE'). O método retorna {True} em caso de sucesso, {False} se houver erro."""
    return Base_SQL_IMP.executa_comando_CLEAR_TABLE(self, nome_tb)
    
# CONSTRUTOR

def conecta(dir, uid, senha):
  """Conecta com a base de dados no disco e devolve um objeto da classe
  {Base_SQL} representando a mesma. Se houver algum erro, devolve {None}.
  
  A string {dir} é o nome completo do diretório onde fica a base de dados. 
  
  A string {uid} é o nome do usuário Linux que tem acesso à base, e {senha}
  é a sua senha de login.  Se {uid} for {None}, tenta concectar usando o usuário corrente;
  nesse caso a {senha} é ignorada."""
  return base_sql_IMP.conecta(dir, uid, senha)

