# Este módulo define a classe de objetos {ObjCompra}, que
# representa um pedido de compra (em particular, um carrinho de
# compras).
# 
# Nas funções abaixo, o parâmetro {prod} é um objeto
# da classe {ObjProduto}, e {qt} e um {float} que especifica uma
# quantidade desse produto.

# Interfaces importadas por esta interface:
import usuario
import produto

# Implementaçao deste módulo:
import compra_IMP; from compra_IMP import ObjCompra_IMP

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela "compras" na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor, 
  depois de chamar {base_sql.conecta}. Não retorna nenhum valor.  
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  compra_IMP.inicializa(limpa)

class ObjCompra(ObjCompra_IMP):
  """Um objeto desta classe representa e descreve um pedido de compra
  de um ou mais produtos em diversas quantidades, feito por um
  cliente da loja, que pode estar em várias etapas de execução.
  Em particular, o pedido pode ainda estar sendo construído e alterado
  pelo usuário -- ou seja, pode ser um "carrinho de compras".
  
  Por enquanto, os atributos de um objeto desta classe são:
  
    'cliente' {ObjUsuario} o cliente que fez ou está montando a compra.
    'status'  {str}        o estado do pedido. 
    
  Além disso, cada objeto desta classe possui uma lista de itens. Cada
  item é uma tripla {(prod, qt,preco)} onde {prod} é um
  objeto da classe {ObjProduto}, {qt} é um float que indica a quantidade
  comprada, e {preco} é um float que indica o preço total do item. Os
  produtos na lista são sempre todos distintos.
  
  O atributo 'status' por enquanto, pode ser:
  
   'aberto': O cliente ainda está montando o pedido.
   'pagando':  O cliente fechou o pedido, e a loja está aguardando o pagamento.
   'pago': A loja já recebeu o pagamento e está mandando para despacho.
   'despachado': A loja já colocou o pedido no correio ou transportadora.
   'entregue': O pedido foi entregue ao cliente.
   
  Mais campos e/ou estados poderão ser acrescentados no futuro.
  
  Além desses atributos, cada compra também tem identificador, uma string da forma "C-{NNNNNNNN}"
  onde {NNNNNNNN} é o índice na tabela (vide abaixo) formatado em 8 algarismos.
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada pedido de compra no sistema é representado por uma linha na tabela "compras" 
  da base SQL em disco.  Apenas algumas dessas linhas são representadas também na 
  memória por objetos da classe {ObjCompra}. 
  
  Cada linha da tabela de compras tem um índice inteiro (chave primária)
  distinto, que é atribuído quando a linha é criada.  Além disso, cada
  linha tem uma coluna da tabela (um campo) para cada um dos atributos
  da compra (exceto a lista de itens, que é armazenada em uma tabela 
  separada, e o identificador)."""

def cria(cliente):
  """Cria um novo objeto da classe {ObjCompra} para o usuário {cliente}
  (um objeto da classe {ObjUsuario}), acrescentando-o à tabela de compras da base de dados.
  O status será inicialmente 'aberto'.  Atribui um identificador único à compra,
  derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return compra_IMP.cria(cliente)

def obtem_identificador(cpr):
  """Devolve o identificador 'C-{NNNNNNNN}' da compra {cpr}."""
  return compra_IMP.obtem_identificador(cpr)

def obtem_indice(cpr):
  """Devolve o índice inteiro da compra {cpr} na tabela de compras da base de dados."""
  return compra_IMP.obtem_indice(cpr)

def obtem_atributos(cpr):
  """Retorna um dicionário Python que é uma cópia dos atributos do pedido de
  compra {cpr}, exceto identificador."""
  return compra_IMP.obtem_atributos(cpr)

def obtem_cliente(cpr):
  """Retorna o cliente da compra {cpr}, um objeto da classe {Objusuario}.
  Equivale a {obtem_atributos(cpr)['cliente']}."""
  return compra_IMP.obtem_cliente(cpr)

def obtem_status(cpr):
  """Retorna o status da compra {cpr}. Equivale a {obtem_atributos(cpr)['status']}."""
  return compra_IMP.obtem_status(cpr)

def obtem_itens(cpr):
  """Retorna uma cópia da lista de itens da compra {cpr}."""
  return compra_IMP.obtem_itens(cpr)

def muda_atributos(cpr, mods):
  """Modifica alguns atributos do objeto {cpr} da classe {ObjCompra},
  registrando as alterações na base de dados.  Não pode ser 
  usado para alterar os itens das compras.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos da compra. Os valores atuais desses
  atributos são substituídos pelos valores correspondentes em {mods}."""
  return compra_IMP.muda_atributos(cpr, mods)

def obtem_quantidade(cpr, prod):
  """Retorna a quantidade atual do produto {prod} no pedido de
  compras {cpr}.  Se o produto não está no pedido, devolve zero."""
  return compra_IMP.obtem_quantidade(cpr, prod)

def obtem_preco(cpr, prod):
  """Retorna o preco total do produto {prod} no pedido de
  compras {cpr}.  Se o produto não está no pedido, devolve zero."""
  return compra_IMP.obtem_preco(cpr, prod)

def calcula_total(cpr):
  """ Retorna um float que é o preco total do pedido de compra, ou seja a
  soma dos campos {qt} nos elementos da lista de itens."""
  return compra_IMP.calcula_total(cpr)

def fecha_compra(cpr):
  """Muda o status de uma certa compra de 'aberto' para 'pagando' e salva o novo
  status da compra no banco de dados."""
  return compra_IMP.fecha_compra(cpr)
    
def acrescenta_item(cpr, prod, qt):
  """Acrescenta um novo item no pedido de cpr, consistindo da quantidade 
  {qt} do produto {prod}, acrescentando-o também a tabela de itens de compra. 
  
  Esta função só pode ser usada se a compra ainda estiver aberta. 
  Não retorna nenhum resultado.
  
  Em particular, se o produto já está na lista de itens, soma {qt} à quantidade que
  consta nessa lista. Também recalcula o preço do item, mesmo se {qt} for zero."""
  compra_IMP.acrescenta_item(cpr,prod,qt)

def troca_quantidade(cpr, prod, qt):
  """Modifica a lista de itens da compra {cpr}, trocando a quantidade
  atual do produto {prod} por {qt}. Altera também a linha correspondente
  da tabela de itens de compras. 
  
  Esta função só pode ser usada se a compra ainda estiver aberta. 
  Não retorna nenhum resultado.
  
  Em particular, se {qt} for zero, elimina o produto {prod} da lista. Se o produto {prod} 
  não está na lista, acrescenta-o com quantidade {qt}, e recalcula o preço do item,
  mesmo que o produto já esteja na lista com essa quantidade. """
  compra_IMP.troca_quantidade(cpr, prod, qt)

def elimina_produto(cpr, prod):
  """Modifica a lista de itens da compra, eliminando a entrada com produto {prod}.
  Também elimina a linha correspondente da tabela de itens de compras. 
  
  Esta função só pode ser usada se a compra ainda estiver aberta
  e o produto estiver na lista. Não retorna nenhum resultado."""
  compra_IMP.elimina_produto(cpr, prod)

def busca_por_identificador(id_compra):
  """Localiza uma compra com identificador {id_compra} (uma string da forma
  'C-{NNNNNNNN}'), e devolve a mesma na forma de um objeto da classe {ObjCompra}.
  Se tal compra não existe, devolve {None}."""
  return compra_IMP.busca_por_identificador(id_compra)

def busca_por_indice(ind):
  """Mesma que {busca_por_identificador}, mas quer o índice  inteiro {ind} da linha da tabela,
  em vez do identificador do objeto."""
  return compra_IMP.busca_por_indice(ind)

def busca_por_produto(id_produto):
  """Localiza os pedidos de compra que contém o produto com identificador {id_produto} 
  e devolve uma lista de identificadores das compras (não uma lista de objetos);
  ou lista vazia se não existir tal compra."""
  return compra_IMP.busca_por_produto(id_produto)

def busca_por_usuario(id_usuario):
  """Localiza os pedidos de compra feitas pelo usuário {id_usuario} 
  e devolve uma lista de identificadores compras (não uma lista de objetos);
  ou lista vazia se não existirem tais compras."""
  return compra_IMP.busca_por_usuario(id_usuario)

def cria_testes():
  """Limpa as tabelas de compras e de itens com {inicializa(True)}, e cria três pedidos
  de compra para fins de teste, incluindo-os na tabela.  Os pedidos estarão inicialmente
  com status 'aberto'. Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {base_sql.conecta}.  Supõe que as tabelas de usuários
  e de produtos já foram inicializadas, e cada uma tem pelo menos três entradas.""" 
  compra_IMP.cria_testes()

def diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  compra_IMP.diagnosticos(val)

def calcular_frete(compra, CEP):
  """Retorna float {frete} de uma compra para determinado CEP. A fórmula ainda não está definida."""

  return compra_IMP.calcular_frete(compra, CEP)
