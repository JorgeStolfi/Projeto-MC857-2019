#! /usr/bin/python3

import sys
import identificador

ok_global = True  # Vira {False} se houver erro.

def verifica(rotulo, let, indice, ident):
  """Imprime os argumentos e verifica se conferem."""
  global ok_global
  ok = True # Estado deste teste.
  sys.stderr.write(rotulo + "\n")
  sys.stderr.write("  let = '" + let + "' indice = " + str(indice) + " ident = '" + str(ident) + "'\n")
  if not type(indice) is int:
    sys.stderr.write("  **erro - tipo de {indice} não é int\n")
    ok = False
  elif indice < 1 or indice > 99999999:
    sys.stderr.write("  **erro - valor de {indice} fora dos limites\n")
    ok = False
  if not type(ident) is str:
    sys.stderr.write("  **erro - tipo de {ident} não é str\n")
    ok = False
  elif len(ident) != 10:
    sys.stderr.write("  **erro - comprimento de {ident} incorreto\n")
    ok = False
  if ok:
    ident_esp = ("%s-%08d" % (let, indice))
    if ident != ident_esp:
      sys.stderr.write("  **erro - identificador não bate com indice\n")
      ok = False
  if ok:
    sys.stderr.write("  verifica: ok\n")
  ok_global = ok_global and ok
  
def verifica_lista(rotulo, let, indices, idents):
  """Verifica pares da lista."""
  global ok_global
  ok = True # Estado deste teste.
  if indices == None: indices = [].copy()
  sys.stderr.write(rotulo + "\n")
  if len(indices) != len(idents):
    sys.stderr.write("  **erro - tamanhos das listas não batem\n")
    ok = False
  else:
    pares = zip(indices, idents)
    for indel, ident in pares:
      if (type(indel) is tuple or type(indel) is list) and len(indel) == 1:
        indice = indel[0]
      else:
        indice = indel
      verifica("  ----------------------------------", let, indice, ident)
  if ok:
    sys.stderr.write("verifica_lista: ok\n")
  ok_global = ok_global and ok
 
let1 = "X"
indice1 = 123456
ident1 = identificador.de_indice(let1, indice1)
verifica("identificador.de_indice", let1, indice1, ident1)
 
let2 = "Y"
ident2 = "Y-00654321"
indice2 = identificador.para_indice(let2, ident2)
verifica("identificador.para_indice", let2, indice2, ident2)

let3 = "Z"
indices3 = [ 111, 222, [ 333 ], 444 ]
idents3 = identificador.de_lista_de_indices(let3, indices3)
verifica_lista("identificador.de_lista_de_indices", let3, indices3, idents3)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  # Terminou OK:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  # Termina com erro:
  sys.stderr.write("**erro - teste falhou\n")
  assert False
