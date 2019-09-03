# Este módulo define a classe de objetos {ObjProduto} que
# representa um produto do catálogo da loja virtual.
# 
# Nas funções abaixo, {bas} é um objeto da classe {Base_SQL}
# que representa a base de dados da loja.

# Interfaces importadas por esta interface:
import base_sql; from base_sql import Base_SQL

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
    
  def calcula_preco(self,qt):
    """Dada a quantidade {qt} a comprar (um float), calcula o preço a pagar.
    Em princípio é {qt} vezes o preço unitário, mas eventualmente
    poderá haver desconto por atacado, etc.."""
    
  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do produto
    (exceto o identificador)."""
    return ObjProduto_IMP.obtem_atributos(self)
    
  def muda_atributos(self,bas,alts):
    """Recebe um dicionário {alts} cujas chaves são um subconjunto
    dos nomes de atributos do produto (exceto o identificador);
    e troca os valores desses atributos pels valores 
    correspondentes em {alts}.  Também atualiza a entrada
    correspondente da tabela de sessoes da base {bas}. 
    Não retorna nenum resultado."""
    ObjProduto_IMP.muda_atributos(self,bas,alts)
    
# Construtor da classe:

def cria(bas,atrs):
  """Cria um novo objecto da classe {ObjProduto} com atributos especificados pelo 
  dicionário {atrs} (que não deve incluir o identificador). Acrescenta esse 
  produto à tabela de produtos da base {bas}, e define seu identificador 
  a partir do índice do produto nessa base."""
  return produto_IMP.cria(bas,atrs)

