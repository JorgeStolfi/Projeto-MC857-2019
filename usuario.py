# Este módulo define a classe de objetos {ObjUsuario}, que
# representa um usuário (cliente) da loja virtual.

# Implementação deste módulo e da classe {ObjUsuario}:
import usuario_IMP; from usuario_IMP import ObjUsuario_IMP

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de usuários na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {base_sql.conecta}. 
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  usuario_IMP.inicializa(limpa)

class ObjUsuario(ObjUsuario_IMP):
  """Um objeto desta classe representa um usuário da loja e
  armazena seus atributos.  Por enquanto, são:

    'nome'      nome completo do usuário.
    'senha'     senha do usuário.
    'email'     endereço de email
    'CPF'       número CPF ("{XXX}.{YYY}.{ZZZ}-{KK}")
    'endereco'  endereço completo, em 3 linhas (menos CEP).
    'CEP'       código de endereçamento postal completo ("{NNNNN}-{LLL}").
    'telefone'  telefone completo com DDI e DDD ("+{XX}({YY}){MMMM}-{NNNN}").
    'documento' número do documento de identidade (RG, passaporte, etc.).
    
  O 'documento' é opcional.  Os demais atributos são obrigatórios.
    
  Outros atributos (nascimento, preferências, etc.) poderão ser acrescentados no futuro.

  Além desses atributos, cada usuário tem um identificador, uma string da forma
  "U-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela (vide abaixo)
  formatado em 8 algarismos.
  
  Os campos 'CPF' e 'email' de todos os usuários
  devem ser distintos.  Todos os campos podem ser alterados,
  exceto o índice (e identificador).
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada usuário do sistema -- cliente ou funcionário, ativo ou bloqueado
  -- é representado por uma linha na tabela "usuarios" da base SQL em
  disco. Apenas algumas dessas linhas são representadas também na memória por objetos
  da classe {ObjUsuario}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do usuário."""

def cria(atrs):
  """Cria um novo objeto da classe {ObjUsuario}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de usuários da base de dados.
  Atribui um identificador único ao usuário, derivado do seu índice na tabela.
  
  Não pode haver outro usuário com mesmo email ou CPF.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return usuario_IMP.cria(atrs)

def muda_atributos(usr, mods):
  """Modifica alguns atributos do objeto {usr} da classe {ObjUsuario},
  registrando as alterações na base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do usuário (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.

  Se o 'email' ou 'CPF' for alterado, não pode existir nenum outro 
  usuário na tabela com mesmo email.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  usuario_IMP.muda_atributos(usr, mods)

def obtem_identificador(usr):
  """Devolve o identificador 'U-{NNNNNNNN}' do usuario."""
  return usuario_IMP.obtem_identificador(usr)

def obtem_indice(usr):
  """Devolve o índice inteiro do usuario na tabela de usuários."""
  return usuario_IMP.obtem_indice(usr)

def obtem_atributos(usr):
  """Retorna um dicionário Python que é uma cópia dos atributos do usuário,
  exceto identificador."""
  return usuario_IMP.obtem_atributos(usr)

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

def busca_por_palavra(pal):
  """Devolve uma lista com todos os identificadores "U-{NNNNNNNN}"
  dos produtos que contém a palavra {pal} nos seus 
  campos 'nome'.  Se não houver nenhum item 
  satisfazendo a busca, devolve uma lista vazia."""
  return usuario_IMP.busca_por_palavra(pal)


# UTILIDADES


def confere_e_elimina_conf_senha(args):
  """Se o campo 'senha' está em {args}, exige o campo
  'conf_senha' com mesmo valor.  Em caso de erro, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro.  Senão, remove o campo 'conf_senha' de {atrs}
  e retorna sem resultado.
  
  Esta função é útil para processar comandos de 
  cadastrar novo usuário ou alterar dados de usuário."""
  return usuario_IMP.confere_e_elimina_conf_senha(args)

# FUNÇÕES PARA DEPURAÇÃO

def cria_testes():
  """Limpa a tabela de usuários com {inicializa(True)}, e cria pelo menos três usuários
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.""" 
  usuario_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  usuario_IMP.diagnosticos(val)
