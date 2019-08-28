import sys

Error = "Erro"

def connect():
    sys.stderr.write("Conectado com a base \n")

def conecta():
    sys.stderr.write("Conectado com a base \n")

def busca_por_palavra(bas, pal):
  cmd = "SELECT " + pal + " FROM produto"
  print("Produtos encontrados: " + cmd)
  return cmd

def busca_por_indice(bas, ind):
  cmd = "SELECT " + ind + " FROM produto"
  print("Produtos encontrados: "+ cmd)
  return cmd

def acrescenta(bas,prod):
  sys.stderr.write("!! base_produtos_IMP.acrescenta: a implementar\n")
  return 12345
  
def atualiza(bas,ind,prod):
  sys.stderr.write("!! base_produtos_IMP.atualiza: a implementar\n")
  return 12345
