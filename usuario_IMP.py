# Implementação do módulo {usuario} e da classe {ObjUsuario}.

import usuario

import tabela_generica
import conversao_sql
import identificador
import tabelas
import valida_campo; from valida_campo import ErroAtrib

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
    ( 'nome',          type("foo"), 'TEXT',    False ), # Nome completo.
    ( 'senha',         type("foo"), 'TEXT',    False ), # Senha de login.
    ( 'email',         type("foo"), 'TEXT',    False ), # Endereço de email
    ( 'CPF',           type("foo"), 'TEXT',    False ), # Número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    ( 'endereco',      type("foo"), 'TEXT',    False ), # Endereço completo, em 3 linhas (menos CEP).
    ( 'CEP',           type("foo"), 'TEXT',    False ), # Código de endereçamento postal completo ("{NNNNN}-{LLL}").
    ( 'telefone',      type("foo"), 'TEXT',    False ), # Telefone completo com DDI e DDD ("+{XXX}({YYY}){MMMMM}-{NNNN}").
    ( 'documento',     type("foo"), 'TEXT',    True  ), # Número do documento de identidade (RG, pasaporte, etc.)
    ( 'administrador', type(False), 'INTEGER', False ), # Define se o usuário é administrador (1=administrador)
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
  
  # Valida os atributos:
  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  # Converte atibutos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, False, tabelas.obj_para_indice)
  # Insere na base de dados e obtém o índice na mesma:
  usr = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  assert type(usr) is usuario.ObjUsuario
  return usr

def muda_atributos(usr, mods):
  global cache, nome_tb, letra_tb, colunas, diags

  # Valida os atributos:
  erros = valida_atributos(usr, mods)
  if len(erros) != 0: raise ErroAtrib(erros)
  
  # Converte valores de formato memória para formato SQL.
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, True, tabelas.obj_para_indice)
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, usr.id_usuario, mods_SQL)
  assert res == usr
  return

def obtem_identificador(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return usr.id_usuario

def obtem_indice(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return identificador.para_indice(letra_tb, usr.id_usuario)

def obtem_atributos(usr):
  global cache, nome_tb, letra_tb, colunas, diags
  return usr.atrs.copy()

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

def busca_por_palavra(pal):
  chaves = ('nome',)
  valores = (pal,)
  busca_com_and = ' AND ' in pal
  
  if busca_com_and:
    valores = pal.split(' AND ')
    valores = tuple(valores)
 
  usuarios =  tabela_generica.busca_por_semelhanca(nome_tb, letra_tb, colunas, chaves, valores)
  return usuarios

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


def confere_e_elimina_conf_senha(args):

  senha = (args['senha'] if 'senha' in args else None)
  if senha != None and senha != '':
    # Senha está sendo alterada/definida.  Precisa confirmar senha:
    if 'conf_senha' not in args:
      raise ErroAtrib([ "campo 'Confirmar Senha' 'e obrigatório", ])
    else:
      if senha != args['conf_senha']:
        raise ErroAtrib([ "senhas não batem", ])
   
  # Remove o campo 'conf_senha', não mais necessários
  if 'conf_senha' in args: del args['conf_senha']
  return


# FUNÇÕES INTERNAS

def valida_atributos(usr, atrs):
  """Faz validação nos atributos {atrs}. Devolve uma lista 
  de strings com descrições dos erros encontrados.
  
  Se {usr} é {None}, supõe que um usuário está sendo criado.
  Nesse caso exige que todos os atributos do usuário
  estejam presentes, possivelmente com valor {None} ou 
  cadeia vazia.
  
  Se {usr} não é {None}, supõe que {atrs} sao alterações a aplicar nesse
  usuário. 
  
  Em qualquer caso, não pode haver na base nenhum usuário
  com mesmo email ou CPF."""
  global cache, nome_tb, letra_tb, colunas, diags
  
  erros = [].copy();
  
  # Validade dos campos fornecidos:
  if 'nome' in atrs:
    erros += valida_campo.nome_de_usuario('nome', atrs['nome'], False)
  if 'email' in atrs:
    erros += valida_campo.email('Email', atrs['email'], False)
  if 'CPF' in atrs:
    erros += valida_campo.CPF('CPF', atrs['CPF'], False)
  if 'CEP' in atrs:
    erros += valida_campo.CEP('CEP', atrs['CEP'], False)
  if 'telefone' in atrs:
    erros += valida_campo.telefone('Telefone', atrs['telefone'], False)
  if 'endereco' in atrs:
    erros += valida_campo.endereco('Endereco', atrs['endereco'], False)
  if 'endereco_1' in atrs:
    erros += valida_campo.linha_de_endereco('Endereco - Linha 1', atrs['endereco_1'], False)
  if 'endereco_2' in atrs:
    erros += valida_campo.linha_de_endereco('Endereco - Linha 2', atrs['endereco_2'], False)
  if 'cidade_UF' in atrs:
    erros += valida_campo.cidade_UF('Cidade, UF', atrs['cidade_UF'], False)
  if 'administrador' in atrs:
    erros += valida_campo.cidade_UF('Administrador', atrs['administrador'], False)
  if 'documento' in atrs:
    erros += valida_campo.cidade_UF('Documento', atrs['documento'], True)
     
  # Pega a senha, se tiver:
  if 'senha' in atrs:
    senha = atrs['senha']
    if senha == '': senha = None
  else:
    senha = None
  
  # Valida a senha:
  erros += valida_campo.senha('Senha', senha, (usr != None))

  if 'endereco_1' in atrs:
    # Cozinhada: Define o campo 'endereco' formatado como 'Linha_1\nLinha_2\nCidade, UF'
    atrs['endereco'] = atrs['endereco_1'] + '\n' + atrs['endereco_2'] + '\n' + atrs['cidade_UF']
    del atrs['endereco_1']
    del atrs['endereco_2']
    del atrs['cidade_UF']
    
  # Acrescenta 'administrador' se não está presente, converte para booleano se está:
  if 'administrador' not in atrs:
    atrs['administrador'] = False
  elif type(atrs['administrador']) is not bool:
    atrs['administrador'] = True
      
  # Verifica completude:
  nargs = 0 # Número de campos em {atrs} reconhecidos.
  for chave, tipo_mem, tipo_sql, nulo_ok in colunas:
    if chave in atrs:
      nargs += 1
    elif usr == None:
      erros.append("campo '" + chave + "' é obrigatório")

  if nargs < len(atrs):
    # Não deveria ocorrer:
    erro_prog("campos espúrios em {atrs} = " + str(atrs) + "")
    
  # Verifica unicidade de email e CPF:
  for chave in ('CPF', 'email'):
    # Exige atributo {chave} único:
    if chave in atrs:
      val = atrs[chave]
      if chave == 'CPF':
        id_bus = busca_por_CPF(val)
      elif chave == 'email':
        id_bus = busca_por_email(val)
      # sys.stderr.write("\n\n  valida_atributos: chave = '" + chave + "' val = '" + str(val) + "' id_bus = " + str(id_bus) + "\n\n")
      if (id_bus != None) and ((usr == None) or (id_bus != usr.id_usuario)):
        erros.append("usuário com '" + chave + "' = '" + val + "' já existe: " + id_bus)

  return erros

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
    obj = cria_obj(id_usuario, atrs_SQL)
  else:
    assert obj.id_usuario == id_usuario
    modifica_obj(obj, atrs_SQL)
  if diags: mostra(2,"obj = " + str(obj))
  return obj
    
def cria_obj(id_usuario, atrs_SQL):
  """Cria um novo objeto da classe {ObjUsuario} com
  identificador {id_usuario} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados.
  
  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte atributos para formato na memória.  Todos devem estar presentes:
  atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.obj_para_indice)
  if diags: mostra(2,"criando objeto, atrs_mem = " + str(atrs_mem))
  assert type(atrs_mem) is dict
  if len(atrs_mem) != len(colunas):
    erro_prog("numero de atributos = " + str(len(atrs_mem)) + " devia ser " + str(len(colunas)))

  # Paranóia: verifica de novo a unicidade de CPF e email:
  for chave in ('CPF', 'email'):
    if chave not in atrs_mem:
      erro_prog("falta atributo '" + chave + "'")
    else:
      val = atrs_mem[chave]
      id_bus = busca_por_campo_unico(chave, val);
      if id_bus != None:
        erro_prog("usuário com '" + chave + "' = '" + val + "' já existe: " + id_usuario + " " + id_bus)
    
  obj = usuario.ObjUsuario(id_usuario, atrs_mem)
  return obj
  
def modifica_obj(obj, atrs_SQL):
  """O parâmetro {obj} deve ser um objeto da classe {ObjUsuario}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.

  Os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags

  # Converte atributos para formato na memória. Pode ser subconjunto:
  mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.obj_para_indice)
  if diags: mostra(2,"modificando objeto, mods_mem = " + str(mods_mem))
  assert type(mods_mem) is dict
  if len(mods_mem) > len(colunas):
    erro_prog("numero de atributos a alterar = " + str(len(mods_mem)) + " excessivo")

  # Paranóia: verifica de novo a unicidade de CPF e email:
  for chave in ('CPF', 'email'):
    if chave in mods_mem:
      val = mods_mem[chave]
      id_bus = busca_por_campo_unico(chave, val);
      if id_bus != None and id_bus != obj.id_usuario:
        erro_prog("usuário com '" + chave + "' = '" + val + "' já existe: " + id_usuario + " " + id_bus)

  # Modifica os atributos:
  for chave, val in mods_mem.items():
    if not chave in obj.atrs:
      erro_prog("chave '" + chave + "' inválida")
    val_velho = obj.atrs[chave]
    if val != None and val_velho != None and (not type(val_velho) is type(val)):
      erro_prog("tipo do campo '" + chave + "' incorreto")
    obj.atrs[chave] = val
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
