# Funções para conversão de identificador e índice

# Implementacao desta interface:
import identificador_IMP

def de_indice(let, indice):
  """Converte um índice inteiro {indice} em um string identificador da
  forma "{X}-{NNNNNNNN}" onde {X} é a string {let} dada e {NNNNNNNN} é o
  valor {indice} formatado em 8 algarismos decimais, com zeros à esquerda. Por exemplo,
  `identificador_de_indice("U",20557)` devolve "U-00020557".

  O índice {indice} deve estar em {0..99999999}. ({10^8-1})."""
  return identificador_IMP.de_indice(let,indice)

def para_indice(let, ident):
  """Dado um identificador de objeto {ident}, da forma "{X}-{NNNNNNNN}",
  onde {X} deve ser a letra {let} dada, extrai o índice inteiro {NNNNNNNN} do 
  mesmo. Por exemplo, `indice_de_identificador("U","U-00020557")` devolve o inteiro 20555."""
  return identificador_IMP.para_indice(let,ident)

def de_lista_de_indices(let, indices):
  """Dada uma lista de list {indices} de índices de linhas de uma tabela, devolve
  uma lista com os identificadores dos objetos correspondentes. Se {indices} for {None}
  ou uma lista vazia, devolve uma lista vazia.
  
  Para conveniência, cada elemento da lista {indices} pode ser um inteiro, ou uma
  lista ou tupla de tamanho 1 cujo único elemento é um inteiro."""
  return identificador_IMP.de_lista_de_indices(let,indices)
