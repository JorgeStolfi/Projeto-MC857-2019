# Este módulo define a classe de objetos {ObjSessao}, que
# representa uma sessão de 'login' de um cliente da loja virtual.
# 
# Nas funções abaixo, {usr} é um objeto da classe {ObjUsuario}
# que representa o cliente.

# Interfaces importadas por esta interface:
import usuario; from usuario import ObjUsuario

# Implementaçao deste módulo:
import sessao_IMP; from sessao_IMP import ObjSessao_IMP

def inicializa():
  """Inicializa o modulo, criando a tabela de sessões na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor.
  Não retorna nenhum valor."""
  usuario_IMP.inicializa()

class ObjSessao(ObjSessao_IMP):
  """Um objeto desta classe representa uma sessao de acesso ao
  servidor.  Os atributos deste objeto, por enquanto, são:
  
    'usr' {ObjUsuario} - o usuário que fez login na sessão.
    'aberta' {bool} - estado da sessao.
    
  Outros atributos (data, cookie, IP, etc.) poderão ser acrescentados no futuro.
  
  Cada sessao pertence a um unico usuario, mas cada
  usuário pode ter várias sessoes abertas ao mesmo tempo. A sessao é criada
  e "aberta" quando o usuario faz login, e e "fechada" no logout.

   Cada sessão do sistema -- aberta ou fechada -- é representada por uma linha na tabela "sessoes" da base SQL em
  disco. Apenas algumas dessas linhas são representadas também na memória por objetos
  da classe {ObjSessao}. 
  
  Cada linha da tabela tem um índice inteiro (chave primária) distinto, que é atribuído
  quando a linha é criada.  Neste sistema, esse índice é manipulado na forma de 
  um identificador de sessão, uma string da forma "S-{NNNNNNNN}"
  onde {NNNNNNNN} é o índice formatado em 8 algarismos.
  
  Além disso, cada linha tem uma coluna da tabela (um campo) para cada um dos
  atributos da sessão (menos o identificador), como definido por {sessão.campos()}.
  """
# Construtor da classe:

def cria(usr):
  """Cria um novo objeto da classe {ObjSessao}, associada ao usuário {usr},
  inicialmente aberta.  Também acrescenta a sessão à base de dados.  Em caso de
  sucesso, retorna o objeto.
  Atribui um identificador único à sessão, derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return sessao_IMP.cria(usr)

def obtem_identificador(sessao):
	"""Devolve o identificador 'S-{NNNNNNNN}' da sessão."""
    return sessao_IMP.obtem_identificador(sessao)

def obtem_usuario(sessao):
    """Retorna o objeto da classe {ObjUsuario} correspondente ao usuario que
    fez login na sessao.  Equivale a {self.obtem_atributos()['usr']}. """
    return sessao_IMP.obtem_usuario(sessao)

def busca_por_identificador(id_sessao):
    """Devolve um dicionário {atrs} com o conteúdo da linha 
    de identificador {id_sessao} da tabela de sessões da base {bas}.
    O dicionário não inclui o campo 'id_sessao'."""
    return sessao_IMP.busca_por_identificador(id_sessao)

def aberta(sessao):
    """Retorna o estado da sessão: {True} se a sessao ainda esta aberta, 
    {False} se o usuário deu logout.  Equivale a {self.obtem_atributos()['aberta']}."""
    return sessao_IMP.aberta(sessao)

def obtem_atributos(sessao):
    """Retorna um dicionário Python que é uma cópia dos atributos da sessão,
    exceto identificador."""
    return sessao_IMP.obtem_atributos(sessao)
    
def muda_atributos(sessao, alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos da sessão (exceto o identificador), e troca os 
    valores desses atributos pelos valores correspondentes em {alts}.  
    Também altera esses campos na base de dados.
    """
    sessao_IMP.muda_atributos(sessao, alts)
    
def logout(sessao):
    """Registra o logout do usuário na sessão, mudando o atributo 'aberta'
    permanentemente para {False}. Também altera esse campo na base de dados.
    Em caso de sucesso, retorna o próprio objeto."""
    return sessao_IMP.logout(sessao)
    
def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjSessao}, menos o identificador.  O resultado é adequado 
  para o parâmetro {cols} das funções do módulo {tabela_generica}."""
  return sessao_IMP.campos()

