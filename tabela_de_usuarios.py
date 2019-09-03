# Funções para acesso à tabela de usuários na base de dados da loja.

# Cada linha desta tabela representa um produto do catálogo da loja.
# Tem a maioria dos campos de um objeto de classe {ObjProduto}.  
# 
# Cada linha tem um índice inteiro (chave primária) que é atribuído
# quando a linha é criada. As funções e métodos desta base manuseiam o
# índice na forma de um identificador de usuário "U-{NNNNNNNN}".
# 
# Especificamente, cada linha tem os seguintes campos de informação
# (colunas da tabela):
#   
#   'id_usuario' {str} O identificador do usuario, "U-{NNNNNNNN}".
#   'nome' {str} - nome completo do usuário.
#   'senha' {str} - senha do usuário.
#   'email' {str} - endereço de email
#   'CPF' {str} - número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
#   'endereco' {str} - endereço completo, em 3 linhas (menos CEP).
#   'CEP' {str} - código de endereçamento postal completo ("{NNNNN}-{LLL}").
#   'telefone' {str} - telefone completo com DDI e DDD ("+{XX}({YY}){MMMM}-{NNNN}").
#   
# Outros campos (como RG, nascimento, preferências, etc.)
# serão acrescentados oportunamente.
#
# Além do 'id_usuario', os campos 'CPF' e 'email' de todos os usuários
# devem ser distintos.  Todos os campos podem ser alterados,
# exceto 'id_usuario' e 'CPF'.
# 
# Nas funções abaixo, uma linha da tabela é representada na memória
# por um dicionário Python {atrs} cujas chaves e valores
# são os campos da linha.
#
# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.

# Implementação desta interface:
import tabela_de_usuarios_IMP

def cria_tabela(bas):
  """Cria a tabela de usuarios na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  tabela_de_usuarios_IMP.cria_tabela(bas)

def acrescenta(bas,atrs):
  """Acrescenta uma nova linha na tabela de usuários da base {bas}, cujo
  conteúdo é o dicionário {atrs}, e devolve o identificador
  "U-{NNNNNNNN}" da mesma. O dicionário não deve conter o campo
  'id_usuario'. Não pode haver nenhum usuário na tabela com mesmo email
  e CPF. """
  return tabela_de_usuarios_IMP.acrescenta(bas,atrs)

def busca_por_identificador(bas,id_usuario):
  """Devolve um dicionário {atrs} com o conteúdo da linha 
  de identificador {id_usuario} da tabela de usuários da base {bas}.
  O dicionário não inclui o campo 'id_usuario'."""
  return tabela_de_usuarios_IMP.busca_por_identificador(bas,id_usuario)

def busca_por_email(bas,em):
  """Devolve o identificador do usuário na tabela cujo endereço de email
  é {em}. Se não houver tal usuário, devolve {None}."""
  return tabela_de_usuarios_IMP.busca_por_email(bas,em)

def busca_por_CPF(bas,CPF):
  """Devolve o identificador do usuário na tabela com o número 
  de {CPF} dado (um string no formato "{XXX}.{YYY}.{ZZZ}-{KK}".
  Se não houver tal usuário, devolve {None}."""
  return tabela_de_usuarios_IMP.busca_por_CPF(bas,CPF)

def atualiza(bas,id_usuario,atrs):
  """Modifica alguns campos de uma linha da tabela de usuários da base {bas}.
  A linha é especificada pelo seu identificador {id_usuario}.  
  Não devolve nenhum resultado.
  
  O parâmetro {atrs} deve ser um dicionário cujas chaves são um
  subconjunto dos nomes dos campos da linha (excluindo 'id_usuario'
  e 'CPF'). Os valores desses campos na tabela são substituídos pelos
  valores em {atrs}.  Se o atributo 'email' for alterado, não pode 
  haver nenhum usuário na tabela com mesmo email."""
  tabela_de_usuarios_IMP.atualiza(bas,id_usuario,atrs)
