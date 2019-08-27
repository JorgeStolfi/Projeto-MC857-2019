# Este módulo define a classe de objetos {Usuario} que
# representa um usuário (cliente) da loja virtual.

# Implementação deste módulo e da classe {Usuario}:
import usuario_IMP
from usuario_IMP import Usuario_IMP

class Usuario(Usuario_IMP):
  """Um objeto desta classe representa um usuário da loja e
  armazena seus atributos.  Por enquanto, são:
    {nome} {str} - nome completo do usuário.
    {senha} {str} - senha do usuário.
    {email} {str} - endereço de email
    {CPF} {str} - número CPF
    {endereco} {str} - endereço completo, em 3 linhas (menos CEP).
    {CEP} {str} - código de endereçamento postal completo ("{NNNNN}-{LLL}").
    {telefone} {str} - telefone completo com DDI e DDD ("+{XX}({YY}){MMMM}-{NNNN}").
  """
  
  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'U-{NNNNNNNN}', onde 
    {NNNNNNNN} é um número de 8 algarismos 
    que identifica unicamente o usuário. Este identificador é 
    atribuído na criação do usuário e não pode ser alterado."""
    return Usuario_IMP.obtem_identificador(self)
    
  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do usuário,
    exceto identificador."""
    return Usuario_IMP.obtem_atributos(self)
    
  def muda_atributos(self,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do usuário, e troca os valores desses atributos 
    pelos valores correspondentes em {alts}.  Também atualiza esses
    valores na base de dados. """
    return usuario_IMP.muda_atributos(self,alts)
    
# Construtor da classe:

def cria(atrs):
  """Cria um novo objeto da classe {Usuario}, com atributos especificados 
  pelo dicionário Python {atrs}, insere o mesmo na base de dados de usuários, e
  define seu identificador a partir do índice do mesmo nessa base."""
  return usuario_IMP.cria(atrs)
  
