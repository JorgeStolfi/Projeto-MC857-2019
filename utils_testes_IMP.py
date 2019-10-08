# Implementação do módulo {utils_testes}.

import sys
import re
import inspect
import json

def erro_prog(mens):
  fr = inspect.stack()[2]
  sys.stderr.write("  File %s, line %d, in %s: ** erro: %s\n" % (fr[1],fr[2],fr[3],mens))
  assert False

def aviso_prog(mens, grave):
  fr = inspect.stack()[2]
  tipo = ("** erro" if grave else "!! aviso")
  sys.stderr.write("  File %s, line %d, in %s: %s %s\n" % (fr[1],fr[2],fr[3],tipo,mens))
  return

def mostra(ind,mens):
  sys.stderr.write("%*s%s\n" % (ind,'',mens))

def verifica_objeto(modulo, tipo, obj, indice, ident, atrs): 

  ok = True # Este teste deu OK?

  if obj == None:
    sys.stderr.write("None\n")
  elif not type(obj) is tipo:
    aviso_prog("tipo do objeto " + str(type(obj)) + " inválido", True)
    ok = False
  else:
    sys.stderr.write("  testando {obtem_indice()}:\n")
    indice_cmp = modulo.obtem_indice(obj)
    if indice_cmp != indice:
      aviso_prog("retornou " + str(indice_cmp) + ", deveria ter retornado " + str(indice), True)
      ok = False

    sys.stderr.write("  testando {obtem_identificador()}:\n")
    ident_cmp = modulo.obtem_identificador(obj)
    if ident_cmp != ident:
      aviso_prog("retornou " + str(ident_cmp) + ", deveria ter retornado " + str(ident), True)
      ok = False

    sys.stderr.write("  testando {obtem_atributos()}:\n")
    atrs_cmp = modulo.obtem_atributos(obj)
    if atrs_cmp != atrs:
      aviso_prog("retornou " + str(atrs_cmp) + ", deveria ter retornado " + str(atrs), True)
      ok = False
    
    sys.stderr.write("testando {busca_por_indice()}:\n")
    obj1 = modulo.busca_por_indice(indice)
    if obj1 != obj:
      aviso_prog("retornou " + str(obj1) + ", deveria ter retornado " + str(obj), True)
      ok = False

    sys.stderr.write("testando {busca_por_identificador()}:\n")
    obj1 = modulo.busca_por_identificador(ident)
    if obj1 != obj:
      aviso_prog("retornou " + str(obj1) + ", deveria ter retornado " + str(obj), True)
      ok = False

  return ok

def formata_dict(dados):
  """Esta função de depuração recebe um dicionário {dados}
  e devolve um string é um fragmento HTML5 que mostra esses
  dados em formato relativamente legível (JSON com quebras de
  linha e indentação)."""
  dados_lin = json.dumps(dados, indent='&nbsp;&nbsp;', sort_keys=True, separators=(',<br/>', ': '))
  dados_lin = re.sub(r'\[', '[<br/>', dados_lin)
  dados_lin = re.sub(r'\{', '{<br/>', dados_lin)
  dados_lin = re.sub(r'\},', '  \},', dados_lin)
  return dados_lin
