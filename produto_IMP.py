# Este módulo implementa a classe de objetos {Produto} que
# representa um produto do catálogo da loja virtual.

import inspect, sys
import base, base_produtos

class Produto_IMP():

  def __init__(self,atrs):
    self.atrs = atrs;
    self.id = None;

  def obtem_identificador(self):
    """Devolve uma cadeia consistindo das letras 'P-' e 8 algarismos decimais,
    que identifica unicamente o produto. Este identificador é 
    atribuído na criação do produto e não pode ser alterado."""
    return self.id

  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do produto,
    exceto o identificador."""
    atrs = dict((name, getattr(self, name)) for name in dir(self) if (not name.startswith('_') and not inspect.ismethod(getattr(self, name) ) ) ) 
    return atrs

  def calcula_preco(self,qt):
    return 3.1415926
  
  def muda_atributos(self,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do produto, e troca os valores desses atributos 
    pels valores correspondentes em {alts}."""
    for key in alts:
        if key in dir(self):
            setattr(self, key, alts[key])

def cria(atrs):
  sys.stderr.write("Criando objeto...\n")
  prod = Produto_IMP(atrs.copy())
  sys.stderr.write("acrescentando na base...\n")
  # ind = base_produtos.acrescenta(prod)  # Descomentar quando funcionar
  ind = 12345
  sys.stderr.write("acrescentado, ind = %d\n" % ind)
  prod.id = base.identificador_de_indice("P",ind)
  return prod
