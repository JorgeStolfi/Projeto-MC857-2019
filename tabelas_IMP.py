# Implementação do módulo {tabelas}.

# Os principais objetos:
import usuario; from usuario_IMP import ObjUsuario_IMP
import produto; from produto_IMP import ObjProduto_IMP
import compra; from compra_IMP import ObjCompra_IMP
import sessao; from sessao_IMP import ObjSessao_IMP

def inicializa_todas(limpa):
  usuario.inicializa(limpa)
  produto.inicializa(limpa)
  compra.inicializa(limpa)
  sessao.inicializa(limpa)

def obtem_indice(obj, tipo):
  assert type(obj) is tipo
  if type(obj) is ObjUsuario_IMP:
    ind = usuario.obtem_indice(obj)
  elif type(obj) is ObjCompra_IMP:
    ind = compra.obtem_indice(obj)
  elif type(obj) is ObjProduto_IMP:
    ind = produto.obtem_indice(obj)
  elif type(obj) is ObjSessao_IMP:
    ind = sessao.obtem_indice(obj)
  else:
    sys.stderr.write("**erro: objeto " + str(obj) + " com tipo inválido\n")
    assert False
  return ind

def obtem_obj(ind, tipo):
  assert type(ind) is int
  assert ind >= 0 and ind <= 99999999
  if tipo is type(ObjUsuario_IMP):
    obj = usuario.busca_por_indice(ind)
  elif tipo is type(ObjCompra_IMP):
    obj = compra.busca_por_indice(ind)
  elif tipo is type(ObjProduto_IMP):
    obj = produto.busca_por_indice(ind)
  elif tipo is type(ObjSessao_IMP):
    obj = sessao.busca_por_indice(ind)
  else:
    sys.stderr.write("**erro: tipo Python '" + str(tipo) + "' invalido\n")
    assert False
