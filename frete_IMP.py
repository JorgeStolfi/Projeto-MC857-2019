import sys

def calcula(cep,peso,volume):
  #dicionario generico para testes
  cep_dict = {str(i):i*0.1 for i in range(99)}
  #valores arbitrarios para testes
  A=5
  B=0.75
  C=0.75

  peso_pacote = A + (B*volume) + (C*peso)
  regiao = str(cep)[:2]
  fator_dist = cep_dict[regiao]
  frete = fator_dist*(peso_pacote)
  return frete