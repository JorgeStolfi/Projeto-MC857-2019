# Implementação do módulo {tabelas}.

import sys

# Os principais objetos:
import usuario
import produto
import compra
import sessao
from utils_testes import erro_prog, mostra

def inicializa_todas(limpa):
  usuario.inicializa(limpa)
  produto.inicializa(limpa)
  compra.inicializa(limpa) # Também chama {itens_de_compras.inicializa(limpa)}
  sessao.inicializa(limpa)

def cria_todos_os_testes():
  # A ordem é importante:
  usuario.cria_testes() # Não tem atributos de tipo objeto.
  produto.cria_testes() # Não tem atributos de tipo objeto.
  compra.cria_testes()  # Tem atributos de tipo {ObjUsuario} e {ObjProduto}. Cria também itens para as compras.
  sessao.cria_testes()  # Tem atributos de tipo {ObjUsuario} e {ObjCompra}.

def obj_para_indice(obj, tipo):
  assert obj != None and type(obj) is tipo
  if tipo is usuario.ObjUsuario:
    ind = usuario.obtem_indice(obj)
  elif tipo is produto.ObjProduto:
    ind = produto.obtem_indice(obj)
  elif tipo is compra.ObjCompra:
    ind = compra.obtem_indice(obj)
  elif tipo is sessao.ObjSessao:
    ind = sessao.obtem_indice(obj)
  else:
    erro_prog("objeto " + str(obj) + " com tipo inválido")
  assert type(ind) is int
  assert ind >= 0 and ind <= 99999999
  return ind

def indice_para_obj(ind, tipo):
  # sys.stderr.write("tabelas_IMP.indice_para_obj:\n")
  # sys.stderr.write("  ind = " + str(ind) + "\n")
  # sys.stderr.write("  tipo = " + str(tipo) + "\n")
  assert type(ind) is int
  assert ind >= 0 and ind <= 99999999
  if tipo is usuario.ObjUsuario:
    obj = usuario.busca_por_indice(ind)
  elif tipo is produto.ObjProduto:
    obj = produto.busca_por_indice(ind)
  elif tipo is compra.ObjCompra:
    obj = compra.busca_por_indice(ind)
  elif tipo is sessao.ObjSessao:
    obj = sessao.busca_por_indice(ind)
  else:
    erro_prog("tipo Python '" + str(tipo) + "' invalido")
  # sys.stderr.write("  obj = " + str(obj) + "\n")
  assert obj == None or type(obj) is tipo
  return obj
  
