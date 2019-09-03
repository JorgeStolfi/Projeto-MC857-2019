# Funções para acesso à tabela de itens de pedidos de compras.

# Cada linha desta tabela é um item de um pedido de compras:
# ou seja, uma determinada quantidade de um determinado produto.
# 
# Cada linha tem um índice inteiro (chave primária) que é atribuído
# quando a linha é criada. As funções e métodos desta base manuseiam o
# índice na forma de um identificador de item de compra "I-{NNNNNNNN}".
# 
# Especificamente, cada linha tem os seguintes campos de informação
# (colunas da tabela):
#   
#   'id_item' {str} O identificador do item, "I-{NNNNNNNN}".
#   'id_compra' {str} O identificador do pedido de compra, "C-{NNNNNNNN}".
#   'id_produto' {str} O identificador do produto a comprar, "P-{NNNNNNNN}".
#   'qt' {float} A quantidade a comprar.
#   'preco' {decimal(12,2)} o preço total do item.
# 
# Outros campos (como peso e volume) poderão vir a ser
# acrescentados oportunamente.
# 
# Todos os campos, exceto {id_item}, {id_compra}, e {id_produto}, 
# podem ser alterados.
# 
# Nas funções abaixo, uma linha da tabela é representada na memória
# por um dicionário Python {atrs} cujas chaves e valores
# são os campos da linha.
# 
# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.

# Implementação desta interface:
import tabela_de_itens_de_compras_IMP

def cria_tabela(bas):
  """Cria a tabela de itens de compras na base de dados {bas}. 
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  tabela_de_itens_de_compras_IMP.cria_tabela(bas)

def acrescenta(bas,atrs):
  """Acrescenta uma nova linha na tabela de itens de compras
  da base {bas}, cujo conteúdo é o dicionário {atrs}, e devolve
  o identificador "I-{NNNNNNNN}" da mesma.
  O dicionário não deve conter o campo 'id_item'."""
  return tabela_de_itens_de_compras_IMP.acrescenta(bas,atrs)

def busca_por_identificador(bas,id_item):
  """Devolve um dicionário {atrs} com o conteúdo da linha 
  de identificador {id_item} da tabela de itens de compras da base {bas}.
  O dicionário não inclui o campo 'id_item'."""
  return tabela_de_itens_de_compras_IMP.busca_por_identificador(bas,id_item)

def busca_por_compra(bas,id_compra):
  """Devolve uma lista com todos os identificadores "I-{NNNNNNNN}"
  dos itens cujo identificador de compra é 'id_compra'. 
  Se não houver nenum item satisfazendo a busca, devolve uma lista vazia."""
  return tabela_de_itens_de_compras_IMP.busca_por_compra(bas,id_compra)

def busca_por_produto(bas,id_produto):
  """Devolve uma lista com todos os identificadores "I-{NNNNNNNN}"
  dos itens cujo identificador de produto é 'id_produto'. 
  Se não houver nenum item satisfazendo a busca, devolve uma lista vazia."""
  return tabela_de_itens_de_compras_IMP.busca_por_produto(bas,id_produto)

def atualiza(bas,id_item,atrs):
  """Modifica alguns campos de uma linha da tabela de itens de compras da base {bas}.
  A linha é especificada pelo seu identificador {id_item}.  Não devolve nenhum resultado.
  
  O parâmetro {atrs} deve ser um dicionário cujas chaves são um
  subconjunto dos nomes dos campos da linha. Os valores desse campos na
  tabela são substituídos pelos valores em {atrs}.
  O dicionário {atrs} não deve ter a chave 'id_item'."""
  tabela_de_itens_de_compras_IMP.atualiza(bas,id_item,atrs)
