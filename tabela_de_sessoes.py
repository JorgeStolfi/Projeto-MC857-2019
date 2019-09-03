# Funções para acesso à base de dados das sessões.

# Cada linha desta tabela representa uma sessão de login, ativa ou 
# encerrada.  Os campos são basicamente os mesmos de um objeto de 
# classe {ObjSessao}. 
# 
# Cada linha tem um índice inteiro (chave primária) que é atribuído
# quando a linha é criada. As funções e métodos desta base manuseiam o
# índice na forma de um identificador de sessao "S-{NNNNNNNN}".
# 
# Especificamente, cada linha tem os seguintes campos de informação
# (colunas da tabela):
#   
#   'id_sessao' {str} O identificador do sessao, "S-{NNNNNNNN}".
#   'id_usuario' {str} - O identificador do usuário, "U-{NNNNNNNN}".
#   'aberta' {bool} - {True} se a sessão está ativa, {False} se o cliente deu logout.
#   
# Outros campos (como peso, volume, estoque, imagens, palvras-chave, etc.)
# serão acrescentados oportunamente.
# 
# O identificador 'id_sessao' de cada linha é atribuído sequencialmente
# quando a linha é criada.  Todos os campos, exceto 'id_sessao', e 'id_usuario',
# podem ser alterados.
# 
# Nas funções abaixo, uma linha da tabela é representada na memória
# por um dicionário Python {atrs} cujas chaves e valores
# são os campos da linha.

# Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.

# Implementação desta interface:
import tabela_de_sessoes_IMP

def cria_tabela(bas):
  """Cria a tabela de sessões na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  tabela_de_sessoes_IMP.cria_tabela(bas)

def acrescenta(bas,atrs):
  """Acrescenta uma nova linha na tabela de sessões
  da base {bas}, cujo conteúdo é o dicionário {atrs},
  e devolve o identificador "S-{NNNNNNNN}" da mesma.
  O dicionário não deve conter o campo 'id_sessao'."""
  return tabela_de_sessoes_IMP.acrescenta(bas,ses)

def busca_por_identificador(bas,id_sessao):
  """Devolve um dicionário {atrs} com o conteúdo da linha 
  de identificador {id_sessao} da tabela de sessões da base {bas}.
  O dicionário não inclui o campo 'id_sessao'."""
  return tabela_de_sessoes_IMP.busca_por_identificador(bas,id_sessao)

def atualiza(bas,id_sessao,atrs):
  """Modifica alguns campos de uma linha da tabela de sessões da base {bas}.
  A linha é especificada pelo seu identificador {id_sessao}. 
  Não devolve nenhum resultado.
  
  O parâmetro {atrs} deve ser um dicionário cujas chaves são um
  subconjunto dos nomes dos campos da linha (excluindo 'id_sessao'). 
  Os valores desses campos na tabela são substituídos pelos valores em {atrs}."""
  tabela_de_sessoes_IMP.atualiza(bas,id_sessao,atrs)
