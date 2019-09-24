# Funções úteis para testes.

import utils_testes_IMP

def erro_prog(mens):
  """Escreve a mensagem {mens} na saída {sys.stderr},
  e aborta a execução com {assert False}.  
  
  Esta função deve ser chamada apenas para informar erros do programa. 
  Erros em dados fornecidos pelo usuário devem ser enviados ao browser na forma
  de uma página HTML com a mensagem de erro."""
  utils_testes_IMP.erro_prog(mens)

def mostra(ind,mens):
  """Escreve a mensagem {mens} na saída {sys.stderr}, indentada de {ind} colunas.
  Útil para imprimir variáveis internas no diagnóstico de programas"""
  utils_testes_IMP.mostra(ind,mens)

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
