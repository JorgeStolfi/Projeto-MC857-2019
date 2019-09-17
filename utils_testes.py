# Funções úteis para testes.

import utils_testes_IMP

def verifica_objeto(titulo, modulo, tipo, obj, indice, ident, atrs):
  """Faz testes de consistência básicos de um objeto {obj} de classe {tipo}, 
  que deve ser uma das classes principais do sistems, como {ObjUsuario}, {ObjProduto}, etc.;
  dados o indice esperado {indice} na tabela correspondente da base de dados, o
  identificador esperado {ident}, e os atributos esperados {atrs}.
  
  
  Especifcamente, verifica as funções {obtem_indice(obj)}, {obtem_identificador(obj)},
  {obtem_atributos(obj)}, {busca_por_indice(indice)} e {busca_por_identificador(ident)}
  do {modulo} dado.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return utils_testes_IMP.verifica_objeto(titulo, modulo, tipo, obj, indice, ident, atrs)
