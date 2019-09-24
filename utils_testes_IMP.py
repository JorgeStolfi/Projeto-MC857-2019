# Implementação do módulo {utils_testes}.

import sys
import inspect

def erro_prog(mens):
  fr = inspect.stack()[2]
  sys.stderr.write("  File %s, line %d, in %s: ** erro: %s\n" % (fr[1],fr[2],fr[3],mens))
  assert False

def mostra(ind,mens):
  sys.stderr.write("%*s%s\n" % (ind,'',mens))

def verifica_objeto(titulo, modulo, tipo, obj, indice, ident, atrs): 
  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write(titulo + ":\n")
  ok = True # Este teste deu OK?
  if obj == None:
    sys.stderr.write("None\n")
  elif not type(obj) is tipo:
    sys.stderr.write("  **erro: tipo do objeto " + str(type(obj)) + " inválido\n")
    ok = False
  else:
    sys.stderr.write("  testando {obtem_indice()}:\n")
    indice_cmp = modulo.obtem_indice(obj)
    if indice_cmp != indice:
      sys.stderr.write("  **erro: retornou " + str(indice_cmp) + ", deveria ter retornado " + str(indice) + "\n")
      ok = False

    sys.stderr.write("  testando {obtem_identificador()}:\n")
    ident_cmp = modulo.obtem_identificador(obj)
    if ident_cmp != ident:
      sys.stderr.write("  **erro: retornou " + str(ident_cmp) + ", deveria ter retornado " + str(ident) + "\n")
      ok = False

    sys.stderr.write("  testando {obtem_atributos()}:\n")
    atrs_cmp = modulo.obtem_atributos(obj)
    if atrs_cmp != atrs:
      sys.stderr.write("  **erro: retornou " + str(atrs_cmp) + ", deveria ter retornado " + str(atrs) + "\n")
      ok = False
    
    sys.stderr.write("testando {busca_por_indice()}:\n")
    obj1 = modulo.busca_por_indice(indice)
    if obj1 != obj:
      sys.stderr.write("  **erro: retornou " + str(obj1) + ", deveria ter retornado " + str(obj) + "\n")
      ok = False

    sys.stderr.write("testando {busca_por_identificador()}:\n")
    obj1 = modulo.busca_por_identificador(ident)
    if obj1 != obj:
      sys.stderr.write("  **erro: retornou " + str(obj1) + ", deveria ter retornado " + str(obj) + "\n")
      ok = False

  # Resultado deste teste:
  if not ok:
    sys.stderr.write("  **erro: teste falhou \n")
  sys.stderr.write("%s\n" % ("-" * 70))
  return ok
