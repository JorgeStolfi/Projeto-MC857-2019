# Este módulo define a classe de objetos {ObjProduto} que
# representa um produto do catálogo da loja virtual.

# Implementação deste módulo e da classe {ObjProduto}:
import produto_IMP; from produto_IMP import ObjProduto_IMP

def inicializa(limpa):
  """Inicializa o modulo, criando a tabela de usuários na base de dados.
  Deve ser chamada apenas uma vez no ínicio da execução do servidor.
  Não retorna nenhum valor.  Se o parâmetro booleano {limpa} for {True},
  apaga todas as linhas da tabela SQL, resetando o contador em 0."""
  produto_IMP.inicializa(limpa)

class ObjProduto(ObjProduto_IMP):
  """Um objeto desta classe representa um produto da loja e armazena seus 
  atributos.  Por enquanto, eles são:
  
    {descr_curta} {str} - descrição do produto em uma linha.
    {descr_longa} {str} - descrição completa do produto. 
    {unid} {str} - unidade de venda ("item", "caixa de 10", "metro", "rolo de 5m", etc.) 
    {preco} {float} - preço unitário.
    
  O preço unitário é em reais, e é arredondado para centavos inteiros 
  (a menos de erros de arredondamento do float).
  
  Mais atributos (imagens, estoque, volume, peso, descontos por atacado, etc.)
  podem ser acrescentados no futuro.
  
  Cada produto da loja, mesmo com estoque esgotado, é representado por uma linha na tabela
  "produtos" da base SQL em disco. Apenas algumas dessas linhas são representadas também na memória por objetos
  da classe {ObjProduto}. 
  
  Cada linha da tabela tem um índice inteiro (chave primária) distinto, que é atribuído
  quando a linha é criada.  Neste sistema, esse índice é manipulado na forma de 
  um identificador de produto, uma string da forma "P-{NNNNNNNN}"
  onde {NNNNNNNN} é o índice formatado em 8 algarismos.
  
  Além disso, cada linha tem uma coluna da tabela (um campo) para cada um dos
  atributos do usuário (menos o identificador), como definido por {produto.campos()}.
  
  Todos os campos podem ser alterados, exceto o índice (e identificador).
  Entretanto, alterações no preço podem deixar pedidos de compras inconsistentes.
  Esse problema deverá ser tratado no futuro."""

def cria(atrs):
  """Cria um novo objecto da classe {ObjProduto} com os
  atributos especificados pelo dicionário {atrs}, acrescentando-o à tabéla de produtos da base de dados.
  Atribui um identificador único ao usuário, derivado do seu índice na tabela.
  Retorna o objeto criado."""
  return produto_IMP.cria(atrs)
  
def obtem_identificador(prod):
  """Devolve o identificador 'P-{NNNNNNNN}' do produto."""
  return produto_IMP.obtem_identificador(prod)
  
def obtem_indice(usr):
  """Devolve o índice inteiro do produto na tabela de produtos."""
  return produto_IMP.obtem_indice(usr)

def obtem_atributos(prod):
  """Retorna um dicionário Python que é uma cópia dos atributos do produto,
  exceto o identificador."""
  return produto_IMP.obtem_atributos(prod)
  
def muda_atributos(prod, mods):
  """Modifica alguns atributos do objeto {prod} da classe {ObjProduto},
  registrando as alterações na base de dados. Não devolve nenhum resultado.   

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do produto (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores 
  correspondentes em {mods}."""
  produto_IMP.muda_atributos(prod, mods)
  
def calcula_preco(prod, qt):
  """Dada a quantidade {qt} a comprar (um float), calcula o preço a pagar.
  Em princípio o resultado é {qt} vezes o preço unitário, mas eventualmente
  poderá haver desconto por atacado, etc.."""
  return produto_IMP.calcula_preco(prod,qt)

def busca_por_identificador(id_produto):
  """Localiza um produto com identificador {id_produto} (uma string da forma
  "P-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Obj_Produto}.
  Se tal produto não existe, devolve {None}."""
  return produto_IMP.busca_por_identificador(id_produto)

def busca_por_indice(ind):
  """Mesma que {busca_por_identificador}, mas quer o índice inteiro {ind} da linha da tabela,
  em vez do identificador do objeto."""
  return produto_IMP.busca_por_indice(ind)

def busca_por_palavra(prod, pal):
  """Devolve uma lista com todos os identificadores "P-{NNNNNNNN}"
  dos produtos que contém a palavra {pal} nos seus 
  campos 'descr_curta' ou 'descr_media'.  Se não houver nenhum item 
  satisfazendo a busca, devolve uma lista vazia."""
  return produto_IMP.busca_por_palavra(prod,pal)

def campos():
  """Retorna uma seqüência de tuplas que descrevem os nomes e propriedades
  dos atributos de um {ObjProduto}, menos o identificador.  O resultado é adequado 
  para o parâmetro {cols} das funções do módulo {tabela_generica}."""
  return produto_IMP.campos()

