# Funções para acesso à tabela de produtos.

# Cada linha desta tabela representa um produto do catálogo da loja.
# Tem a maioria dos campos de um objeto de classe {ObjProduto}. 
# 
# Cada linha tem um índice inteiro (chave primária) que é atribuído
# quando a linha é criada. As funções e métodos desta base manuseiam o
# índice na forma de um identificador de produto "P-{NNNNNNNN}".
# 
# Especificamente, cada linha tem os seguintes campos de informação
# (colunas da tabela):
#   
#   'id_produto' {str} O identificador do produto, "P-{NNNNNNNN}".
#   'descr_curta' {str} - descrição do produto em uma linha.
#   'descr_media' {str} - descrição do produto em 4 linhas, com dimensões etc.
#   'descr_longa' {str} - descrição completa do produto. 
#   'unid' {str} - unidade ("item", "caixa de 10", "metro", "rolo de 5m", etc.) 
#   'preco' {decimal(12,2)} - preço unitário.
#   
# Outros campos (como peso, volume, estoque, imagens, palvras-chave, etc.)
# serão acrescentados oportunamente.
# 
# Todos os campos, exceto 'id_produto', podem ser alterados
# (por exemplo para corrigir erros).
# 
# Nas funções abaixo, uma linha da tabela é representada na memória
# por um dicionário Python {atrs} cujas chaves e valores
# são os campos da linha.
# 
# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.  

# Implementação desta interface:
import tabela_de_produtos_IMP 

def cria_tabela(bas):
  """Cria a tabela de produtos na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  tabela_de_produtos_IMP.cria_tabela(bas)

def acrescenta(bas,atrs):
  """Acrescenta uma nova linha na tabela de produtos
  da base {bas}, cujo conteúdo é o dicionário {atrs},
  e devolve o identificador "P-{NNNNNNNN}" da mesma.
  O dicionário não deve conter o campo 'id_produto'."""
  return tabela_de_produtos_IMP.acrescenta(bas,atrs)

def busca_por_identificador(bas,id_produto):
  """Devolve um dicionário {atrs} com o conteúdo da linha 
  de identificador {id_produto} da tabela de produtos da base {bas}.
  O dicionário não inclui o campo 'id_produto'."""
  return tabela_de_produtos_IMP.busca_por_identificador(bas,id_produto)

def busca_por_palavra(bas,pal):
  """Devolve uma lista com todos os identificadores "P-{NNNNNNNN}"
  dos produtos que contém a palavra {pal} nos seus 
  campos 'descr_curta' ou 'descr_media'.  Se não houver nenum item 
  satisfazendo a busca, devolve uma lista vazia."""
  return tabela_de_produtos_IMP.busca_por_palavra(bas,pal)

def atualiza(bas,id_produto,atrs):
  """Modifica alguns campos de uma linha da tabela de produtos da base {bas}.
  A linha é especificada pelo seu identificador {id_produto}. 
  Não devolve nenhum resultado.
  
  O parâmetro {atrs} deve ser um dicionário cujas chaves são um
  subconjunto dos nomes dos campos da linha (excluindo 'id_produto'). 
  Os valores desses campos na tabela são substituídos pelos valores em {atrs}."""
  tabela_de_produtos_IMP.atualiza(bas,id_produto,atrs)
