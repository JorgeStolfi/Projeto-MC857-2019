
# Para diagnóstico:
import sys
import tabela_generica
import tabelas
import usuario
import conversao_sql
import identificador
import sessao

# VARIÁVEIS GLOBAIS DO MÓDULO
 
cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjSessao} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "sessoes"
  # Nome da tabela na base de dados.
 
letra_tb = "S"
  # Prefixo comum dos identificadores de sessao.

colunas = None
  # Descrição das colunas da tabela na base de dados.

# Definição interna da classe {ObjUsuario}:

class ObjSessao_IMP:
  def __init__(self, id_sessao, atrs):
    global cache, nome_tb, letra_tb, colunas
    self.id_sessao = id_sessao
    self.atrs = atrs.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas
  colunas = \
    ( ( "usr",     usuario.ObjUsuario,  'INTEGER', False,   0,  99999999  ), # Objeto/índice do usuário.
      ( "abrt",    type(False),         'INTEGER', False,   0,         1  ), # Estado da sessao (1 = aberta).
      ( "cookie",  type("foo"),         'TEXT',    False,  10,        45  )  # Cookie da sessao
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
 
def cria(usr, cookie):
  global cache, nome_tb, letra_tb, colunas
  # Insere na base de dados e obtém o índice na mesma:
  atrs_SQL = { 'usr': usuario.obtem_indice(usr), 'abrt': 1, 'cookie': cookie }
  ses = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(ses) is sessao.ObjSessao:
    sys.stderr.write("sessao_IMP.cria: ** erro: " + str(ses) + "\n");
    assert False
  return ses

def obtem_identificador(ses):
  global cache, nome_tb, letra_tb, colunas
  return ses.id_sessao

def obtem_indice(ses):
  global cache, nome_tb, letra_tb, colunas
  return identificador.para_indice(letra_tb, ses.id_sessao)

def obtem_atributos(ses):
  global cache, nome_tb, letra_tb, colunas
  return ses.atrs.copy()

def obtem_usuario(ses):
  global cache, nome_tb, letra_tb, colunas
  return ses.atrs['usr']

def obtem_cookie(ses):
  global cache, nome_tb, letra_tb, colunas
  return ses.atrs['cookie']

def aberta(ses):
  global cache, nome_tb, letra_tb, colunas
  return ses.atrs['abrt']

def busca_por_identificador(id_sessao):
  global cache, nome_tb, letra_tb, colunas
  ses = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_sessao)
  return ses

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas
  ses = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return ses

def muda_atributos(ses, mods):
  global cache, nome_tb, letra_tb, colunas
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice);
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, ses.id_sessao, mods_SQL)
  if res != ses:
    sys.stderr.write("sessao_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def fecha(ses):
  global cache, nome_tb, letra_tb, colunas
  mods = { 'abrt': False }
  muda_atributos(ses, mods)

def campos():
  global cache, nome_tb, letra_tb, colunas
  return colunas

def cria_testes():
  global cache, nome_tb, letra_tb, colunas
  inicializa(True)
  # Identificador de usuários e cookie de cada sessão:
  lista_ucs = \
    [ 
      ( "U-00000001", "ABCDEFGHIJK" ),
      ( "U-00000001", "BCDEFGHIJKL" ),
      ( "U-00000003", "CDEFGHIJKLM" )
    ]
  for id_usuario, cookie in lista_ucs:
    usr = usuario.busca_por_identificador(id_usuario)
    ses = cria(usr, cookie)
    assert ses != None and type(ses) is sessao.ObjSessao
  return

# FUNÇÕES INTERNAS

def def_obj(obj, id_sessao, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjSessao} com
  identificador {id_sessao} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjSessao}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas
  sys.stderr.write("produto_IMP.def_obj(" + str(obj) + ", " + id_sessao + ", " + str(atrs_SQL) + ") ...\n")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.indice_para_obj)
    sys.stderr.write("  criando objeto, atrs_mem = " + str(atrs_mem) + "\n")
    obj = sessao.ObjSessao(id_sessao, atrs_mem)
  else:
    assert obj.id_sessao == id_sessao
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.indice_para_obj)
    sys.stderr.write("  modificando objeto, mods_mem = " + str(mods_mem) + "\n")
    if len(mods_mem) > len(obj.atrs):
      sys.stderr.write("  **erro: numero excessivo de atributos a alterar\n")
      assert False
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        sys.stderr.write("  **erro: chave '" + chave + "' inválida\n")
        assert False
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        sys.stderr.write("  **erro: tipo do campo '" + chave + "' incorreto\n")
        assert False
      if chave == 'usr' and val != val_velho:
        sys.stderr.write("  **erro: campo '" + chave + "' não pode ser alterado\n")
        assert False
      obj.atrs[chave] = val
  sys.stderr.write("  obj = " + str(obj) + "\n")
  return obj

