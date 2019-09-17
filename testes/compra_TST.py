#! /usr/bin/python3

import usuario
import tabela_generica
import base_sql
import identificador
import utils_testes
import sys

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {compra}, limpando tabela:\n")
compra.inicializa(True)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_compra(rotulo,usr,indice,ident,atrs):
  """Testes básicos de consistência do objeto {usr} da classe {ObjCompra}, dados {indice},
  {ident} e {atrs} esperados."""
  global ok_global
  ok = utils_teste.verifica_objeto(rotulo, compra, compra.ObjCompra, usr, indice, ident, atrs)

  if usr != None and type(usr) is compra.ObjCompra:
    
    # ----------------------------------------------------------------------
    sys.stderr.write("testando {busca_por_email()}:\n")
    em1 = atrs['email']
    usr1 = compra.busca_por_email(em1)
    if usr1 != usr:
      sys.stderr.write("  **erro: retornou " + str(usr1) + ", deveria ter retornado " + str(usr) + "\n")
      ok = False

    # ----------------------------------------------------------------------
    sys.stderr.write("testando {busca_por_CPF()}:\n")
    CPF1 = atrs['CPF']
    usr1 = compra.busca_por_CPF(CPF1)
    if usr1 != usr:
      sys.stderr.write("  **erro: retornou " + str(usr1) + ", deveria ter retornado " + str(usr) + "\n")
      ok = False

  ok_global = ok_global and ok
  return
 
def testa_cria_compra(rotulo,indice,ident,atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  usr = compra.cria(atrs)
  verifica_compra(rotulo,usr,indice,ident,atrs)
  return usr
 
# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.cria}:\n")
usr1_atrs = {
  "nome": "José Primeiro", 
  "senha": "123456789", 
  "email": "primeiro@gmail.com", 
  "CPF": "123.456.789-00", 
  "endereco": "Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP", 
  "CEP": "13083-418", 
  "telefone": "+55(19)9 9876-5432"
}
uindice1 = 1
uident1 = "U-00000001"
usr1 = testa_cria_usuario("usr1",uindice1,uident1,usr1_atrs)

usr2_atrs = {
  "nome": "João Segundo", 
  "senha": "987654321", 
  "email": "segundo@ic.unicamp.br", 
  "CPF": "987.654.321-99", 
  "endereco": "Avenida dos Semáforos, 1003\nJardim Pelado\nCampinas, SP", 
  "CEP": "13083-007", 
  "telefone": "+55(19)9 9898-1212"
}
uindice2 = 2
uident2 = "U-00000002"
usr2 = testa_cria_usuario("usr2",uindice2,uident2,usr2_atrs)

usr3_atrs = {
  "nome": "Juca Terceiro", 
  "senha": "4321002134", 
  "email": "muda@gmail.com", 
  "CPF": "111.111.111-11", \
  "endereco": "Rua Zero, 0000\nVila Zero\nCampinas, SP", \
  "CEP": "13083-999", 
  "telefone": "+55(19)9 9999-9999"
}
uindice3 = 3
uident3 = "U-00000003"
usr3 = testa_cria_usuario("usr3",uindice3,uident3,usr3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.muda_atributos}:\n")

usr1_mods = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
usuario.muda_atributos(usr1,usr1_mods)
usr1_d_atrs = usr1_atrs
for k, v in usr1_mods.items():
  usr1_d_atrs[k] = v
verifica_usuario("usr1_d",usr1,uindice1,uident1,usr1_d_atrs)

if type(usr2) is ObjUsuario:
  usuario.muda_atributos(usr2,usr2_atrs) # Não deveria mudar os atributos
  verifica_usuario("usr2",usr2,uindice2,uident2,usr2_atrs)

if type(usr2) is ObjUsuario:
  usr2_m_atrs = usr3_atrs.copy()
  usr2_m_atrs['CPF'] = usr2_atrs['CPF'] # Não pode alterar CPF.
  usuario.muda_atributos(usr2,usr2_m_atrs) # Deveria assumir os valores do usr3
  verifica_usuario("usr2_m",usr2,uindice2,uident2,usr2_m_atrs)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  # Terminou OK:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  # Termina com erro:
  sys.stderr.write("**erro - teste falhou\n")
  assert False

import sys
import compra; from compra import ObjCompra
import usuario; from usuario import ObjUsuario
import produto; from produto import ObjProduto
import base_sql
import tabela_de_compras
import identificador

#inicializa banco de dados
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB/MC857",None,None)
assert res == None

#inicializa modulo compra
compra.inicializa()

colunas_compras = compra.campos()

#limpa a tabela de compras
sys.stderr.write("Limpando tabela de compras...\n")
res = tabela_generica.limpa_tabela("compras", colunas_compras)
sys.stderr.write("Resultado = " + str(res) + "\n")



# ----------------------------------------------------------------------
def mostra_compra(rotulo,cpr,id,atrs):
  """Imprime compra {cpr} e compara seus atributos com {id,atrs}."""
  sys.stderr.write(rotulo + " = \n")
  if cpr == None:
    sys.stderr.write("None\n")
  elif type(cpr) is compra.ObjCompra:
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

cpr1_mods = {
    "qt" : "2348",
    "preco" : "3.50"
    }
compra.muda_atributos(cpr1,cpr1_mods)
cpr1_a = compra.busca_por_compra(cid1)
cpr1_a_atrs = cpr1_atrs
for k,v in cpr1_mods:
  cpr1_a_atrs[k] = v
mostra_compra("cpr1_a",cpr1_a,cid1,cpr1_a_atrs)

if type(cpr2) is ObjCompra:
    compra.muda_atributos(usr2,usr2_atrs)
    mostra_compra("cpr2",cpr2,cid2,cpr2_atrs)
    
if type(cpr3) is ObjCompra:
    compra.muda_atributos(usr3,usr2_atrs)
    mostra_compra("cpr3",cpr3,cid2,cpr2_atrs)
