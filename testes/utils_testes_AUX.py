# Módulo auxiliar para {utils_testes_TST.py}
# Define uma classe de objeto com os métodos padrões,
# e um objeto {obj1} dessa classe com atributos
# esperados {obj1_ind}, {obj1_id}, {obj1_atrs}.

# Casse de objeto e suas funções para teste:
class ObjTeste:
  
  def __init__(self,ind,id,atrs):
    self.ind = ind
    self.id = id
    self.atrs = atrs.copy()
    
def obtem_indice(obj):
  return obj.ind
  
def obtem_identificador(obj):
  return obj.id
  
def obtem_atributos(obj):
  return obj.atrs.copy()
  
obj1_ind = 100
obj1_id = ("X-%08d" % obj1_ind)
obj1_atrs = { 'coisa': 100, 'treco': 200, 'lhufas': [ 10, 100 ] }
obj1 = ObjTeste(obj1_ind, obj1_id, obj1_atrs)

def busca_por_indice(ind):
  if ind == obj1_ind:
    return obj1
  else:
    return None

def busca_por_identificador(id):
  if id == obj1_id:
    return obj1
  else:
    return None
