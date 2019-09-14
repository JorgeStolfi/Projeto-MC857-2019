
# Para diagnóstico:
import sys
import tabela_generica

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "sessoes"
  # Nome da tabela na base de dados.
  
letra_tb = "S"
  # Prefixo comum dos identificadores de sessao.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjSessao} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

colunas =  \
  (
    ( "id_usuario", type("foo"), 'TEXT NOT NULL',  10,  10  ), # Identificador do usuário, "U-{NNNNNNNN}".
    ( "aberta",     type(False), 'INT NOT NULL',    0.   1  )  # Estado da sessao (aberta?). 
  )
  # Descrição das colunas da tabela na base de dados.

def inicializa():
  global cache, nome_tb, colunas
  tabela_generica.cria_tabela(nome_tb, colunas)

class ObjSessao_IMP:
  def __init__(self, id_sessao, atrs):
    self.id_sessao = id_sessao
    self.atrs = atrs.copy()

def cria(usr):
  global cache, nome_tb, colunas
  # Insere na base de dados e obtém o índice na mesma:
  atrs = {'id_usuario': usuario.obtem_identificador(usr), 'aberta': False}
  atrs_SQL = ???(atrs)
  ses = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(ses) is ObjSessao_IMP:
    sys.stderr.write("sessao_IMP.cria: ** erro: " + str(ses) + "\n");
    assert False
  return ses

def obtem_identificador(ses):
  global cache, nome_tb, colunas
  return ses.id_sessao

def obtem_usuario(ses):
  global cache, nome_tb, colunas
  return ses.atrs['usr']

def aberta(ses):
  global cache, nome_tb, colunas
  return ses.atrs['ab']

def obtem_atributos(ses):
  global cache, nome_tb, colunas
  return ses.atrs.copy()

def busca_por_identificador(id_sessao):
  global cache, nome_tb, colunas
  ses = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_sessao)
  return ses

def muda_atributos(ses, mods):
  global cache, nome_tb, colunas
  mods_SQL = ???(mods)
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, ses.id_sessao, mods)
  if res != ses:
    sys.stderr.write("sessao_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def logout(ses):
  global cache, nome_tb, colunas
  mods = { 'aberta': False }
  muda_atributos(ses, mods)

def campos():
  global cache, nome_tb, colunas
  return colunas

# FUNÇÕES INTERNAS

def def_obj(obj, ident, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjSessao} com
  identificador {id_sessao} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjSessao}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, colunas
  sys.stderr.write("produto_IMP.def_obj(" + str(obj) + ", " + ident + ", " + str(atrs_SQL) + ") ...\n")
  if obj == None:
    atrs_mem = ???(atrs_SQL)
    sys.stderr.write("  criando objeto, atrs_mem = " + str(atrs) + "\n")
    obj = ObjSessao_IMP(ident, atrs_mem)
  else
    assert obj.id == ident
    mods_mem = ???(atrs_SQL)
    sys.stderr.write("  modificando objeto, mods_mem = " + str(atrs) + "\n")
    if len(mods) > len(obj.atributos):
      return "**erro: numero excessivo de atributos a alterar"
    for chave, val in mods.items():
      if not chave in obj.atributos:
        return "**erro: chave '" + chave + "' inválida"
      val_velho = obj.atributos[chave]
      if not type(val_velho) is type(val):
        return "**erro: tipo do campo '" + chave + "' incorreto"
      obj.atributos[chave] = val
  sys.stderr.write("  obj = " + str(obj) + "\n")
  return obj

