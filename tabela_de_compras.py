# Funções para acesso à tabela de pedidos de compras.

# Cada linha desta tabela representa um pedido de compras (ou um
# carrinho de compras) de um cliente. Tem a maioria dos campos de
# objeto de classe {ObjCompra}, menos os itens da compra
# (que estão numa tabela separada, {tabela_de_itens_de_compras.py}. 
# 
# Cada linha tem um índice inteiro (chave primária) que é atribuído
# quando a linha é criada. As funções e métodos desta base manuseiam o
# índice na forma de um identificador de compra "C-{NNNNNNNN}".
# 
# Especificamente, cada linha tem os seguintes campos de informação
# (colunas da tabela):
#   
#   'id_compra' {str} O identificador do pedido de compra, "C-{NNNNNNNN}".
#   'id_usuario' {str} O identificador do cliente da compra, "U-{NNNNNNNN}".
#   'status' {str} O status da compra: 'aberto', 'pagando', etc.
#   
# Outros campos (como datas, endereço de entrega, forma de pagamento, etc.)
# serão acrescentados oportunamente.  Todos os campos, menos 
# 'id_compra' e 'id_usuario', podem ser alterados.
# 
# Nas funções abaixo, uma linha da tabela é representada na memória
# por um dicionário Python {atrs} cujas chaves e valores
# são os campos da linha.
# 
# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.  

# Implementação desta interface:
import tabela_de_compras_IMP

def cria_tabela(bas):
  """Cria a tabela de compras na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  tabela_de_compras_IMP.cria_tabela(bas)

def acrescenta(bas,atrs):
  """Acrescenta uma nova linha na tabela de compras
  da base {bas}, cujo conteúdo é o dicionário {atrs},
  e devolve o identificador "C-{NNNNNNNN}" da mesm.
  O dicionário não deve conter o campo 'id_compra'."""
  return tabela_de_compras_IMP.acrescenta(bas,atrs)

def busca_por_identificador(bas,id_compra):
  """Devolve um dicionário {atrs} com o conteúdo da linha 
  de identificador {id_compra} da tabela de compras da base {bas}.
  O dicionário não inclui o campo 'id_compra'."""
  return tabela_de_compras_IMP.busca_por_identificador(bas,id)

def atualiza(bas,id_compra,atrs):
  """Modifica alguns campos de uma linha da tabela de compras da base {bas}.
  A linha é especificada pelo seu identificador {id_compra}.  Não devolve 
  nenhum resultado.
  
  O parâmetro {atrs} deve ser um dicionário cujas chaves são um
  subconjunto dos nomes dos campos da linha (excluindo 'id_compra').
  Os valores desses campos na tabela são substituídos pelos valores em {atrs}."""
  tabela_de_compras_IMP.atualiza(bas,id_compra,atrs)
