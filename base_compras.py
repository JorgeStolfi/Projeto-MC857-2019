# Funções para acesso à base de dados dos compras.

# Cada entrada da base de compras tem os mesmos atributos de um objeto de 
# classe {Compra}, menos o identificador.  Cada entrada tem um índice 
# inteiro (chave primária) que é atribuído quando a entrada é criada.

# Implementação desta interface:
import base_compras_IMP

# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base}
# que representa a base de dados da loja.

def busca_por_indice(bas,ind):
  """Devolve um objeto da classe {Compra} extraído da base de compras, 
  dado seu índice inteiro {ind} na base."""
  return base_compras_IMP.busca_por_indice(bas,ind)

def acrescenta(bas,ped):
  """Dado um objeto {ped} da classe {Compra}, acrescenta uma nova entrada
  na base com os dados desse pedido de compra (menos o identificador, que é
  ignorado). Devolve o índice inteiro da compra na base."""
  return base_compras_IMP.acrescenta(ped)

def atualiza(bas,ind,ped):
  """Dado um objeto {ped} da classe {Compra}, atualiza
  a entrada de índice {ind} da base com os os atributos de {ped} 
  (menos o identificador, que é ignorado).  

  O objeto {ped} não é alterado.  A função não devolve nenhum resultado."""
  base_compras_IMP.atualiza(ind,ped)

