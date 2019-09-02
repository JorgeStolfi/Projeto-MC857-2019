# Funções para acesso à base de dados dos compras.

# Cada entrada da base de compras tem os mesmos atributos de um objeto de 
# classe {Compra}, menos o identificador.  Cada entrada tem um índice 
# inteiro (chave primária) que é atribuído quando a entrada é criada.

# Implementação desta interface:
import base_compras_IMP

# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base}
# que representa a base de dados da loja.

def busca_por_indice(bas,ind):
  """Devolve um objeto da classe {Compra} extraído da tabela de compras
  da base {bas}, dado seu índice inteiro {ind} na base."""
  return base_compras_IMP.busca_por_indice(bas,ind)

def acrescenta(bas,cpr):
  """Dado um objeto {cpr} da classe {Compra}, acrescenta uma nova entrada
  na tabela compras da base {bas}
  com os dados desse pedido de compra (menos o identificador, que é
  ignorado). Devolve o índice inteiro da compra na base."""
  return base_compras_IMP.acrescenta(bas,cpr)

def atualiza(bas,ind,cpr):
  """Dado um objeto {cpr} da classe {Compra}, atualiza
  a entrada de índice {ind} da tabela de compras da base com os os atributos de {cpr} 
  (menos o identificador, que é ignorado).  

  O objeto {cpr} não é alterado.  A função não devolve nenhum resultado."""
  base_compras_IMP.atualiza(bas,ind,cpr)

