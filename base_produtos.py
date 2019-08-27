# Funções para acesso à base de dados dos produtos.

# Implementação desta interface:
import base_produtos_IMP 

# Cada entrada da base de produtos tem os mesmos atributos de um objeto de 
# classe {Produto}, menos o identificador.  Cada entrada tem um índice 
# inteiro (chave primária) que é atribuído quando a entrada é criada.

# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base}
# que representa a base de dados da loja.

def busca_por_indice(bas,ind):
  """Devolve um objeto da classe {Produto} extraído da base de produtos, 
  dado seu índice inteiro {ind} na base."""
  return base_produtos_IMP.busca_por_indice(bas,ind)

def busca_por_palavra(bas,pal):
  """Devolve uma lista Python de objetos da classe {Produto}, consistindo
  de todos os produtos da base que tem a cadeia {pal} nas suas descrições
  (curta, média, e longa), em ordem arbitrária. Se não houver nenhum 
  produto que satisfaça essa busca, devolve uma lista vazia."""
  return base_produtos_IMP.busca_por_palavra(bas,pal)

def acrescenta(bas,prod):
  """Dado um objeto {prod} da classe {Produto}, acrescenta uma nova entrada
  na base com os dados desse produto (menos o identificador, que é
  ignorado). Devolve o índice inteiro do produto na base."""
  return base_produtos_IMP.acrescenta(bas,prod)

def atualiza(bas,ind,prod):
  """Dado um objeto {prod} da classe {Produto}, atualiza
  a entrada da base com os os atributos de {prod};
  menos o identificador.  A entrada é localizada pelo
  seu índice inteiro {ind}.

  O objeto {prod} não é alterado.  A função não devolve nenhum resultado."""
  base_produtos_IMP.atualiza(bas,ind,prod)
