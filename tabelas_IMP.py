# Implementação do módulo {tabelas}.

import sys

# Os principais objetos:
import usuario
import sessao
import produto
import compra

def inicializa_todas(limpa):
  usuario.inicializa(limpa)
  sessao.inicializa(limpa)
  produto.inicializa(limpa)
  compra.inicializa(limpa)

def obj_para_indice(obj, tipo):
  assert obj != None and type(obj) is tipo
  if tipo is usuario.ObjUsuario:
    ind = usuario.obtem_indice(obj)
  elif tipo is sessao.ObjSessao:
    ind = sessao.obtem_indice(obj)
  elif tipo is produto.ObjProduto:
    ind = produto.obtem_indice(obj)
  elif tipo is compra.ObjCompra:
    ind = compra.obtem_indice(obj)
  else:
    sys.stderr.write("**erro: objeto " + str(obj) + " com tipo inválido\n")
    assert False
  assert type(ind) is int
  assert ind >= 0 and ind <= 99999999
  return ind

def indice_para_obj(ind, tipo):
  sys.stderr.write("tabelas_IMP.indice_para_obj:\n")
  sys.stderr.write("  ind = " + str(ind) + "\n")
  sys.stderr.write("  tipo = " + str(tipo) + "\n")
  assert type(ind) is int
  assert ind >= 0 and ind <= 99999999
  if tipo is usuario.ObjUsuario:
    obj = usuario.busca_por_indice(ind)
  elif tipo is sessao.ObjSessao:
    obj = sessao.busca_por_indice(ind)
  elif tipo is produto.ObjProduto:
    obj = produto.busca_por_indice(ind)
  elif tipo is compra.ObjCompra:
    obj = compra.busca_por_indice(ind)
  else:
    sys.stderr.write("**erro: tipo Python '" + str(tipo) + "' invalido\n")
    assert False
  sys.stderr.write("  obj = " + str(obj) + "\n")
  assert obj == None or type(obj) is tipo
  return obj
  
