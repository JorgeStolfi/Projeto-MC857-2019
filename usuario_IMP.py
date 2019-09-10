# Implementação do módulo {usuario} e da classe {ObjUsuario}.

# Para diagnóstico:
import sys
import tabela_generica

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "usuarios"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjUsuario} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

colunas = \
  (
    ( 'nome',     type("foo"), 'TEXT NOT NULL',  1,  60  ), # nome completo do usuário.
    ( 'senha',    type("foo"), 'TEXT NOT NULL',  8,  24  ), # senha do usuário.
    ( 'email',    type("foo"), 'TEXT NOT NULL',  6,  60  ), # endereço de email
    ( 'CPF',      type("foo"), 'TEXT NOT NULL', 14,  14  ), # número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    ( 'endereco', type("foo"), 'TEXT NOT NULL', 30, 180  ), # endereço completo, em 3 linhas (menos CEP).
    ( 'CEP',      type("foo"), 'TEXT NOT NULL',  9,   9  ), # código de endereçamento postal completo ("{NNNNN}-{LLL}").
    ( 'telefone', type("foo"), 'TEXT NOT NULL', 15,  20  ), # telefone completo com DDI e DDD ("+{XXX}({YYY}){MMMMM}-{NNNN}").
  )
  # Descrição das colunas da tabela na base de dados.

def inicializa():
  global cache, nome_tb, colunas
  # Cria a tabela:
  res = tabela_generica.cria_tabela(nome_tb, colunas)
  if res != None:
    sys.stderr.write("usuario_IMP.inicializa: **erro " + str(res) + "\n")
    assert False

class ObjUsuario_IMP:

  def __init__(self, id_usuario, atrs):
    global cache, nome_tb, colunas
    self.identificador = id_usuario
    self.atributos = atrs.copy()

def obtem_identificador(usr):
  global cache, nome_tb, colunas
  return usr.identificador

def obtem_atributos(usr):
  global cache, nome_tb, colunas
  return usr.atributos.copy()

def muda_atributos(usr, alts):
  global cache, nome_tb, colunas
  res = tabela_generica.atualiza(nome_tb, cache, "U", colunas, cria_obj, muda_obj, usr.identificador, alts)
  if res != usr:
    sys.stderr.write("usuario_IMP.muda_atributos: **erro " + str(res) + "\n")
    assert False
  return

def cria(atrs):
  global cache, nome_tb, colunas
  sys.stderr.write("usuario_IMP.cria(" + str(atrs) + ") ...\n")
  # Atributo 'CPF' não pode ser alterado:
  # Verifica unicidade de CPF e email:
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

  # Insere na base de dados e obtém o índice na mesma:
  usr = tabela_generica.acrescenta(nome_tb, cache, "U", colunas, cria_obj, atrs)
  if not type(usr) is ObjUsuario_IMP:
    sys.stderr.write("usuario_IMP.cria: ** erro: " + str(usr) + "\n");
    assert False
  return usr

def busca_por_identificador(id_usuario):
  global cache, nome_tb, colunas
  usr = tabela_generica.busca_por_identificador(nome_tb, cache, "U", colunas, cria_obj, id_usuario)
  return usr

def busca_por_email(em):
  global cache, nome_tb, colunas
  return busca_por_campo_unico('email', em)

def busca_por_CPF(CPF):
  global cache, nome_tb, colunas
  return busca_por_campo_unico('CPF', CPF)

def campos():
  global cache, nome_tb, colunas
  return colunas

# FUNÇÕES INTERNAS

def cria_obj(id_usuario, atrs):
  """Cria um novo objeto da classe {ObjUsuario} com dado identificador e atributos.
  Não coloca na base de dados."""
  global cache, nome_tb, colunas
  sys.stderr.write("usuario_IMP.cria_obj(" + id_usuario + ", " + str(atrs) + ") ...\n")
  usr = ObjUsuario_IMP(id_usuario, atrs)
  sys.stderr.write("  usr = " + str(usr) + "\n")
  return usr
     
def muda_obj(usr, alts):
  """Modifica os atributos do objeto {obj} da classe {ObjUsuario} segundo 
  consta do dicionário {alts}. Não modifica a linha correspondente da 
  base de dados."""
  global cache, nome_tb, colunas
  sys.stderr.write("usuario_IMP.muda_obj\n")
  sys.stderr.write("  usr antes = " + str(usr) + "\n")
  sys.stderr.write("  alts = " + str(alts) + "\n")
  
  if 'CPF' in alts:
    CPF_velho = usr.atributos['CPF']
    CPF_novo = alts['CPF']
    if CPF_novo != CPF_velho:
      return "**erro: CPF não pode ser alterado"

  if len(alts) > len(usr.atributos):
    return "**erro: numero excessivo de atributos a alterar"
  
  for chave, val in alts.items():
    if not chave in usr.atributos:
      return "**erro: chave '" + chave + "' inválida"
    # !!! Deveria testar se o valor {val} tem o tipo correto.
    # val_velho = usr.atributos[chave]
    # if not type(val_velho) is type(val):
    #   return "**erro: tipo do campo '" + chave + "' incorreto"
    usr.atributos[chave] = val
  
  sys.stderr.write("  usr = " + str(usr) + "\n")
  return usr

def busca_por_campo_unico(chave, val):
  """Função interna: procura usuário cujo atributo {chave}
  tem valor {val}, supondo que ele é único. Se
  encontrar, devolve o identificador desse usuário,
  senão devolve {None}"""
  global cache, nome_tb, colunas
  res = tabela_generica.busca_por_campo(nome_tb, cache, "U", colunas, chave, val)
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
      assert False
    id_usuario = res[0];
    return id_usuario
