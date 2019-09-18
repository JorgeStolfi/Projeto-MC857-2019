# Implementação do módulo {usuario} e da classe {ObjUsuario}.

import usuario

import tabela_generica
import conversao_sql
import identificador
import tabelas
import sys # Para diagnóstico.

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
    ( 'nome',     type("foo"), 'TEXT', False,   1,  60  ), # Nome completo.
    ( 'senha',    type("foo"), 'TEXT', False,   8,  24  ), # Senha de login.
    ( 'email',    type("foo"), 'TEXT', False,   6,  60  ), # Endereço de email
    ( 'CPF',      type("foo"), 'TEXT', False,  14,  14  ), # Número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    ( 'RG',       type("foo"), 'TEXT', False,   8,  15  ), # Número RG ("[0-9]{8-15}")
    ( 'endereco', type("foo"), 'TEXT', False,  30, 180  ), # Endereço completo, em 3 linhas (menos CEP).
    ( 'CEP',      type("foo"), 'TEXT', False,   9,   9  ), # Código de endereçamento postal completo ("{NNNNN}-{LLL}").
    ( 'telefone', type("foo"), 'TEXT', False,  15,  20  ), # Telefone completo com DDI e DDD ("+{XXX}({YYY}){MMMMM}-{NNNN}").
  )
  # Descrição das colunas da tabela na base de dados.

# Definição interna da classe {ObjUsuario}:

class ObjUsuario_IMP:

  def __init__(self, id_usuario, atrs):
    global cache, nome_tb, letra_tb, colunas
    self.id_usuario = id_usuario
    self.atrs = atrs.copy()

# Implementação das funções:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs):
  global cache, nome_tb, letra_tb, colunas
  sys.stderr.write("usuario_IMP.cria(" + str(atrs) + ") ...\n")

  # Verifica unicidade de CPF:
  for chave in ('CPF', 'email'):
    # Exige atributo {chave} único:
    if chave not in atrs:
      sys.stderr.write("usuario_IMP.cria: ** erro: falta atributo '" + chave + "'\n")
      assert False
    else:
      val = atrs[chave]
      if chave == 'CPF':
        id_bus = busca_por_CPF(val)
      elif chave == 'email':
        id_bus = busca_por_email(val)
      if id_bus != None:
        sys.stderr.write("usuario_IMP.cria: ** erro: atributo '" + chave + "' já existe: " + id_bus + "\n");
        assert False

  # Converte atibutos para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, tabelas.obj_para_indice)
  # Insere na base de dados e obtém o índice na mesma:
  usr = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, mods_SQL)
  if not type(usr) is usuario.ObjUsuario:
    sys.stderr.write("usuario_IMP.cria: ** erro: tipo de objeto errado" + str(usr) + "\n");
    assert False
  return usr

def obtem_identificador(usr):
  global cache, nome_tb, letra_tb, colunas
  return usr.id_usuario

def obtem_indice(usr):
  global cache, nome_tb, letra_tb, colunas
  return identificador.para_indice(letra_tb, usr.id_usuario)

def obtem_atributos(usr):
  global cache, nome_tb, letra_tb, colunas
  return usr.atrs.copy()

def muda_atributos(usr, mods):
  global cache, nome_tb, letra_tb, colunas
  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, tabelas.obj_para_indice)
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, usr.id_usuario, mods_SQL)
  if res != usr:
    sys.stderr.write("usuario_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def busca_por_identificador(id_usuario):
  global cache, nome_tb, letra_tb, colunas
  usr = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_usuario)
  return usr

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas
  usr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return usr

def busca_por_email(em):
  global cache, nome_tb, letra_tb, colunas
  return busca_por_campo_unico('email', em)

def busca_por_CPF(CPF):
  global cache, nome_tb, letra_tb, colunas
  return busca_por_campo_unico('CPF', CPF)

def busca_por_RG(RG):
  global cache, nome_tb, letra_tb, colunas
  return busca_por_campo_unico('RG', RG)

def campos():
  global cache, nome_tb, letra_tb, colunas
  return colunas

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
  global cache, nome_tb, letra_tb, colunas
  sys.stderr.write("usuario_IMP.def_obj(" + str(obj) + ", " + id_usuario + ", " + str(atrs_SQL) + ") ...\n")
  if obj == None:
    # Converte atributos para formato na memória.
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    sys.stderr.write("  criando objeto, atrs_mem = " + str(atrs_mem) + "\n")
    obj = usuario.ObjUsuario(id_usuario, atrs_mem)
  else:
    assert obj.id_usuario == id_usuario
    # Converte atributos para formato na memória.
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, tabelas.obj_para_indice)
    sys.stderr.write("  modificando objeto, mods_mem = " + str(mods_mem) + "\n")
    if len(mods_mem) > len(obj.atrs):
      sys.stderr.write("usuario_IMP.def_obj:  **erro: numero excessivo de atributos a alterar\n")
      assert False
    # O campo 'CPF' não pode ser alterado.
    if 'CPF' in mods_mem:
      CPF_velho = obj.atrs['CPF']
      CPF_novo = mods_mem['CPF']
      if CPF_novo != CPF_velho:
        sys.stderr.write("usuario_IMP.def_obj:  **erro: CPF não pode ser alterado\n")
        assert False
    # Modifica:
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        sys.stderr.write("usuario_IMP.def_obj:  **erro: chave '" + chave + "' inválida\n")
        assert False
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        sys.stderr.write("usuario_IMP.def_obj:  *erro: tipo do campo '" + chave + "' incorreto\n")
        assert False
      obj.atrs[chave] = val
  sys.stderr.write("  obj = " + str(obj) + "\n")
  return obj

def busca_por_campo_unico(chave, val):
  """Função interna: procura usuário cujo atributo {chave}
  tem valor {val}, supondo que ele é único. Se
  encontrar, devolve o identificador desse usuário,
  senão devolve {None}"""
  global cache, nome_tb, letra_tb, colunas
  res = tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, chave, val)
  if res == None:
    # Não achou ninguém?
    return None
  elif (type(res) is list or type(res) is tuple) and len(res) == 0:
    # Não achou ninguém:
    return None
  elif type(res) is str:
    # Deu erro:
    sys.stderr.write(res + "\n")
    assert False
  else:
    if len(res) != 1:
      sys.stderr.write("usuario_IMP.busca_por_campo_unico: **erro: campo '" + chave + "' val = '" + str(val) + "' duplicado\n")
      sys.stderr.write(" res = " + str(res) + "\n")
      assert False
    id_usuario = res[0];
    return id_usuario
