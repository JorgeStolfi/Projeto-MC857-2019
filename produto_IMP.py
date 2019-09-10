# Imlementação do módulo {produto} e da classe {ObjProduto}.

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
    tabela_de_produtos.atualiza(bas,self.id,alts)

def cria(bas,atrs):
  sys.stderr.write("Criando objeto...\n")
  prod = ObjProduto_IMP(atrs.copy())
  sys.stderr.write("acrescentando na base...\n")
  pid = tabela_de_produtos.acrescenta(bas,prod.obtem_atributos()) 
  sys.stderr.write("acrescentado, ind = %s\n" % pid)
  prod.id = pid
  return prod

# ======================================================================

#Implementação do módulo {tabela_de_produtos}.

import sys
import identificador
import base_sql

class Obj_Tabela_De_Produtos_IMP:
  
  def __init__(self,bas):
    # Base de dados:
    self.bas = bas
    # Nomes e tipos das colunas (menos 'indice'):
    self.colunas = (
      ('descr_curta', 'varchar(60) NOT NULL'),
      ('descr_media', 'varchar(128) NOT NULL'),
      ('descr_longa', 'text NOT NULL'),
      ('unidade', 'char(60) NOT NULL'),
      ('preco', 'float(20) NOT NULL'),
    )
    campos = "indice integer NOT NULL PRIMARY KEY," + \
    for c in self.colunas:
      campos = campos + ", " + c[0] + " " + c[1]
    self.bas.executa_comando_CREATE_TABLE("produtos", campos)

  def busca_por_palavra(bas, pal):
    curta = "descr_curta LIKE '%" + pal + "%'"
    media = "descr_media LIKE '%" + pal + "%'"
    longa = "descr_longa LIKE '%" + pal + "%'"
    cond = \
      curta + " OR " + \
      media + " OR " + \
      longa
    indices_econtrados = self.bas.executa_comando_SELECT("produtos", cond, ['indice'])
    print("Produtos encontrados: " + str(indices_econtrados))
    ids = [].copy()
    for ind in indices_econtrados:
      ids.push(identificador.de_indice("P", ind[0]))
    return ids

  def busca_por_identificador(bas, ind_produto):
    ind = identificador.para_indice("P", ind_produto)
    cond = "indice = " + str(ind)
    col_nomes = ( c[0] for c in self.colunas )
    res = self.bas.executa_comando_SELECT("produtos", cond, col_nomes)
    print("Produtos encontrados: " + str(res))
    if res == None or len(res) == 0:
      return None
    else:
      assert len(res) == 1
      col_vals = res[0]
      assert len(col_vals) == len(col_nomes)
      atrs = dict(zip(col_nomes, col_vals))
      return atrs

  def acrescenta(bas, atrs):
    ind = self.bas.executa_comando_INSERT("produtos", atrs)
    id_produto = identificador.de_indice("P", ind)
    return id_produto

  def atualiza(bas, id_produto, atrs):
    ind = identificador.para_indice("P", id_produto)
    cond = "indice = " + str(ind)
    self.bas.executa_comando_UPDATE("produtos", cond, atrs)

def cria_tabela(bas):
  return Obj_Tabela_De_Produtos_IMP(bas)

