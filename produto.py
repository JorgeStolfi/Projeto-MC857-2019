# Este módulo define a classe de objetos {Produto} que
# representa um produto do catálogo da loja virtual.

# Implementação deste módulo e da classe {Produto}:
import produto_IMP
from produto_IMP import Produto_IMP

class Produto(Produto_IMP):

  # Um objeto desta classe representa um produto da loja
  # e armazena atributos: "descr_curta", "descr_media", "descr_longa", 
  # "imagens", etc. 
  
  def obtem_id(self):
    """Devolve uma cadeia consistindo das letras 'P-' e 8 algarismos decimais,
    que identifica unicamente o produto. Este identificador é 
    atribuído na criação do produto e não pode ser alterado."""
    return Produto_IMP.obtem_id(self)
    
  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do produto,
    exceto o identificador."""
    return Produto_IMP.obtem_atributos(self)
    
  def muda_atributos(self,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do produto, e troca os valores desses atributos 
    pels valores correspondentes em {alts}."""
    return Produto_IMP.muda_atributos(self,alts)
    
# Construtor da classe:

def cria(atrs):
  """Cria um novo produto com um novo identificador único e os
  atributos especificados pelo dicionário Python {atrs}."""
  return produto_IMP.cria(atrs)

