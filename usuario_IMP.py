# Implementação do módulo {usuario} e da classe {ObjUsuario}.

import usuario

import tabela_generica
import conversao_sql
import identificador
import tabelas
import sys # Para diagnóstico.
from utils_testes import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "usuarios"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjUsuario} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "U"
  # Prefixo dos identificadores de usuários

colunas = \
  (
    ( 'nome',          type("foo"), 'TEXT',    False,   1,  60  ), # Nome completo.
    ( 'senha',         type("foo"), 'TEXT',    False,   8,  24  ), # Senha de login.
    ( 'email',         type("foo"), 'TEXT',    False,   6,  60  ), # Endereço de email
    ( 'CPF',           type("foo"), 'TEXT',    False,  14,  15  ), # Número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    ( 'endereco',      type("foo"), 'TEXT',    False,  30, 180  ), # Endereço completo, em 3 linhas (menos CEP).
    ( 'CEP',           type("foo"), 'TEXT',    False,   8,  10  ), # Código de endereçamento postal completo ("{NNNNN}-{LLL}").
    ( 'telefone',      type("foo"), 'TEXT',    False,   9,  40  ), # Telefone completo com DDI e DDD ("+{XXX}({YYY}){MMMMM}-{NNNN}").
    ( 'documento',     type("foo"), 'TEXT',    True,    6,  24  ), # Número do documento de identidade (RG, pasaporte, etc.)
    ( 'administrador', type(False), 'INTEGER', False,   0,   1  ), # Define se o usuário é administrador (1=administrador)
  )
  # Descrição das colunas da tabela na base de dados.
  
diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {ObjUsuario}:

class ObjUsuario_IMP:

  def __init__(self, id_usuario, atrs):
    global cache, nome_tb, letra_tb, colunas
    self.id_usuario = id_usuario
    self.atrs = atrs.copy()

# Implementação das funções:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs):
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"usuario_IMP.cria(" + str(atrs) + ") ...")

  # Verifica unicidade de CPF:
  for chave in ('CPF', 'email'):
    # Exige atributo {chave} único:
    if chave not in atrs:
      erro_prog("falta atributo '" + chave + "'")
    else:
      val = atrs[chave]
      if chave == 'CPF':
        id_bus = busca_por_CPF(val)
      elif chave == 'email':
        id_bus = busca_por_email(val)
      if id_bus != None:
        erro_prog("atributo '" + chave + "' já existe: " + id_bus)

  # Converte atibutos para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, tabelas.obj_para_indice)
  # Insere na base de dados e obtém o índice na mesma:
  usr = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, mods_SQL)
  if not type(usr) is usuario.ObjUsuario:
    erro_prog("tipo de objeto errado" + str(usr))
  return usr

def obtem_identificador(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return usr.id_usuario

def obtem_indice(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return identificador.para_indice(letra_tb, usr.id_usuario)

def obtem_atributos(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return usr.atrs.copy()

def muda_atributos(usr, mods):
  global cache, nome_tb, letra_tb, colunas, diags
  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice)
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, usr.id_usuario, mods_SQL)
  if res != usr:
    erro_prog(" acesso à tabela falhou res = " + str(res))
  return

def busca_por_identificador(id_usuario):
  global cache, nome_tb, letra_tb, colunas, diags
  usr = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_usuario)
  return usr

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas, diags
  usr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return usr

def busca_por_email(em):
  global cache, nome_tb, letra_tb, colunas, diags
  return busca_por_campo_unico('email', em)

def busca_por_CPF(CPF):
  global cache, nome_tb, letra_tb, colunas, diags
  return busca_por_campo_unico('CPF', CPF)

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      {
        'nome': "José Primeiro", 
        'senha': "123456789", 
        'email': "primeiro@gmail.com", 
        'CPF': "123.456.789-00", 
        'endereco': "Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP", 
        'CEP': "13083-418", 
        'telefone': "+55(19)9 9876-5432",
        'documento': "1.234.567-9 SSP-SP",
        'administrador': False,
      },
      {
        'nome': "João Segundo", 
        'senha': "987654321", 
        'email': "segundo@ic.unicamp.br", 
        'CPF': "987.654.321-99", 
        'endereco': "Avenida dos Semáforos, 1003\nJardim Pelado\nCampinas, SP", 
        'CEP': "13083-007", 
        'telefone': "+55(19)9 9898-1212",
        'documento': 'CD98765-43 PF',
        'administrador' : False,
      },
      {
        'nome': "Juca Terceiro", 
        'senha': "333333333", 
        'email': "terceiro@gmail.com", 
        'CPF': "111.111.111-11",
        'endereco': "Rua Zero, 0000\nVila Zero\nCampinas, SP",
        'CEP': "13083-999", 
        'telefone': "+55(19)9 9999-9999",
        'documento': None,
        'administrador' : True,
      }
    ]
  for atrs in lista_atrs:
    usr = cria(atrs)
    assert usr != None and type(usr) is usuario.ObjUsuario
  return

# FUNÇÕES INTERNAS

def def_obj(obj, id_usuario, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjUsuario} com
  identificador {id_usuario} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {ObjUsuario}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0,"usuario_IMP.def_obj(" + str(obj) + ", " + id_usuario + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    # Converte atributos para formato na memória.
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    if diags: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
    if len(atrs_mem) != len(colunas):
      erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(colunas)))
    obj = usuario.ObjUsuario(id_usuario, atrs_mem)
    
  else:
    assert obj.id_usuario == id_usuario
    # Converte atributos para formato na memória.
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    if diags: mostra(2,"modificando objeto, mods_mem = " + str(mods_mem))
    if len(mods_mem) > len(colunas):
      erro_prog("numero de atributos a alterar = " + str(len(mods_mem)) + " excessivo")
    
    # O campo 'CPF' não pode ser alterado.
    if 'CPF' in mods_mem:
      CPF_velho = obj.atrs['CPF']
      CPF_novo = mods_mem['CPF']
      if CPF_novo != CPF_velho:
        erro_prog("CPF não pode ser alterado")
    
    # Modifica:
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if val != None and val_velho != None and (not type(val_velho) is type(val)):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      obj.atrs[chave] = val
  if diags: mostra(2,"obj = " + str(obj))
  return obj

def busca_por_campo_unico(chave, val):
  """Função interna: procura usuário cujo atributo {chave}
  tem valor {val}, supondo que ele é único. Se
  encontrar, devolve o identificador desse usuário,
  senão devolve {None}"""
  global cache, nome_tb, letra_tb, colunas, diags
  res = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, chave, val)
  if res == None:
    # Não achou ninguém?
    return None
  elif (type(res) is list or type(res) is tuple) and len(res) == 0:
    # Não achou ninguém:
    return None
  elif type(res) is str:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    if len(res) != 1:
      erro_prog("campo '" + chave + "' val = '" + str(val) + "' duplicado - res = " + str(res))
    id_usuario = res[0];
    return id_usuario

def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return
