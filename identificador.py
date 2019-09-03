# Funções para conversão de identificador e índice

# Implementacao desta interface:
import identificador_IMP

def de_indice(let,ind):
  """Converte um índice inteiro {ind} em um string identificador da
  forma "{X}-{NNNNNNNN}" onde {X} é a string {let} dada e {NNNNNNNN} é o
  valor {ind} formatado em 8 algarismos decimais, com zeros à esquerda. Por exemplo,
  `identificador_de_indice("U",20557)` devolve "U-00020557".

  O índice {ind} deve estar em {0..99999999}. ({10^8-1})."""
  return identificador_IMP.de_indice(let,ind)

def para_indice(let,id):
  """Dado um identificador de objeto {ident}, da forma "{X}-{NNNNNNNN}",
  onde {X} deve ser a letra {let} dada, extrai o índice inteiro {NNNNNNNN} do 
  mesmo. Por exemplo, `indice_de_identificador("U","U-00020557")` devolve o inteiro 20555."""
  return identificador_IMP.para_indice(let,id)
