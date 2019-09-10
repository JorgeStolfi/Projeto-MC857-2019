# Implementação do módulo {identificador}.

def de_indice(let,ind):
  assert type(let) is str and len(let) == 1
  assert type(ind) is int and ind >= 0
  return "%s-%08d" % (let,ind)

def para_indice(let,id):
  assert type(let) is str and len(let) == 1
  assert type(id) is str and len(id) == 10 
  assert id[0:1] == let 
  assert id[1:2] == "-"
  ind = int(id[2:])
  return ind
