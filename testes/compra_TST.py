#! /usr/bin/python3

import sys
import compra; from compra import ObjCompra
import usuario; from usuario import ObjUsuario
import produto; from produto import ObjProduto
import base_sql
import tabela_de_compras
import identificador

#inicializa banco de dados
sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

#inicializa modulo compra
compra.inicializa()

colunas = compra.campos()

#limpa a tabela de compras
sys.stderr.write("Limpando tabela de compras...\n")
res = tabela_generica.limpa_tabela("compras", colunas)
sys.stderr.write("Resultado = " + str(res) + "\n")



# ----------------------------------------------------------------------
def mostra_compra(rotulo,cpr,id,atrs):
  """Imprime compra {cpr} e compara seus atributos com {id,atrs}."""
  sys.stderr.write(rotulo + " = \n")
  if cpr == None:
    sys.stderr.write("None\n")
  elif type(cpr) is ObjCompra_IMP:
    sys.stderr.write("  id = " + str(compra.obtem_identificador(cpr)) + "\n")
    sys.stderr.write("  atrs = " + str(cpr.obtem_atributos(cpr)) + "\n")
    if atrs != None:
      id_confere = (compra.obtem_identificador(cpr) == id)
      atrs_conferem = (cpr.obtem_atributos(cpr) == atrs)
      sys.stderr.write("  CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")
 
def testa_cria_compra(rotulo,id,atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  cpr = compra.cria(atrs)
  mostra_compra(rotulo,usr,id,atrs)
  return cpr
 


# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.acrescenta}:\n")

cpr1_atrs = {
  "id_produto" : "00000001",
  "qt" : "32",
  "preco" : "3.50"
}
cid1 = "C-00000001"
cpr1 = testa_cria_compra("cpr1",cid1,cpr1_atrs)

cpr2_atrs = {
  "id_produto" : "00000002",
  "qt" : "323",
  "preco" : "7"
}
cid2 = "C-00000002"
cpr2 = testa_cria_compra("cpr2",cid2,cpr2_atrs)

cpr3_atrs = {
  "id_produto" : "00000003",
  "qt" : "342",
  "preco" : "10.50"
}
cid3 = "C-00000003"
cpr3 = testa_cria_compra("cpr3",cid3,cpr3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {compra.busca_por_compra}:\n")
cpr1_c = compra.busca_por_compra(cid1)
mostra_compra("cpr1_c",cpr1_c,cid1,cpr1_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.busca_por_produto}:\n")
cpr_id = cpr2_atrs["id_produto"]
cpr2_p = compra.busca_por_produro(cpr_id)
mostra_compra("cpr2_p",cpr2_p,cid2,cpr2_atrs)

cpr1_alts = {
    "qt" : "2348",
    "preco" : "3.50"
    }

compra.muda_atributos(cpr1,cpr1_alts)
cpr1_a = compra.busca_por_compra(cid1)
cpr1_a_atrs
for k,v in cpr1_atrs
  cpr1_a_atrs[k]=v
mostra_compra("cpr1_a",cpr1_a,cid1,cpr1_a_atrs)

if type(cpr2) is ObjCompra_IMP:
    compra.muda_atributos(usr2,usr2_atrs)
    mostra_compra("cpr2",cpr2,cid2,cpr2_atrs)
    
if type(cpr3) is ObjCompra_IMP:
    compra.muda_atributos(usr3,usr2_atrs)
    mostra_compra("cpr3",cpr3,cid2,cpr2_atrs)
