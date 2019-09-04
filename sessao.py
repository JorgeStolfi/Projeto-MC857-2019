# Este módulo define a classe de objetos {ObjSessao} que
# representa uma sessão de 'login' de um cliente da loja virtual.
# 
# Nas funções abaixo, {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja; e {usr}
# é um objeto da classe {ObjUsuario} que representa o cliente.

# Interfaces importadas por esta interface:
import usuario; from usuario import ObjUsuario
import base_sql; from base_sql import Base_SQL

# Implementaçao deste módulo:
import sessao_IMP; from sessao_IMP import ObjSessao_IMP

class ObjSessao(ObjSessao_IMP):
  """Um objeto desta classe representa uma sessao de acesso ao
  servidor.  Os atributos deste objeto, por enquanto, são:
  
    'usr' {ObjUsuario} - o usuário que fez login na sessão, ou {None}.
    'aberta' {bool} - estado da sessao.
    
  Outros atributos (data, cookie, IP, etc.) poderão ser acrescentados no futuro.
  
  Cada sessao pertence a um unico usuario, mas cada
  usuário pode ter várias sessoes abertas ao mesmo tempo. A sessao é criada
  e "aberta" quando o usuario faz login, e e "fechada" no logout. """

  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'S-{NNNNNNNN}', onde 
    {NNNNNNNN} e um numero de 8 algarismos 
    que identifica unicamente a sessao. Este identificador e 
    atribuido na criacao da sessao e nao pode ser alterado."""
    return ObjSessao_IMP.obtem_identificador(self)

  def aberta(self):
    """Retorna o estado da sessão: {True} se a sessao ainda esta aberta, 
    {False} se o usuário deu logout."""
    return ObjSessao_IMP.aberta(self)

  def obtem_usuario(self):
    """Retorna um objeto do tipo Usuario, para o usuario logado na sessao"""
    return ObjSessao_IMP.obtem_usuario(self)

  def logout(self,bas):
    """Registra o logout do usuário na sessão, mudando o atributo {aberta}
    permanentemente para {False}.  Também registra a mudança na tabela de sessões da
    base de dados {bas}."""
    ObjSessao_IMP.logout(self,bas)
    
# Construtor da classe:

def cria(bas,usr):
  """Cria um novo objeto da classe {ObjSessao}, associada ao usuário {usr},
  inicialmente aberta.  Também acrescenta a sessão à tabela de sessões
  da base de dados {bas}."""
  return sessao_IMP.cria(bas,usr)
