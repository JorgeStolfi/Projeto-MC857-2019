# Este módulo define a classe de objetos {ObjProduto} que
# representa um produto do catálogo da loja virtual.

# Implementação deste módulo e da classe {ObjProduto}:
import produto_IMP; from produto_IMP import ObjProduto_IMP

class ObjProduto(ObjProduto_IMP):
  """Um objeto desta classe representa um produto da loja e armazena seus 
  atributos.  Por enquanto, eles são:
  
    {descr_curta} {str} - descrição do produto em uma linha.
    {descr_media} {str} - descrição do produto em 4 linhas, com dimensões etc.
    {descr_longa} {str} - descrição completa do produto. 
    {unid} {str} - unidade ("item", "caixa de 10", "metro", "rolo de 5m", etc.) 
    {preco} {float} - preço unitário.
    
  O preço unitário é em reais, e é arredondado para centavos inteiros 
  (a menos de erros de arredondamento do float).
  
  Mais atributos (imagens, estoque, volume, peso, descontos por atacado, etc.)
  podem ser acrescentados no futuro."""
  
  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'P-{NNNNNNNN}', onde 
    {NNNNNNNN} é um número de 8 algarismos 
    que identifica unicamente o produto. Este identificador é 
    atribuído na criação do produto e não pode ser alterado."""
    return ObjProduto_IMP.obtem_identificador(self)
    
  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do produto,
    exceto o identificador."""
    return ObjProduto_IMP.obtem_atributos(self)
    
  def muda_atributos(self,alts):
    """Recebe um dicionário {alts} cujas chaves são um subconjunto
    dos nomes de atributos do produto (exceto o identificador);
    e troca os valores desses atributos pels valores 
    correspondentes em {alts}. Também altera esses campos na base de dados.
    Em caso de sucesso, retorna o próprio objeto."""
    ObjProduto_IMP.muda_atributos(self,alts)
    
  def calcula_preco(self,qt):
    """Dada a quantidade {qt} a comprar (um float), calcula o preço a pagar.
    Em princípio o resultado é {qt} vezes o preço unitário, mas eventualmente
    poderá haver desconto por atacado, etc.."""
    
# Construtor da classe:

def cria(atrs):
  """Cria um novo objecto da classe {ObjProduto} com os
  atributos especificados pelo dicionário {atrs}, e 
  atribui um identificador único ao mesmo. Também acrescenta esse produto
  à base de dados.  Em caso de sucesso, retorna o objeto."""
  return produto_IMP.cria(atrs)

# Descrição dos campos:

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjProduto}, menos o identificador.  O resultado é adequado 
  para o parâmetro {cols} das funções do módulo {tabela_generica}."""
  return produto_IMP.campos()

# ======================================================================

# Funções para acesso à tabela de produtos (catálogo da loja).

# Implementação desta interface:
import tabela_de_produtos_IMP
from tabela_de_produtos_IMP import Obj_Tabela_De_Produtos_IMP

class Obj_Tabela_De_Produtos(Obj_Tabela_De_Produtos_IMP):
  # Um objeto (instância) desta classe representa a tabela de produtos
  # da base de dados da loja, ou seja o catálogo da loja. Deve haver
  # uma única instância no servidor.
  # 
  # Cada linha desta tabela representa um produto do catálogo.
  # Tem a maioria dos campos de um objeto de classe {ObjProduto}. 
  # 
  # Cada linha tem um índice inteiro (chave primária) que é atribuído
  # quando a linha é criada. As funções desta interface manuseiam o
  # índice na forma de um identificador de produto "P-{NNNNNNNN}".
  # 
  # Especificamente, cada linha tem os seguintes campos de informação
  # (colunas da tabela):
  #   
  #   'id_produto' {str} O identificador do produto, "P-{NNNNNNNN}".
  #   'descr_curta' {str} - descrição do produto em uma linha.
  #   'descr_media' {str} - descrição do produto em 4 linhas, com dimensões etc.
  #   'descr_longa' {str} - descrição completa do produto. 
  #   'unid' {str} - unidade ("item", "caixa de 10", "metro", "rolo de 5m", etc.) 
  #   'preco' {decimal(12,2)} - preço unitário.
  #   
  # Outros campos (como peso, volume, estoque, imagens, palvras-chave, etc.)
  # serão acrescentados oportunamente.
  # 
  # Todos os campos, exceto 'id_produto', podem ser alterados
  # (por exemplo para corrigir erros).
  # 
  # Nas funções abaixo, uma linha da tabela é representada na memória
  # por um dicionário Python {atrs} cujas chaves e valores
  # são os campos da linha.
  # 
  # Nas funções abaixo, o parametro {bas} é um objeto da classe {Base_SQL}
  # que representa a base de dados da loja.  

  def acrescenta(self,atrs):
    """Acrescenta uma nova linha na tabela de produtos
    da base {bas}, cujo conteúdo é o dicionário {atrs},
    e devolve o identificador "P-{NNNNNNNN}" da mesma.
    O dicionário não deve conter o campo 'id_produto'."""
    return Obj_Tabela_De_Produtos_IMP.acrescenta(self,atrs)

  def busca_por_identificador(self,id_produto):
    """Devolve um dicionário {atrs} com o conteúdo da linha 
    de identificador {id_produto} da tabela de produtos da base {bas}.
    O dicionário não inclui o campo 'id_produto'."""
    return Obj_Tabela_De_Produtos_IMP.busca_por_identificador(self,id_produto)

  def busca_por_palavra(self,pal):
    """Devolve uma lista com todos os identificadores "P-{NNNNNNNN}"
    dos produtos que contém a palavra {pal} nos seus 
    campos 'descr_curta' ou 'descr_media'.  Se não houver nenum item 
    satisfazendo a busca, devolve uma lista vazia."""
    return Obj_Tabela_De_Produtos_IMP.busca_por_palavra(self,pal)

  def atualiza(self,id_produto,atrs):
    """Modifica alguns campos de uma linha da tabela de produtos da base {bas}.
    A linha é especificada pelo seu identificador {id_produto}. 
    Não devolve nenhum resultado.

    O parâmetro {atrs} deve ser um dicionário cujas chaves são um
    subconjunto dos nomes dos campos da linha (excluindo 'id_produto'). 
    Os valores desses campos na tabela são substituídos pelos valores em {atrs}."""
    Obj_Tabela_De_Produtos_IMP.atualiza(self,id_produto,atrs)

def cria_tabela(bas):
  """Cria a tabela de produtos na base de dados {bas}.
  Esta função deve ser chamada apenas uma vez, quando o 
  servidor é iniciado."""
  return tabela_de_produtos_IMP.cria_tabela(bas)
