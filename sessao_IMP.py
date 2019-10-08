
# Para diagnóstico:
import sys
import tabela_generica
import tabelas
import usuario
import conversao_sql
import identificador
import sessao
import compra
from utils_testes import erro_prog, mostra

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
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {ObjUsuario}:

class ObjSessao_IMP:
  def __init__(self, id_sessao, atrs):
    global cache, nome_tb, letra_tb, colunas, diags
    self.id_sessao = id_sessao
    self.atrs = atrs.copy()

# Implementações:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  colunas = \
    ( ( "usr",          usuario.ObjUsuario, 'INTEGER', False,   0,  99999999  ),    # Objeto/índice do usuário.
      ( "abrt",         type(False),        'INTEGER', False,   0,         1  ),    # Estado da sessao (1 = aberta).
      ( "cookie",       type("foo"),        'TEXT',    False,  10,        45  ),    # Cookie da sessao
      ( "carrinho",     compra.ObjCompra,   'INTEGER', True,    0,  99999999  )     # Objeto carrinho
    )
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
 
def cria(usr, cookie, carrinho):
  global cache, nome_tb, letra_tb, colunas, diags
  # Insere na base de dados e obtém o índice na mesma:
  atrs_SQL = { 'usr': usuario.obtem_indice(usr), 'abrt': 1, 'cookie': cookie, 'carrinho' : compra.obtem_indice(carrinho)}
  ses = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  if not type(ses) is sessao.ObjSessao:
    erro_prog("resultado de tipo inválido = " + str(ses))
  return ses

def obtem_identificador(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return ses.id_sessao

def obtem_indice(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return identificador.para_indice(letra_tb, ses.id_sessao)

def obtem_atributos(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return ses.atrs.copy()

def obtem_usuario(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return ses.atrs['usr']

def obtem_cookie(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return ses.atrs['cookie']

def aberta(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return ses.atrs['abrt']

def obtem_carrinho(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  return ses.atrs['carrinho']

def busca_por_identificador(id_sessao):
  global cache, nome_tb, letra_tb, colunas, diags
  ses = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_sessao)
  return ses

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas, diags
  ses = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return ses

def muda_atributos(ses, mods):
  global cache, nome_tb, letra_tb, colunas, diags
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice);
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, ses.id_sessao, mods_SQL)
  if res != ses:
    erro_prog("resultado inesperado = " + str(res))
  return

def fecha(ses):
  global cache, nome_tb, letra_tb, colunas, diags
  # !!! Verificar se a sessão não é {None} e está aberta. !!!
  mods = { 'abrt': False }
  muda_atributos(ses, mods)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  # Identificador de usuários e cookie de cada sessão:
  lista_ucs = \
    [ 
      ( "U-00000001", "ABCDEFGHIJK", "C-00000001" ),
      ( "U-00000001", "BCDEFGHIJKL", "C-00000002" ),
      ( "U-00000002", "CDEFGHIJKLM", "C-00000003" )
    ]
  for id_usuario, cookie, id_carrinho in lista_ucs:
    usr = usuario.busca_por_identificador(id_usuario)
    carrinho = compra.busca_por_identificador(id_carrinho)
    ses = cria(usr, cookie, carrinho)
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
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "produto_IMP.def_obj(" + str(obj) + ", " + id_sessao + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.indice_para_obj)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = sessao.ObjSessao(id_sessao, atrs_mem)
  else:
    assert obj.id_sessao == id_sessao
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.indice_para_obj)
    if diags: mostra(2, "modificando objeto, mods_mem = " + str(mods_mem))
    if len(mods_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      if chave == 'usr' and val != val_velho:
        erro_prog("campo '" + chave + "' não pode ser alterado")
      obj.atrs[chave] = val
  if diags: mostra(2, "obj = " + str(obj))
  return obj

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return
