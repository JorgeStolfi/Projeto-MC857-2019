# Este módulo implementa a classe de objetos {ObjProduto} que
# representa um produto do catálogo da loja virtual.

import inspect, sys
import base_sql, tabela_de_produtos, identificador 

class ObjProduto_IMP():

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
    tabela_de_produtos.atualiza(bas,self.id_produto,alts)

def cria(bas,atrs):
  sys.stderr.write("Criando objeto...\n")
  prod = ObjProduto_IMP(atrs.copy())
  sys.stderr.write("acrescentando na base...\n")
  pid = tabela_de_produtos.acrescenta(bas,prod) 
  sys.stderr.write("acrescentado, ind = %d\n" % ind)
  prod.id_produto = pid
  return prod
