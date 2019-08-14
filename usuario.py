# Este módulo define a classe de objetos {Usuario} que
# representa um usuário (cliente) da loja virtual.

# Implementação deste módulo e da classe {Usuario}:
import usuario_IMP
from usuario_IMP import Usuario_IMP

class Usuario(Usuario_IMP):

  # Um objeto desta classe representa um usuário da loja e
  # armazena seus atributos: "nome", "senha", "email", "CPF", "endereco",
  # "telefone", etc. 
  
  def obtem_id(self):
    """Devolve uma cadeia consistindo das letras 'U-' e 8 algarismos decimais,
    que identifica unicamente o usuário. Este identificador é 
    atribuído na criação do usuário e não pode ser alterado."""
    return Usuario_IMP.obtem_id(self)
    
  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do usuário,
    exceto identificador."""
    return Usuario_IMP.obtem_atributos(self)
    
  def muda_atributos(self,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do usuário, e troca os valores desses atributos 
    pels valores correspondentes em {alts}."""
    return Usuario_IMP.muda_atributos(self,alts)
    
# Construtor da classe:

def cria(atrs):
  """Cria um novo usuário com um novo identificador único e os
  atributos especificados pelo dicionário Python {atrs}."""
  return usuario_IMP.cria(atrs)
  
