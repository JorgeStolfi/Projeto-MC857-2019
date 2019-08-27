#!/usr/bin/python3

# Funções para acesso primário à base de dados da loja. 

# Implementacao desta interface:
import base_IMP; from base_IMP import Base_IMP

class Base(Base_IMP):

  """Um objeto desta classe representa uma base de dados no disco
  (possivelmente com espelho ou cache na memória) contendo quatro
  tabelas separadas: 'usuario', 'produto', 'compra' e 'sessao'. O acesso
  à base é feito por meio de comandos SQL."""

  def executa_comando(self,cmd):
    """Recebe um string {cmd} que é um comando de consulta, acréscimo, ou
    alteração da base, codificado na linguagem SQL.
    
    Devolve o resultado da execução do comando. Se o comando falhar (por exemplo, se
    não houver algo que satisfaça um comando de busca), devolve {None}.
    
    Alterações e adições são automaticamente finalizadas ("commit")
    e não podem ser canceladas ("rollback")."""
    return Base_IMP.executa_cmd(self,cmd)

  def indice_inserido(self):
    """Esta função pode ser chamada logo após inserir algum novo
    item (produto, compra, usuário, ou sessão) na base de de dados.  Ela 
    devolve o índice inteiro (chave) que foi atribuído ao item, e 
    o identifica na base de dados."""
    return Base_IMP.indice_inserido(self)

def conecta(dir,uid,senha):
  """Conecta com a base de dados no disco e devolve um objeto da classe
  {Base} representando a mesma. Se houver algum erro, devolve {None}.
  
  A string {dir} é o nome completo do diretório onde está a base de dados.
  A string {uid} é o nome do usuário Linux que tem acesso à base, e {senha}
  é a sua senha de login.  Se {uid} for {None}, tenta concectar usando o usuário corrente;
  nesse caso a {senha} é ignorada."""
  return base_IMP.conecta(dir,uid,senha)

# UTILITÁRIOS


def identificador_de_indice(let,ind):
  """Converte um índice inteiro {ind} em um string identificador da
  forma "{X}-{NNNNNNNN}" onde {X} é a string {let} dada e {NNNNNNNN} é o
  valor {ind} formatado em 8 algarismos decimais, com zeros à esquerda. Por exemplo,
  `identificador_de_indice("U",20557)` devolve "U-00020557".

  O índice {ind} deve estar em {0..99999999}. ({10^8-1})."""
  return base_IMP.identificador_de_indice(let,ind)

def indice_de_identificador(let,id):
  """Dado um identificador de objeto {ident}, da forma "{X}-{NNNNNNNN}",
  onde {X} deve ser a letra {let} dada, extrai o índice inteiro {NNNNNNNN} do 
  mesmo. Por exemplo, `indice_de_identificador("U","U-00020557")` devolve o inteiro 20555."""
  return base_IMP.indice_de_identificador(ident)
