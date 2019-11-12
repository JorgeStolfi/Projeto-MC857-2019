# Implementação do módulo {produto} e da classe {ObjProduto}.

import produto

import tabela_generica
import conversao_sql
import identificador
import tabelas
from utils_testes import erro_prog, aviso_prog, mostra
import sys # Para diagnóstico.

# VARIÁVEIS GLOBAIS DO MÓDULO

nome_tb = "produtos"
  # Nome da tabela na base de dados.

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ObjProdutos} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidadde dos objetos.

letra_tb = "P"
  # Prefixo dos identificadores de produtos.

colunas = \
  ( ( 'descr_curta', type("foo"), 'TEXT',    False ), # Descricao curta do produto.
    ( 'descr_media', type("foo"), 'TEXT',    False ), # Descricao media do produto.
    ( 'descr_longa', type("foo"), 'TEXT',    False ), # Descricao longa do produto.
    ( 'palavras',    type("foo"), 'TEXT',    True  ), # Sinônimos e termos relacionados, para busca.
    ( 'unidade',     type("foo"), 'TEXT',    False ), # Unidade de venda ('metro', 'caixa', 'peça', etc.).
    ( 'preco',       type(10.5),  'FLOAT',   False ), # Preco unitário do produto em reais.
    ( 'imagem',      type("foo"), 'TEXT',    False ), # Nome do arquivo da imagem no diretorio 'imagens'.
    ( 'peso',        type(10.5),  'FLOAT',   False ), # peso do produto em gramas.
    ( 'volume',      type(10.5),  'FLOAT',   False ), # volume do produto em mililitros.
    ( 'estoque',     type(10),    'INTEGER', False ), # Estoque do produto.
    ( 'oferta',      type(True),  'INTEGER', False ), # Produto está em oferta.
    ( 'variado',     type(True),  'INTEGER', False ), # Produto possui variedades.
    ( 'grupo',       type("foo"), 'TEXT',    True  ), # Identificador de produto do grupo.
    ( 'variedade',   type("foo"), 'TEXT',    True  ), # Descrição super-curta do produto, relativa ao grupo.
  )
  # Descrição das colunas da tabela na base de dados.

diags = False
  # Quando {True}, mostra comandos e resultados em {stderr}. 

class ObjProduto_IMP():
  # Definição interna da classe {ObjUsuario}:

  def __init__(self, id_produto, atrs):
    self.atrs = atrs.copy()
    self.id_produto = id_produto

# Implementação das funções:

def inicializa(limpa):
  global cache, nome_tb, letra_tb, colunas, diags
  if limpa:
    tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    tabela_generica.cria_tabela(nome_tb, colunas)
    
def cria(atrs):
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "produto_IMP.cria(" + str(atrs) + ") ...")
  
  # Converte atributos para formato SQL.
  atrs_SQL = conversao_sql.dict_mem_para_dict_SQL(atrs, colunas, False, tabelas.obj_para_indice)
  
  # Insere na base de dados e obtém o índice na mesma:
  prod = tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj, atrs_SQL)
  assert type(prod) is produto.ObjProduto
  return prod

def obtem_identificador(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.id_produto

def obtem_palavras(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.palavras

def obtem_indice(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return identificador.para_indice(letra_tb, prod.id_produto)

def obtem_preco(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.atrs['preco']

def obtem_atributos(prod):
  global cache, nome_tb, letra_tb, colunas, diags
  return prod.atrs.copy()

def calcula_preco(prod, qtd):
  return prod.atrs['preco'] * qtd

def muda_atributos(prod, mods):
  global cache, nome_tb, letra_tb, colunas, diags
  # Converte valores de formato memória para formato SQL. 
  mods_SQL = conversao_sql.dict_mem_para_dict_SQL(mods, colunas, True, tabelas.obj_para_indice)
  
  # Modifica atributos na tabela e na memória:
  res = tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj, prod.id_produto, mods_SQL)
  assert res == prod
  return

def busca_por_identificador(id_produto):
  global cache, nome_tb, letra_tb, colunas, diags
  prod = tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj, id_produto)
  return prod

def busca_por_indice(ind):
  global cache, nome_tb, letra_tb, colunas, diags
  usr = tabela_generica.busca_por_indice(nome_tb, cache, letra_tb, colunas, def_obj, ind)
  return usr

def busca_por_palavra(pal):
  chaves = ('descr_curta', 'descr_media', 'palavras')
  valores = (pal,)
  busca_com_and = ' AND ' in pal
  
  if busca_com_and:
    valores = pal.split(' AND ')
    valores = tuple(valores)
 
  produtos =  tabela_generica.busca_por_semelhanca(nome_tb, letra_tb, colunas, chaves, valores)
  return produtos

def busca_ofertas():
  lista_ids=tabela_generica.busca_por_campo(nome_tb,letra_tb,colunas,"oferta",1)
  return lista_ids

def cria_testes():
  global cache, nome_tb, letra_tb, colunas, diags
  inicializa(True)
  lista_atrs = \
    [ 
      {
        'descr_curta': "Escovador de ouriço",
        'variado' : False,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
        'palavras': 'escovador, animal, ourico, animais, portátil',
        'descr_longa': 
          """Fabricante: Ouricex LTD<br/>
          Origem: Cochinchina<br/>
          Modelo: EO-22<br/>
          Tensão: 110-230 V<br/>
          Potência: 1500 W<br/>
          Acessórios: cabo de força de 50 m, 10 pentes finos, 10 pentes grossos, valise em ABS<br/>
          Dimensões: 300 x 200 x 3000 mm""",
        'preco': 120.50,
        'imagem': "155951.png",
        'estoque': 500,
        'unidade': "1 aparelho",
        'peso':10.0,
        'volume':500.5,
        'oferta' : True,
      },
      {
        'descr_curta': "Furadeira telepática (x 2)",
        'variado' : False,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Kit com duas furadeiras telepáticas 700 W para canos de até 2 polegadas com acoplador para guarda-chuva e cabo de força",
        'palavras': 'furadeira, marcenaria',
        'descr_longa': 
          """"Fabricante: Ferramentas Tres Dedos SA<br/>
          Origem: Brasil<br/>
          Modelo: FT7T<br/>
          Tensão: insuportável<br/>
          Potência: 700 W<br/>
          Material: Alumínio, policarbonato, chiclete.<br/>
          Acessórios: 1 acoplador para guarda-chuvas, 1 jogo de 5 pedais, cabo de força de 2 m.<br/>
          Dimensões: 150 x 400 x 250 mm""",
        'preco': 420.00,
        'imagem': "156931.png",
        'estoque': 500,
        'unidade': "caixa de 2",
        'peso':10.0,
        'volume':500.5,
        'oferta' : False,
      },
      {
        'descr_curta': "Luva com 8 dedos",
        'variado' : True,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Luva para mão esquerda com 8 dedos, em camurça, com forro de bom-bril",
        'palavras': 'luva, inverno',
        'descr_longa': 
          """Fabricante: United Trash Inc.<br/>
          Origem: USA<br/>
          Modelo: 8-EB<br/>
          Normas: ANSI 2345, ABNT 2019-857<br/>
          Material: Camurça artificial 1 mm, lã de aço.<br/>
          Tamanho: G<br/>
          Peso: 120 g""",
        'preco': 19.95,
        'imagem': "160519.png",
        'estoque': 500,
        'unidade': "1 unidade",
        'peso':10.0,
        'volume':500.5,
        'oferta' : True,
      },
      {
        'descr_curta': "Luva com 8 dedos",
        'variado' : False,
        'grupo': "P-00000003",
        'variedade' : "Tamanho M",
        'descr_media': "Luva para mão esquerda com 8 dedos, em camurça, com forro de bom-bril",
        'palavras': 'luva, inverno',
        'descr_longa': 
          """Fabricante: United Trash Inc.<br/>
          Origem: USA<br/>
          Modelo: 8-EB<br/>
          Normas: ANSI 2345, ABNT 2019-857<br/>
          Material: Camurça artificial 1 mm, lã de aço.<br/>
          Tamanho: G<br/>
          Peso: 120 g""",
        'preco': 19.95,
        'imagem': "160519.png",
        'estoque': 500,
        'unidade': "1 unidade",
        'peso':10.0,
        'volume':500.5,
        'oferta' : True,
      },
      {
        'descr_curta': "Luva com 8 dedos",
        'variado' : False,
        'grupo': "P-00000003",
        'variedade' : "Tamanho G",
        'descr_media': "Luva para mão esquerda com 8 dedos, em camurça, com forro de bom-bril",
        'palavras': 'luva, inverno',
        'descr_longa': 
          """Fabricante: United Trash Inc.<br/>
          Origem: USA<br/>
          Modelo: 8-EB<br/>
          Normas: ANSI 2345, ABNT 2019-857<br/>
          Material: Camurça artificial 1 mm, lã de aço.<br/>
          Tamanho: G<br/>
          Peso: 120 g""",
        'preco': 19.95,
        'imagem': "160519.png",
        'estoque': 500,
        'unidade': "1 unidade",
        'peso':10.0,
        'volume':500.5,
        'oferta' : True,
      },
      {
        'descr_curta': "Luva com 8 dedos",
        'variado' : False,
        'grupo': "P-00000003",
        'variedade' : "Tamanho P",
        'descr_media': "Luva para mão esquerda com 8 dedos, em camurça, com forro de bom-bril",
        'palavras': 'luva, inverno',
        'descr_longa': 
          """Fabricante: United Trash Inc.<br/>
          Origem: USA<br/>
          Modelo: 8-EB<br/>
          Normas: ANSI 2345, ABNT 2019-857<br/>
          Material: Camurça artificial 1 mm, lã de aço.<br/>
          Tamanho: G<br/>
          Peso: 120 g""",
        'preco': 19.95,
        'imagem': "160519.png",
        'estoque': 500,
        'unidade': "1 unidade",
        'peso':10.0,
        'volume':500.5,
        'oferta' : True, 
      },
      {
        'descr_curta': "Ferroada",
        'variado' : False,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Espada élfica forjada na cidade de Gondolin.",
        'palavras': 'espada, elfo, senhor dos aneis',
        'descr_longa': 
          """Fabricante: Gondolin Ferreiros SA<br/>
          Origem: Gondolin<br/>
          Dono Original: Bilbo""",
        'preco': 2000.00,
        'imagem': "170859.png",
        'estoque': 500,
        'unidade': "1 espada" ,
        'peso':10.0,
        'volume':500.5,
        'oferta' : False,
      },
      {
        'descr_curta': "Amassador de suspiros",
        'variado' : False,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Amassador de suspiros lânguidos manual com 5 velocidades e 2 temperaturas.",
        'palavras': 'amassador, suspiro',
        'descr_longa': 
          """Fabricante: Produits Ineffables SA<br/>
          Origem: França<br/>
          Acionamento: manual<br/>
          Acessórios: frasco de elixir, estojo, 4 parafusos de fixação com buchas<br/>
          Peso: excessivo<br/>
          Volume: estridente""",
        'preco': 49.99,
        'imagem': "136714.png",
        'estoque': 20,
        'unidade': "1 aparelho",
        'peso':10.0,
        'volume':500.5,
        'oferta' : True,
      },
      
      { 'descr_curta': "Cabideiro",
        'variado' : False,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Cabideiro com capacidade para 420 cabides", 
        'palavras':'cabide, cabides, roupas, roupa',
        'descr_longa': 
          """Lindo cabideiro com suporte para 420 cabides, ideal para você, seus pais, filhos, irmãos, tios e cachorros<br/>
          Fabricante: Gargah Lar SA""",
        'preco': 69.00, 
        'imagem': "146752.png", 
        'estoque': 1, 
        'unidade': "01 (hum) cabideiro",
        'peso':10.0,
        'volume':500.5,
        'oferta' : False,
      },

      { 'descr_curta': "Ácido patético",
        'variado' : True,
        'grupo' : None,
        'variedade' : None,
        'descr_media': "Ácido patético (H2PeO4) puro ACS para análise", 
        'palavras':'química,limpeza,elixir',
        'descr_longa': 
          """Ácido patético puro para análise<br/>
          Fabricante: Tox Chic SA<br/>
          Fórmula: H2PeO4<br/>
          Pureza: 99.8%<br/>
          """,
        'preco': 25.00, 
        'imagem': "170013.png", 
        'estoque': 50, 
        'unidade': "frasco",
        'peso': 10.0,
        'volume': 500.5,
        'oferta' : False,
      },
      { 'descr_curta': "Ácido patético - 200 mL",
        'variado' : False,
        'grupo' : "P-00000010",
        'variedade' : "200 mL",
        'descr_media': "Ácido patético (H2PeO4) puro ACS para análise - 200 mL", 
        'palavras': None,
        'descr_longa': 
          """Ácido patético puro para análise, 200 mL<br/>
          Embalagem: Garrafa de vidro<br/>
          """,
        'preco': 20.00, 
        'imagem': "170013.png", 
        'estoque': 50, 
        'unidade': "frasco",
        'peso': 300.0,
        'volume': 200.5,
        'oferta' : False,
      },
      { 'descr_curta': "Ácido patético - 500 mL",
        'variado' : False,
        'grupo' : "P-00000010",
        'variedade' : "500 mL",
        'descr_media': "Ácido patético (H2PeO4) puro ACS para análise - 500 mL", 
        'palavras':'química,limpeza,elixir',
        'descr_longa': 
          """Ácido patético puro para análise, 500 mL<br/>
          Embalagem: Garrafa de vidro<br/>
          """,
        'preco': 45.00, 
        'imagem': "170013.png", 
        'estoque': 50, 
        'unidade': "frasco",
        'peso': 650.0,
        'volume': 500.5,
        'oferta' : False,
      },
      { 'descr_curta': "Ácido patético - 5 litros",
        'variado' : False,
        'grupo' : "P-00000010",
        'variedade' : "5 litros",
        'descr_media': "Ácido patético (H2PeO4) puro ACS para análise - 5 litros", 
        'palavras':'química,limpeza,elixir',
        'descr_longa': 
          """Ácido patético puro para análise, 5 litros<br/>
          Embalagem: Bombona de polietileno<br/>
          """,
        'preco': 370.00, 
        'imagem': "170013.png", 
        'estoque': 50, 
        'unidade': "frasco",
        'peso': 7000.0,
        'volume': 5000.0,
        'oferta' : False,
      },
    ]
  for atrs in lista_atrs:
    # Acrescenta o produto à base de dados:
    prod = cria(atrs)
    assert prod != None and type(prod) is produto.ObjProduto
    # Mostra na janela de shell:
    sys.stderr.write("id = %s \"%s\"" % (produto.obtem_identificador(prod), atrs['descr_curta'],))
    if ('grupo' in atrs) and (atrs['grupo'] != None):
      sys.stderr.write(" [grupo = %s var = \"%s\"]" % (str(atrs['grupo']), str(atrs['variedade'],)))
    sys.stderr.write("\n")
  return

# FUNÇÕES INTERNAS

def def_obj(obj, id_produto, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {ObjProduto} com
  identificador {id_produto} e atributos {atrs_SQL}, tais como extraidos
  da tabela de sessoes. O objeto *não* é inserido na base de dados. 
  
  Se {obj} não é {None}, deve ser um objeto da classe {ObjProduto}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}.
  
  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global cache, nome_tb, letra_tb, colunas, diags
  if diags: mostra(0, "produto_IMP.def_obj(" + str(obj) + ", " + id_produto + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, tabelas.obj_para_indice)
    if diags: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = produto.ObjProduto(id_produto, atrs_mem)
  else:
    assert obj.id_produto == id_produto
    # Converte atributos para formato na memória.
    mods_mem = conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, tabelas.obj_para_indice)
    if diags: mostra(2, "modificando objeto, mods_mem = " + str(mods_mem))
    assert type(mods_mem) is dict
    if len(mods_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in mods_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      obj.atrs[chave] = val
  if diags: mostra(2, "obj = " + str(obj))
  return obj


def diagnosticos(val):
  global cache, nome_tb, letra_tb, colunas, diags
  diags = val
  return

