# Este módulo define a classe de objetos {ObjUsuario}, que
# representa um usuário (cliente) da loja virtual.

# Implementação deste módulo e da classe {ObjUsuario}:
import usuario_IMP; from usuario_IMP import ObjUsuario_IMP

def inicializa():
  """Inicializa o modulo, criando a tabela de usuários na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor."""
  usuario_IMP.inicializa()

class ObjUsuario(ObjUsuario_IMP):
  """Um objeto desta classe representa um usuário da loja e
  armazena seus atributos.  Por enquanto, são:
  
    'nome'     nome completo do usuário.
    'senha'    senha do usuário.
    'email'    endereço de email
    'CPF'      número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    'endereco' endereço completo, em 3 linhas (menos CEP).
    'CEP'      código de endereçamento postal completo ("{NNNNN}-{LLL}").
    'telefone' telefone completo com DDI e DDD ("+{XX}({YY}){MMMM}-{NNNN}").
    
  Outros atributos (nascimento, preferências, etc.) poderão ser acrescentados no futuro.
  
  Cada usuário do sistema -- cliente ou funcionário, ativo ou bloqueado
  -- é representado por uma linha na tabela "usuarios" da base SQL em
  disco. Apenas algumas dessas linhas são representadas também na memória por objetos
  da classe {ObjUsuario}. 
  
  Cada linha da tabela tem um índice inteiro (chave primária) distinto, que é atribuído
  quando a linha é criada.  Neste sistema, esse índice é manipulado na forma de 
  um identificador de usuário, uma string da forma "U-{NNNNNNNN}"
  onde {NNNNNNNN} é o índice formatado em 8 algarismos.
  
  Além disso, cada linha tem uma coluna da tabela (um campo) para cada um dos
  atributos do usuário (menos o identificador), como definido por {usuario.campos()}.
  
  Os campos 'CPF' e 'email' de todos os usuários
  devem ser distintos.  Todos os campos podem ser alterados,
  exceto o índice (e identificador) e o CPF."""

def cria(atrs):
  """Cria um novo objeto da classe {ObjUsuario}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de usuários da base de dados.
  Atribui um identificador único ao usuário, derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return usuario_IMP.cria(atrs)

def obtem_identificador(usr):
  """Devolve o identificador 'U-{NNNNNNNN}' do usuario."""
  return usuario_IMP.obtem_identificador(usr)

def obtem_atributos(usr):
  """Retorna um dicionário Python que é uma cópia dos atributos do usuário,
  exceto identificador."""
  return usuario_IMP.obtem_atributos(usr)

def muda_atributos(usr, mods):
  """Modifica alguns atributos do objeto {usr} da classe {ObjUsuario},
  registrando as alterações na base de dados.  

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do usuário (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores 
  correspondentes em {mods}.

  O atributo 'CPF'não pode ser alterado; se o dicionário {mods} incluir o campo 'CPF',
  o valor deve ser o CPF atual. Se o atributo 'email' for alterado,
  não pode existir nenum outro usuário na tabela com mesmo email."""
  usuario_IMP.muda_atributos(usr, mods)

def busca_por_identificador(id_usuario):
  """Localiza um usuario com identificador {id_usuario} (uma string da forma
  "U-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Obj_Usuario}.
  Se tal usuário não existe, devolve {None}."""
  return usuario_IMP.busca_por_identificador(id_usuario)

def busca_por_indice(ind):
  """Mesma que {busca_por_identificador}, mas quer o índice  inteiro {ind} da linha da tabela,
  em vez do identificador do objeto."""
  return usuario_IMP.busca_por_indice(ind)

def busca_por_email(em):
  """Localiza um usuário cujo endereço de email é {em} (um string da forma
  "{nome}@{host}") e devolve o identificador do mesmo (não o objeto);
  ou {None} se não existir tal usuário."""
  return usuario_IMP.busca_por_email(em)

def busca_por_CPF(CPF):
  """Localiza um usuário cujo número CPF é {CPF} (um string no formato
  "{XXX}.{YYY}.{ZZZ}-{KK}") e devolve o identificador do mesmo (não um objeto);
  ou {None} se não existir tal usuário."""
  return usuario_IMP.busca_por_CPF(CPF)

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjUsuario}, menos o identificador.  O resultado é adequado 
  para o parâmetro {cols} das funções do módulo {tabela_generica}."""
  return usuario_IMP.campos()

def limpa_tabela():
  """Apaga todas as linhas da tabela de usuários na base de dados,
  reinicializando o contador de linhas em 0. Não retorna nenhum valor. 
  
  Esta função deve ser chamada apenas uma vez no ínicio da execução do servidor,
  antes de criar, buscar, ou atterar qualquer usuário.  Caso contrário,
  os objetos {ObjUsuario} na memória ficarão inconsistentes com a base."""
  usuario_IMP.limpa_tabela()
