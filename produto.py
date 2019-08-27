# Este módulo define a classe de objetos {Produto} que
# representa um produto do catálogo da loja virtual.

# Implementação deste módulo e da classe {Produto}:
import produto_IMP; from produto_IMP import Produto_IMP

class Produto(Produto_IMP):
  """Um objeto desta classe representa um produto da loja e armazena seus 
  atributos.  Por enquanto:
    {descr_curta} {str} - descrição do produto em uma linha.
    {descr_media} {str} - descrição do produto em 4 linhas, com dimensões etc.
    {descr_longa} {str} - descrição completa do produto. 
    {unid} {str} - unidade ("item", "caixa de 10", "metro", "rolo de 5m", etc.) 
    {preco} {float} - preço unitário.
  """
  
  def obtem_identificador(self):
    """Devolve uma cadeia no formato 'P-{NNNNNNNN}', onde 
    {NNNNNNNN} é um número de 8 algarismos 
    que identifica unicamente o produto. Este identificador é 
    atribuído na criação do produto e não pode ser alterado."""
    return Produto_IMP.obtem_identificador(self)
    
  def calcula_preco(self,qt):
    """Dada a quantidade {qt} a comprar (um float), calcula o preço a pagar.
    Em princípio é {qt} vezes o preço unitário, mas eventualmente
    poderá haver desconto por atacado, etc.."""
    
  def obtem_atributos(self):
    """Retorna um dicionário Python com os atributos do produto,
    exceto o identificador."""
    return Produto_IMP.obtem_atributos(self)
    
  def muda_atributos(self,alts):
    """Recebe um dicionário Python {alts} cujas chaves são um subconjunto
    dos nomes de atributos do produto, e troca os valores desses atributos 
    pels valores correspondentes em {alts}.  Não retorna nenum resultado."""
    Produto_IMP.muda_atributos(self,alts)
    
# Construtor da classe:

def cria(atrs):
  """Cria um novo produto com atributos especificados pelo dicionário Python {atrs}.
  Acrescenta esse produto na base de dados de produtos, e define seu identificador 
  a partir do índice do produto nessa base."""
  return produto_IMP.cria(atrs)

