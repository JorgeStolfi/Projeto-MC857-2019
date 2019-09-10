# Este módulo define a classe de objetos {ObjSessao}, que
# representa uma sessão de 'login' de um cliente da loja virtual.
# 
# Nas funções abaixo, {usr} é um objeto da classe {ObjUsuario}
# que representa o cliente.

# Interfaces importadas por esta interface:
import usuario; from usuario import ObjUsuario
import base_sql; from base_sql import Base_SQL

# Implementaçao deste módulo:
import sessao_IMP; from sessao_IMP import ObjSessao_IMP

class ObjSessao(ObjSessao_IMP):
  """Um objeto desta classe representa uma sessao de acesso ao
  servidor.  Os atributos deste objeto, por enquanto, são:
  
    'usr' {ObjUsuario} - o usuário que fez login na sessão.
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

  def obtem_atributos(self):
    """Retorna um dicionário Python que é uma cópia dos atributos da sessão,
    exceto identificador."""
    return ObjSessao_IMP.obtem_atributos(self)
    
  def muda_atributos(self, alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos da sessão (exceto o identificador), e troca os 
    valores desses atributos pelos valores correspondentes em {alts}.  
    Também altera esses campos na base de dados.
    Em caso de sucesso, retorna o próprio objeto."""
    return ObjSessao_IMP.muda_atributos(self, alts)

  def obtem_usuario(self):
    """Retorna o objeto da classe {ObjUsuario} correspondente ao usuario que
    fez login na sessao.  Equivale a {self.obtem_atributos()['usr']}. """
    return ObjSessao_IMP.obtem_usuario(self)

  def aberta(self):
    """Retorna o estado da sessão: {True} se a sessao ainda esta aberta, 
    {False} se o usuário deu logout.  Equivale a {self.obtem_atributos()['aberta']}."""
    return ObjSessao_IMP.aberta(self)
    
  def logout(self):
    """Registra o logout do usuário na sessão, mudando o atributo 'aberta'
    permanentemente para {False}. Também altera esse campo na base de dados.
    Em caso de sucesso, retorna o próprio objeto."""
    return ObjSessao_IMP.logout(self)
    
# Construtor da classe:

def cria(usr):
  """Cria um novo objeto da classe {ObjSessao}, associada ao usuário {usr},
  inicialmente aberta.  Também acrescenta a sessão à base de dados.  Em caso de
  sucesso, retorna o objeto."""
  return sessao_IMP.cria(usr)

# Descrição dos campos:

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjSessao}, menos o identificador.  O resultado é adequado 
  para o parâmetro {cols} das funções do módulo {tabela_generica}."""
  return sessao_IMP.campos()
# ======================================================================
# Funções para acesso à base de dados das sessões.

# Implementação desta interface:
import tabela_de_sessoes_IMP
from tabela_de_sessoes_IMP import Obj_Tabela_De_Sessoes_IMP

class Obj_Tabela_De_Sessoes(Obj_Tabela_De_Sessoes_IMP):
  # Um objeto (instância) desta classe representa a tabela de sessoes
  # da base de dados. Deve haver uma única instância 
  # no servidor.
  # 
  # Cada linha desta tabela representa uma sessão de login, ativa ou 
  # encerrada.  Os campos são basicamente os mesmos de um objeto de 
  # classe {ObjSessao}. 
  # 
  # Cada linha tem um índice inteiro (chave primária) que é atribuído
  # quando a linha é criada. As funções desta interface manuseiam o
  # índice na forma de um identificador de sessao "S-{NNNNNNNN}".
  # 
  # Especificamente, cada linha tem os seguintes campos de informação
  # (colunas da tabela):
  #   
  #   'id_sessao' {str} O identificador do sessao, "S-{NNNNNNNN}".
  #   'id_usuario' {str} - O identificador do usuário, "U-{NNNNNNNN}".
  #   'aberta' {bool} - {True} se a sessão está ativa, {False} se o cliente deu logout.
  #   
  # Outros campos (como peso, volume, estoque, imagens, palvras-chave, etc.)
  # serão acrescentados oportunamente.
  # 
  # O identificador 'id_sessao' de cada linha é atribuído sequencialmente
  # quando a linha é criada.  Todos os campos, exceto 'id_sessao', e 'id_usuario',
  # podem ser alterados.
  # 
  # Nas funções abaixo, uma linha da tabela é representada na memória
  # por um dicionário Python {atrs} cujas chaves e valores
  # são os campos da linha.

  # Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
  # que representa a base de dados da loja.

  def acrescenta(self,atrs):
    """Acrescenta uma nova linha na tabela de sessões
    da base {bas}, cujo conteúdo é o dicionário {atrs},
    e devolve o identificador "S-{NNNNNNNN}" da mesma.
    O dicionário não deve conter o campo 'id_sessao'."""
    return Obj_Tabela_De_Sessoes_IMP.acrescenta(self,ses)

  def busca_por_identificador(self,id_sessao):
    """Devolve um dicionário {atrs} com o conteúdo da linha 
    de identificador {id_sessao} da tabela de sessões da base {bas}.
    O dicionário não inclui o campo 'id_sessao'."""
    return Obj_Tabela_De_Sessoes_IMP.busca_por_identificador(self,id_sessao)

  def atualiza(self,id_sessao,atrs):
    """Modifica alguns campos de uma linha da tabela de sessões da base {bas}.
    A linha é especificada pelo seu identificador {id_sessao}. 
    Não devolve nenhum resultado.

    O parâmetro {atrs} deve ser um dicionário cujas chaves são um
    subconjunto dos nomes dos campos da linha (excluindo 'id_sessao'). 
    Os valores desses campos na tabela são substituídos pelos valores em {atrs}."""
    Obj_Tabela_De_Sessoes_IMP.atualiza(self,id_sessao,atrs)

def cria_tabela(bas):
  """Cria a tabela de sessões na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  return tabela_de_sessoes_IMP.cria_tabela(bas)
