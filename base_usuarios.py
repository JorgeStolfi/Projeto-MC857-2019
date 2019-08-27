# Funções para acesso à base de dados dos usuários.

# Cada entrada da base de usuários tem os mesmos atributos de um objeto de 
# classe {Usuario}, menos o identificador.  Cada entrada tem um índice 
# inteiro (chave primária) que é atribuído quando a entrada é criada.

# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base}
# que representa a base de dados da loja.

# Implementação desta interface:
import base_usuarios_IMP

def busca_por_indice(bas,ind):
  """Devolve um objeto da classe {Usuario} extraído da base de usuários, 
  dado seu índice inteiro {ind} na base."""
  return base_usuarios_IMP.busca_por_indice(bas,ind)

def busca_por_email(bas,em):
  """Devolve um objeto da classe {Usuario} extraído da base de usuários, 
  dado seu endereço de email {em}."""
  return base_usuarios_IMP.busca_por_email(bas,em)

def busca_por_CPF(bas,CPF):
  """Devolve um objeto da classe {Usuario} extraído da base de usuários, 
  dado seu número CPF {CPF} (um string no formato padrão, "NNN.NNN.NNN-KK"."""
  return base_usuarios_IMP.busca_por_CPF(bas,CPF)

def acrescenta(bas,usr):
  """Dado um objeto {usr} da classe {Usuario}, acrescenta uma nova entrada
  na base com os dados desse usuário (menos o identificador, que é
  ignorado). Devolve o índice inteiro do usuário na base."""
  return base_usuarios_IMP.acrescenta(bas,usr)

def atualiza(bas,ind,usr):
  """Dado um objeto {usr} da classe {Usuario}, atualiza
  a entrada de índice {ind} da base com os os atributos de {usr},
  menos seu identificador.  A entrada é localizada pelo
  seu índice inteiro {ind}.

  O objeto {usr} não é alterado.  A função não devolve nenhum resultado."""
  base_usuarios_IMP.atualiza(bas,ind,usr)
