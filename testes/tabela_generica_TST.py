#! /usr/bin/python3

#Testes do módulo {tabela_generica}
import tabela_generica
import base_sql
import identificador

# Para diagnóstico:
import sys

def mostra_obj(rotulo, obj, id, atrs):
  """Imprime usuário {obj} e compara seus atributos com {id,atrs}."""
  sys.stderr.write(rotulo + " = \n")
  if obj == None:
    sys.stderr.write("  None\n")
  elif type(obj) is str:
    sys.stderr.write("  " + obj + "\n")
    assert False
  elif type(obj) is ObjBobo:
    sys.stderr.write("  id = " + str(obj.id) + "\n")
    sys.stderr.write("  atrs = " + str(obj.atrs) + "\n")
    if atrs != None:
      id_confere = (obj.id == id)
      atrs_conferem = (obj.atrs == atrs)
      sys.stderr.write("  CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")
  else:
    sys.stderr.write("  **erro: resultado não é objeto do tipo correto\n")
    sys.stderr.write("  " + str(obj) + "\n")
    assert False

def mostra_lista_ids(rotulo, res):
  """Mostra uma lista de ids que devem resultar de uma busca por campos."""
  sys.stderr.write(rotulo + " = ")
  if type(res) is list or type(res) is tuple:
    for ident in res:
      sys.stderr.write("  " + str(ident) + "\n")
      obj = tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, cria_obj, ident)
      mostra_obj("  ", obj, ident, None)
  else:
    sys.stderr.write("  **erro: resultado não é lista ou tupla\n")
    sys.stderr.write("  " + str(res) + "\n")
    assert False
   

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857", None, None)

# ----------------------------------------------------------------------

class ObjBobo:
  id = None
  atrs = None
  
  def __init__(self, id, atrs):
    self.id = id
    self.atrs = atrs
    
def cria_obj(id, atrs):
  sys.stderr.write("Criando ObjBobo(" + id + ", " + str(atrs) + ")\n")
  return ObjBobo(id, atrs)
  
def muda_obj(obj, alts):
  sys.stderr.write("Alterando ObjBobo, id = " + obj.id + " alts = " + str(alts) + "\n")
  assert len(alts) <= len(obj.atrs)
  for k, v in alts.items():
    assert k in obj.atrs
    obj.atrs[k] = v
    
cols = (
  ('nome',   type("foo"), 'TEXT',     3,   60),
  ('email',  type("foo"), 'TEXT',     6,   60),
  ('CPF',    type("foo"), 'TEXT',    14,   14),
  ('pernas', type(10),    'INTEGER',  2, 1000)
)

nome_tb = "objs"
let = "X"
cache = {}.copy()

sys.stderr.write("testando {tabela_generica.cria_tabela}:\n")
res = tabela_generica.cria_tabela(nome_tb, cols)
sys.stderr.write("Resultado = " + str(res) + "\n")
 
sys.stderr.write("testando {tabela_generica.limpa_tabela}:\n")
res = tabela_generica.limpa_tabela(nome_tb, cols)
sys.stderr.write("Resultado = " + str(res) + "\n")

# ----------------------------------------------------------------------
sys.stderr.write("testando {tabela_generica.acrescenta}:\n")
atrs1 = {
  "nome": "José Primeiro", 
  "email": "primeiro@ic.unicamp.br", 
  "CPF": "123.456.789-00", 
  "pernas": 4
}
id1 = "X-00000001"
obj1 = tabela_generica.acrescenta(nome_tb, cache, let, cols, cria_obj, atrs1)
mostra_obj("obj1", obj1, id1, atrs1)

atrs2 = {
  "nome": "João Segundo", 
  "email": "segundo@ic.unicamp.br", 
  "CPF": "987.654.321-99", 
  "pernas": 2
}
id2 = "X-00000002"
obj2 = tabela_generica.acrescenta(nome_tb, cache, let, cols, cria_obj, atrs2)
mostra_obj("obj2", obj2, id2, atrs2)

# ----------------------------------------------------------------------
sys.stderr.write("testando {tabela_generica.busca_por_identificador}:\n")

obj1_a = tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, cria_obj, id1)
mostra_obj("obj1_a", obj1_a, id1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("testando {tabela_generica.busca_por_campo}:\n")

em2 = atrs2['email']
res = tabela_generica.busca_por_campo(nome_tb, cache, let, cols, 'email', em2) 
mostra_lista_ids("email = " + em2, res)

CPF1 = "123.456.789-00"
res = tabela_generica.busca_por_campo(nome_tb, cache, let, cols, 'CPF', CPF1)
mostra_lista_ids("CPF = " + CPF1, res)

# ----------------------------------------------------------------------
sys.stderr.write("testando {tabela_generica.atualiza}:\n")

alts1 = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
tabela_generica.atualiza(nome_tb, cache, let, cols, cria_obj, muda_obj, id1, alts1)
obj1_c = tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, cria_obj, id1)
for k, v in alts1.items():
  atrs1[k] = v
mostra_obj("obj1_c", obj1_c, id1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("destruindo a tabela com {base_sql.executa_comando_DROP_TABLE}:\n")
res = base_sql.executa_comando_DROP_TABLE(nome_tb)
sys.stderr.write("Resultado = " + str(res) + "\n")
