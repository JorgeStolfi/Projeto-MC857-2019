#!/usr/bin/python3

# Funções para acesso primário à base de dados da loja. 

# Implementacao desta interface:
import base_IMP; from base_IMP import Base_IMP

class Base(Base_IMP):

  """Um objeto desta classe representa uma base de dados no disco
  (possivelmente com espelho ou cache na memória) contendo quatro
  tabelas separadas: 'usuarios', 'produtos', 'compras' e 'sessoes'. O acesso
  à base é feito por meio de comandos SQL."""

  def executa_comando(self,cmd):
    """Recebe um string {cmd} que é um comando de consulta, acréscimo, ou
    alteração da base, codificado na linguagem SQL.
    Devolve o resultado da execução do comando.  
    
    No caso de um comando "SELECT", o resultado é uma lista de 
    tuplas, uma para cada linha da tabela que
    satisfez as condições da busca. Cada tupla contém os campos
    especificados no comando. Por exmplo, se {cmd} é 
    
      "SELECT email,cpf FROM usuarios WHERE cep=13083-851"
      
    o resultado poderia ser
    
      [ ("zeca@gmail.com", "123.456.789-00"), 
        ("juca@hotmail.com", "987.654,321-99"),
        ... ]
        
    Se nenhuma entrada satisfizer os critérios, o resultado 
    é uma lista vazia.
    
    No caso de um comando "INSERT" ou "UPDATE", o resultado é ???.
    
    Alterações e adições são automaticamente finalizadas ("commit")
    e não podem ser canceladas ("rollback")."""
    return Base_IMP.executa_cmd(self,cmd)

  def indice_inserido(self):
    """Esta função pode ser chamada logo após inserir algum novo
    item (produto, compra, usuário, ou sessão) na base de de dados.  Ela 
    devolve o índice inteiro (chave) que foi atribuído ao item, e 
    o identifica na base de dados."""
    return Base_IMP.indice_inserido(self)
    
# CONSTRUTOR

def conecta(dir,uid,senha):
  """Conecta com a base de dados no disco e devolve um objeto da classe
  {Base} representando a mesma. Se houver algum erro, devolve {None}.
  
  A string {dir} é o nome completo do diretório onde está a base de dados.
  A string {uid} é o nome do usuário Linux que tem acesso à base, e {senha}
  é a sua senha de login.  Se {uid} for {None}, tenta concectar usando o usuário corrente;
  nesse caso a {senha} é ignorada."""
  return base_IMP.conecta(dir,uid,senha)

