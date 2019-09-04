# Este módulo define a classe de objetos {ObjUsuario} que
# representa um usuário (cliente) da loja virtual.
# 
# Nas funções abaixo, {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.

# Interfaces importadas por esta interface:
import base_sql; from base_sql import Base_SQL

# Implementação deste módulo e da classe {ObjUsuario}:
import usuario_IMP; from usuario_IMP import ObjUsuario_IMP

class ObjUsuario(ObjUsuario_IMP):
  """Um objeto desta classe representa um usuário da loja e
  armazena seus atributos.  Por enquanto, são:
  
    'nome' {str} - nome completo do usuário.
    'senha' {str} - senha do usuário.
    'email' {str} - endereço de email
    'CPF' {str} - número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    'endereco' {str} - endereço completo, em 3 linhas (menos CEP).
    'CEP' {str} - código de endereçamento postal completo ("{NNNNN}-{LLL}").
    'telefone' {str} - telefone completo com DDI e DDD ("+{XX}({YY}){MMMM}-{NNNN}").
    
  Outros atributos (nascimento, preferências, etc.) poderão ser acrescentados no futuro.
  """
  
  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'U-{NNNNNNNN}', onde 
    {NNNNNNNN} é um número de 8 algarismos 
    que identifica unicamente o usuário. Este identificador é 
    atribuído na criação do usuário e não pode ser alterado."""
    return ObjUsuario_IMP.obtem_identificador(self)
    
  def obtem_atributos(self):
    """Retorna um dicionário Python que é uma cópia dos atributos do usuário,
    exceto identificador."""
    return ObjUsuario_IMP.obtem_atributos(self)
    
  def muda_atributos(self,bas,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do usuário, e troca os valores desses atributos 
    pelos valores correspondentes em {alts}.  Também atualiza esses
    valores na base de dados {bas}. 
    
    O número CPF não pode ser alterado.  A alteração de email 
    só é permitida se o novo email for distinto dos emails
    de todos os outros usuários na base."""
    return ObjUsuario_IMP.muda_atributos(self,bas,alts)
    
# Construtor da classe:

def cria(bas,atrs):
  """Cria um novo objeto da classe {ObjUsuario}, com atributos especificados 
  pelo dicionário Python {atrs}.  Insere o mesmo na tabela de usuários
  da base de dados {bas}, e define seu identificador a partir do 
  índice do mesmo nessa tabela.
  
  Os atributos 'email' e 'CPF' devem estar definidos em {atrs}, e devem ser 
  distintos dos mesmos atributos de todos os usuários já inseridos na 
  tabela de usuários."""
  return usuario_IMP.cria(bas,atrs)
