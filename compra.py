# Este módulo define a classe de objetos {ObjCompra}, que
# representa um pedido de compra (em particular, um carrinho de
# compra).
# 
# Nas funções abaixo, o parãmetro {prod} é um objeto
# da classe {ObjProduto}; {usr} é um objeto da classe {ObjUsuario};
# e {qt} é um float não-negativo, a quantidade do produto a comprar.

# Interfaces importadas por esta interface:
import usuario; from usuario import ObjUsuario
import produto; from produto import ObjProduto
import base_sql; from base_sql import Base_SQL

# Implementaçao deste módulo:
import compra_IMP; from compra_IMP import ObjCompra_IMP

class ObjCompra(ObjCompra_IMP):
  """Um objeto desta classe representa e descreve um pedido de compra
  de um ou mais produtos em diversas quantidades, feito por um
  cliente da loja, que pode estar em várias etapas de execução.
  Em particular, o pedido pode ainda estar sendo construído e alterado
  pelo usuário -- ou seja, pode ser um "carrinho de compras".
  
  Por enquanto, os atributos de um objeto desta classe são:
  
    'usr'     um {ObjUsuario} que representa o cliente que fez ou está montando a compra.
    'itens'   uma lista Python de itens no pedido.
    'status'  uma string que indica o estado do pedido. 
    
  Cada elemento da lista 'itens' é uma lista de tres elementos {[prod,
  qt,preco]} onde {prod} é um objeto da classe {ObjProduto}, {qt} é
  um float que indica a quantidade comprada, e {preco} é um float que
  indica o preço total do item.  Os produtos na lista são sempre
  todos distintos.
  
  O atributo 'status' por enquanto, pode ser:
  
   'aberto': O cliente ainda está montando o pedido.
   'pagando':  O cliente fechou o pedido, e a loja está aguardando o pagamento.
   'pago': A loja já recebeu o pagamento e está mandando para despacho.
   'despachado': A loja já colocou o pedido no correio ou transportadora.
   'entregue': O pedido foi entregue ao cliente.
   
  Mais campos e/ou estados poderão ser acrescentados no futuro."""

  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'C-{NNNNNNNN}', onde
    {NNNNNNNN} é um número de 8 algarismos
    que identifica unicamente o pedido de compra. Este identificador é
    atribuído na criação do objeto e não pode ser alterado."""
    return ObjCompra_IMP.obtem_identificador(self)

  def obtem_usuario(self):
    """ Esta função retorna o cliente do pedido de compra
    (um objeto da classe {ObjUsuario})."""
    return ObjCompra_IMP.obtem_usuario(self)

  def obtem_status(self):
    """Retorna o atributo 'status' do pedido de compra."""
    return ObjCompra_IMP.obtem_status(self)

  def obtem_itens(self):
    """Retorna uma cópia da lista de itens no pedido de compra."""
    return ObjCompra_IMP.lista_itens(self)

  def calcula_total(self):
    """ Retorna um float que é o preco total do pedido de compra, ou seja a
    soma dos campos {qt} nos elementos da lista de itens."""
    return ObjCompra_IMP.calcula_total(self)
    
  def obtem_atributos(self):
    """Retorna um dicionário Python que é uma cópia dos atributos do pedido de
    compra, exceto identificador."""
    return ObjCompra_IMP.obtem_atributos(self)
    
  def muda_atributos(self, alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do pedido de compra (exceto o identificador), e troca os 
    valores desses atributos por cópias dos valores correspondentes em {alts}.
    A lista de itens (atributo 'itens') não pode ter produtos repetidos.
    Também altera esses campos na base de dados. 
    Em caso de sucesso, retorna o próprio objeto."""
    return ObjCompra_IMP.muda_atributos(self, alts)

  def acrescenta_item(self, prod, qt):
    """Acrescenta um novo item no pedido de compra, consistindo da quantidade 
    {qt} do produto {prod}.
    
    Se o produto já está na lista de itens, soma {qt} à quantidade que
    consta nessa lista. Também recalcula o preço do item e registra a
    alteração na tabela de compras da base {bas}. Se {qt} for zero, o
    efeito é nulo."""
    return ObjCompra_IMP.acrescenta_item(self,bas,prod,qt)

  def troca_qtd(self, prod, qt):
    """Modifica a lista de itens da compra, trocando a quantidade
    atual do produto {prod} por {qt}.
    Se {qt} for zero, elimina o produto {prod} da lista. 
    Se o produto {prod} não está na lista, acrescenta-o com 
    quantidade {qt}. Também recalcula o preço do item e registra
    a alteração na tabela de compras da base {bas}."""
    return ObjCompra_IMP.troca_qtd(self, prod, qt)

  def elimina_prod(self,prod):
    """Modifica a lista de itens da compra, eliminando a entrada
    com produto {prod}.  Se o produto não aparece na lista,
    não faz nada e devolve {False}; caso contrário devolve {True}."""
    return ObjCompra_IMP.elimina_prod(self,prod)
    
# Construtor da classe:

def cria(usr):
  """Esta função cria um objeto da classe {ObjCompra}, cujo usuário 
  é representado pelo objeto {usr} da classe {ObjOsuario}.
  O pedido será inicialmente vazio (sem nenhum produto) e status
  'aberto' (isto é, um carrinho de compras). 
  Também acrescenta esse pedido à base de dados."""
  return compra_IMP.cria(usr)

# Descrição dos campos:

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjCompra}, menos o identificador e a lista de itens.  
  O resultado é adequado para o parâmetro {cols} das funções do módulo
  {tabela_generica}."""
  return compra_IMP.campos()
# ======================================================================
# Funções para acesso à tabela de pedidos de compras.

# Implementação desta interface:
import tabela_de_compras_IMP
from tabela_de_compras_IMP import Obj_Tabela_De_Compras_IMP

class Obj_Tabela_De_Compras(Obj_Tabela_De_Compras_IMP):
  # Um objeto (instância) desta classe representa a tabela de usuários da base
  # de dados da loja. Deve haver uma única instância no servidor.
  # 
  # Cada linha desta tabela representa um pedido de compras (ou um
  # carrinho de compras) de um cliente. Tem a maioria dos campos de
  # objeto de classe {ObjCompra}, menos os itens da compra
  # (que estão numa tabela separada, {tabela_de_itens_de_compras.py}.
  #
  # Cada linha tem um índice inteiro (chave primária) que é atribuído
  # quando a linha é criada. As funções desta interface manuseiam o
  # índice na forma de um identificador de compra "C-{NNNNNNNN}".
  #
  # Especificamente, cada linha tem os seguintes campos de informação
  # (colunas da tabela):
  #
  #   'id_compra' {str} O identificador do pedido de compra, "C-{NNNNNNNN}".
  #   'id_usuario' {str} O identificador do cliente da compra, "U-{NNNNNNNN}".
  #   'status' {str} O status da compra: 'aberto', 'pagando', etc.
  #
  # Outros campos (como datas, endereço de entrega, forma de pagamento, etc.)
  # serão acrescentados oportunamente.  Todos os campos, menos
  # 'id_compra' e 'id_usuario', podem ser alterados.
  #
  # Nas funções abaixo, uma linha da tabela é representada na memória
  # por um dicionário Python {atrs} cujas chaves e valores
  # são os campos da linha.
  #
  # Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
  # que representa a base de dados da loja.

  def acrescenta(self,atrs):
    """Acrescenta uma nova linha na tabela de compras
    da base {bas}, cujo conteúdo é o dicionário {atrs},
    e devolve o identificador "C-{NNNNNNNN}" da mesm.
    O dicionário não deve conter o campo 'id_compra'."""
    return Obj_Tabela_De_Compras_IMP.acrescenta(self,atrs)

  def busca_por_identificador(self,id_compra):
    """Devolve um dicionário {atrs} com o conteúdo da linha
    de identificador {id_compra} da tabela de compras da base {bas}.
    O dicionário não inclui o campo 'id_compra'."""
    return Obj_Tabela_De_Compras_IMP.busca_por_identificador(self,id_compra)

  def atualiza(self,id_compra,atrs):
    """Modifica alguns campos de uma linha da tabela de compras da base {bas}.
    A linha é especificada pelo seu identificador {id_compra}.  Não devolve
    nenhum resultado.

    O parâmetro {atrs} deve ser um dicionário cujas chaves são um
    subconjunto dos nomes dos campos da linha (excluindo 'id_compra').
    Os valores desses campos na tabela são substituídos pelos valores em {atrs}."""
    Obj_Tabela_De_Compras_IMP.atualiza(self,id_compra,atrs)

def cria_tabela(bas):
  """Cria a tabela de compras na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o
  servidor é iniciado."""
  return tabela_de_compras_IMP.cria_tabela(bas)
# ======================================================================
# Funções para acesso à tabela de itens de pedidos de compras.

# Implementação desta interface:
import tabela_de_itens_de_compras_IMP
from tabela_de_itens_de_compras_IMP import Obj_Tabela_De_Itens_De_Compras_IMP

class Obj_Tabela_De_Itens_De_Compras(Obj_Tabela_De_Itens_De_Compras_IMP):
  # Um objeto (instância) desta classe representa a tabela de itens de compras
  # na base de dados da loja. Deve haver uma única instância no servidor.
  # 
  # Cada linha desta tabela é um item de um pedido de compras:
  # ou seja, uma determinada quantidade de um determinado produto.
  # 
  # Cada linha tem um índice inteiro (chave primária) que é atribuído
  # quando a linha é criada. As funções desta interface manuseiam o
  # índice na forma de um identificador de item de compra "I-{NNNNNNNN}".
  # 
  # Especificamente, cada linha tem os seguintes campos de informação
  # (colunas da tabela):
  #   
  #   'id_compra' {str} O identificador do pedido de compra, "C-{NNNNNNNN}".
  #   'id_produto' {str} O identificador do produto a comprar, "P-{NNNNNNNN}".
  #   'qt' {float} A quantidade a comprar.
  #   'preco' {decimal(12,2)} o preço total do item.
  # 
  # Outros campos (como peso e volume) poderão vir a ser
  # acrescentados oportunamente.
  # 
  # Todos os campos, exceto {id_compra}, e {id_produto}, 
  # podem ser alterados.
  # 
  # Nas funções abaixo, uma linha da tabela é representada na memória
  # por um dicionário Python {atrs} cujas chaves e valores
  # são os campos da linha.
  # 
  # Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
  # que representa a base de dados da loja.

  def acrescenta(self, atrs):
    """Acrescenta uma nova linha na tabela de itens de compras
    da base {bas}, cujo conteúdo é o dicionário {atrs}, e devolve
    o identificador "I-{NNNNNNNN}" da mesma.
    O dicionário não deve conter o campo 'id_item'."""
    return Obj_Tabela_De_Itens_De_Compras_IMP.acrescenta(self, atrs)

  def busca_por_identificador(self, id_item):
    """Devolve um dicionário {atrs} com o conteúdo da linha 
    de identificador {id_item} da tabela de itens de compras da base {bas}.
    O dicionário não inclui o campo 'id_item'."""
    return Obj_Tabela_De_Itens_De_Compras_IMP.busca_por_identificador(self, id_item)

  def busca_por_compra(self, id_compra):
    """Devolve uma lista com todos os identificadores "I-{NNNNNNNN}"
    dos itens cujo identificador de compra é 'id_compra'. 
    Se não houver nenum item satisfazendo a busca, devolve uma lista vazia."""
    return Obj_Tabela_De_Itens_De_Compras_IMP.busca_por_compra(self, id_compra)

  def busca_por_produto(self, id_produto):
    """Devolve uma lista com todos os identificadores "I-{NNNNNNNN}"
    dos itens cujo identificador de produto é 'id_produto'. 
    Se não houver nenum item satisfazendo a busca, devolve uma lista vazia."""
    return Obj_Tabela_De_Itens_De_Compras_IMP.busca_por_produto(self, id_produto)

  def atualiza(self, id_item, atrs):
    """Modifica alguns campos de uma linha da tabela de itens de compras da base {bas}.
    A linha é especificada pelo seu identificador {id_item}.  Não devolve nenhum resultado.

    O parâmetro {atrs} deve ser um dicionário cujas chaves são um
    subconjunto dos nomes dos campos da linha. Os valores desse campos na
    tabela são substituídos pelos valores em {atrs}.
    O dicionário {atrs} não deve ter a chave 'id_item'."""
    Obj_Tabela_De_Itens_De_Compras_IMP.atualiza(self, id_item, atrs)

def cria_tabela(bas):
  """Cria a tabela de itens de compras na base de dados {bas}. 
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  return tabela_de_itens_de_compras_IMP.cria_tabela(bas)
