# Este módulo implementa a classe de objetos {Produto} que
# representa um produto do catálogo da loja virtual.

import inspect, sys
import base, base_produtos, identificador 

class Produto_IMP():

  def __init__(self,atrs):
    self.atrs = atrs
    self.id = None

  def obtem_identificador(self):
    return self.id

  def obtem_atributos(self):
    atrs = self.atrs.copy()
    return atrs

  def calcula_preco(self,qt):
    return 3.1415926
  
  def muda_atributos(self,bas,alts):
    for key in alts:
      if key in self.atrs: 
        self.atrs[key] = alts[key]
    ind = identificador.para_indice("P",self.id)
    base_produtos.atualiza(bas,ind,self)

def cria(bas,atrs):
  sys.stderr.write("Criando objeto...\n")
  prod = Produto_IMP(atrs.copy())
  sys.stderr.write("acrescentando na base...\n")
  ind = base_produtos.acrescenta(bas,prod) 
  sys.stderr.write("acrescentado, ind = %d\n" % ind)
  prod.id = identificador.de_indice("P",ind)
  return prod
