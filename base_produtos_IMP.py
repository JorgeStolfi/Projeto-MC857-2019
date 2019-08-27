#!/usr/bin/python3

#Implementação de {base_produtos.py}

import sys
import base

def busca_por_palavra(bas, pal):
  cmd = "SELECT nome FROM produto"
  produtos_econtrados = bas.executa_comando(cmd)
  print("Produtos encontrados: "+produtos_econtrados)
  return produtos_econtrados

def busca_por_indice(bas,ind):
  cmd = "SELECT ind FROM produto"
  produtos_econtrados = bas.executa_comando(cmd)
  print("Produtos encontrados: "+produtos_econtrados)
  return produtos_econtrados

def acrescenta(bas,prod):
  sys.stderr.write("!! base_produtos_IMP.acrescenta: a implementar\n")
  return 12345
  
def atualiza(bas,ind,prod):
  sys.stderr.write("!! base_produtos_IMP.atualiza: a implementar\n")
  return
