# Este módulo define a classe de objetos {ObjSessao}, que
# representa uma sessão de 'login' de um cliente da loja virtual.
# 
# Nas funções abaixo, {usr} é um objeto da classe {ObjUsuario}
# que representa o cliente.

# Interfaces importadas por esta interface:
import usuario

# Implementaçao deste módulo:
import sessao_IMP; from sessao_IMP import ObjSessao_IMP

# !!! Acrescentar mais um atributo 'carrinho' que é um objeto da classe {ObjCompra}. !!!
# !!! Acrescentar o parâmetro {carrinho} à função {sessao.cria(usr,cookie)}.  Procurar todas as chamadas e consertar. !!!
# !!! Acrescentar a função {sessao.obtem_carrinho(ses)} !!!
# !!! No módulo de teste, passar {None} como carrinho !!!

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de sessões na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor, 
  depois de chamar {base_sql.conecta}. Não retorna nenhum valor.  
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  sessao_IMP.inicializa(limpa)

class ObjSessao(ObjSessao_IMP):
  """Um objeto desta classe representa uma sessao de acesso ao
  servidor.  Os atributos deste objeto, por enquanto, são:
  
    'usr' {ObjUsuario} - o usuário que fez login na sessão.
    'abrt' {bool} - estado da sessao.
    
  Outros atributos (data, cookie, IP, etc.) poderão ser acrescentados no futuro.
  
  Cada sessao pertence a um unico usuario, mas cada
  usuário pode ter várias sessoes abertas ao mesmo tempo. A sessao é criada
  e "aberta" quando o usuario faz login, e e "fechada" no logout.

  Cada sessão do sistema -- aberta ou fechada -- é representada por uma
  linha na tabela "sessoes" da base SQL em disco. Apenas algumas dessas
  linhas são representadas também na memória por objetos da classe
  {ObjSessao}.
  
  Cada linha da tabela tem um índice inteiro (chave primária) distinto, que é atribuído
  quando a linha é criada.  Neste sistema, esse índice é manipulado na forma de 
  um identificador de sessão, uma string da forma "S-{NNNNNNNN}"
  onde {NNNNNNNN} é o índice formatado em 8 algarismos.
  
  Além disso, cada linha tem uma coluna da tabela (um campo) para cada um dos
  atributos da sessão (menos o identificador), como definido por {sessão.campos()}."""
 
def cria(usr, cookie):
  """Cria um novo objeto da classe {ObjSessao}, associada ao usuário {usr},
  inicialmente aberta, com o cookie inicial {cookie}.  Também acrescenta a sessão à base de dados.  Em caso de
  sucesso, retorna o objeto.
  Atribui um identificador único à sessão, derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return sessao_IMP.cria(usr, cookie)

def obtem_identificador(ses):
  """Devolve o identificador 'S-{NNNNNNNN}' da sessão {ses}."""
  return sessao_IMP.obtem_identificador(ses)

def obtem_indice(ses):
  """Devolve o índice inteiro da sessão {ses} na tabela de sessões da base de dados."""
  return sessao_IMP.obtem_indice(ses)

def obtem_cookie(ses):
  """Devolve o cookie da sessão {ses} """
  return sessao_IMP.obtem_cookie(ses)

def obtem_usuario(ses):
  """Retorna o objeto da classe {ObjUsuario} correspondente ao usuario que
  fez login na sessao {ses}.  Equivale a {sessao.obtem_atributos(ses)['usr']}. """
  return sessao_IMP.obtem_usuario(ses)

def aberta(ses):
  """Retorna o estado da sessão {ses}: {True} se a sessao ainda esta aberta, 
  {False} se o usuário deu logout.  Equivale a {sessao.obtem_atributos(ses)['abrt']}."""
  return sessao_IMP.aberta(ses)

def obtem_atributos(ses):
  """Retorna um dicionário Python que é uma cópia dos atributos da sessão {ses},
  exceto identificador."""
  return sessao_IMP.obtem_atributos(ses)

def muda_atributos(ses, mods):
  """Recebe um dicionário Python {mods} cujas chaves são um subconjunto
  dos nomes de atributos da sessão (exceto o identificador). Troca os 
  valores desses atributos no objeto {ses} da classe {ObjSessao}
  pelos valores correspondentes em {mods}.  Também altera esses 
  campos na base de dados. """
  sessao_IMP.muda_atributos(ses, mods)

def fecha(ses):
  """Registra o logout do usuário na sessão {ses}, mudando o atributo 'abrt'
  permanentemente para {False}. Também altera esse campo na base de dados.
  Em caso de sucesso, retorna o próprio objeto."""
  return sessao_IMP.fecha(ses)

def busca_por_identificador(id_sessao):
  """Localiza uma sessao com identificador {id_sessao} (uma string da forma
  "S-{NNNNNNNN}"), e devolve a mesma na forma de um objeto da classe {ObjSessao}.
  Se tal sessão não existe, devolve {None}."""
  return sessao_IMP.busca_por_identificador(id_sessao)

def busca_por_indice(ind):
  """Localiza uma sessao com indice inteiro {ind} na tabela de sessões.
  Se tal sessão não existe, devolve {None}."""
  return sessao_IMP.busca_por_indice(ind)

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjSessao}, menos o identificador.  O resultado é adequado 
  para o parâmetro {cols} das funções do módulo {tabela_generica}."""
  return sessao_IMP.campos()

def cria_testes():
  """Limpa a tabela de sessoes com {inicializa(True)}, e cria três sessões
  para fins de teste, incluindo-as na tabela.  As sessões estarão
  inicialmente abertas.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.Supõe que a tabela de usuários 
  já foi inicializada e tem pelo menos três entradas.""" 
  sessao_IMP.cria_testes()
