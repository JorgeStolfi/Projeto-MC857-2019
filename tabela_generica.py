# Funções para manipular tabelas da base de dados.

# Uma tabela de objetos de uma certa classe ({ObjUsuario}, {ObjProduto}, etc) 
# consiste de uma tabela da base SQL, mais um cache de objetos
# na memória.  
#
# Cada tabela SQL tem uma columa de tipo inteiro, 'indice' que é a chave primária
# Esta coluna é incrementada automaticamente pela biblioteca SQL 
# sempre que um objeto é acrescentado à tabela.
#
# Este módulo supõe que cada objeto tem um identificador único da forma 
# "{X}-{NNNNNNNN}", onde {X} é uma letra que indica o tipo dos objetos
# armazenados na tabela ("U" para usuário, "P" para {ObjProduto}, etc.), 
# e {NNNNNNNN} é o índice do objeto na tabela SQL, formatado como 8 
# algarismos decimais.  
#
# O cache de cada tabela é um dicionario Python que mapeia identificadores para 
# objetos.  Os objetos no cache são cópias fiéis de zero ou mais
# linhas da tabela.
#
# Nas funções abaixo, 
#
#   {nome_tb} é o nome da tabela na base (uma string, p. ex. "usuarios"). 
#
#   {cache} é o cache de objetos dessa tabela.
#
#   {let} é a letra de prefixo dos identificadores da tabela (p. ex. "U").
#
#   {cols} é uma seqüência de tuplas que descrevem os campos da tabela,
#     menos o índice da linha.
#
#   {cria_obj} é uma função que constrói um objeto da classe correta, dados seu
#     identificador {id} e um dicionário Python {atrs} que define os valores de seus
#     demais atributos.
#
# Cada tupla da seqüência {cols} tem os seguintes elementos: 
#  
#   A chave do atributo (um string, por exemplo 'nome' ou 'telefone'),
#  
#   O tipo Python (por exemplo, {<class 'int'>})
#  
#   O tipo SQL usado para armazenar o atributo na base
#     (por exemplo, 'INTEGER' ou 'TEXT NOT NULL').
#      
#   Limites minimo e máximo para o campo. Se for texto,
#     os limites referem-se ao comprimento. Se for numérico,
#     referem-se ao valor.
#
# Em caso de erro, as funções abaixo devolvem um string
# que descreve o mesmo, em vez do valor indicado.

# Implementação da interface:
import tabela_generica_IMP

def cria_tabela(nome_tb, cols):
  """Cria a tabela {nome_tb} dentro da base de dados,
  com as colunas descritas em {cols}.  Retorna {None} 
  em caso de sucesso.
  
  Esta função deveria ser chamada apenas uma vez em cada 
  inicialização do servidor, depois de chamar {base_sql.conecta}."""
  return tabela_generica_IMP.cria_tabela(nome_tb, cols)

def acrescenta(nome_tb, cache, let, cols, cria_obj, atrs):
  """Acrescenta mais um objeto {obj} com atributos {atrs} na tabela {nome_tb} 
  da base {bas}, e também no seu {cache}.  O identificador {id} 
  do objeto será "{let}-{ind}", onde {ind} é o índice da linha 
  correspondente na tabela, formatado 
  em 8 dígitos.  O objeto será criado pela chamada {cria_obj(id,atrs)}.
  Os campos de {atrs} devem ser consistentes com o parâmetro {cols}.
  
  Em caso de sucesso, devolve o objeto criado {obj}."""
  return tabela_generica_IMP.acrescenta(nome_tb, cache, let, cols, cria_obj, atrs)

def busca_por_identificador(nome_tb, cache, let, cols, cria_obj, ident):
  """Procura na tabela {nome_tb} e no seu {cache}
  um objeto com o identificador {ident}, que deve ter a forma 
  "{let}-{ind}" onde {ind} é o índice na tabela. 
  
  Mais precisamente, se já existir um objeto {obj} com identificador {ident}
  no dicionario {cache}, pega esse objeto.  Caso contrário
  extrai da tabela {nome_tb} a linha com índice {ind},
  cria um {obj} objeto com {cria_obj(ident,atrs)} onde {atrs} são as colunas
  dessa linha, e armazena {obj} no cache.  Nos dois casos, devolve o 
  objeto {obj}.  Se não existir a linha {ind} na tabela, devolve {None}."""
  return tabela_generica_IMP.busca_por_identificador(nome_tb, cache, let, cols, cria_obj, ident)

def busca_por_campo(nome_tb, cache, let, cols, chave, valor):
  """Procura na tabela {nome_tb} e no seu {cache}
  objetos que tem o valor {val} na coluna de nome {chave}.
  A {chave} deve ser o nome de uma coluna da tabela, como
  definido em {cols}.
  
  Devolve uma lista com os identificadores dos objetos
  encontrados (não os objetos em si). Se nenhuma linha
  satisfizer o critério da busca, devolve uma lista vazia."""
  return tabela_generica_IMP.busca_por_campo(nome_tb, cache, let, cols, chave, valor)

def atualiza(nome_tb, cache, let, cols, cria_obj, muda_obj, ident, alts):
  """Procura na tabela {nome_tb} e no seu {cache}
  um objeto {obj} com o identificador {ident}, que deve ter a forma 
  "{let}-{ind}" onde {ind} é o índice na tabela.  O objeto 
  deve existir.  Se o objeto não estiver no {cache}, cria o mesmo
  com {cria_obj(ident,atrs)} onde {atrs} são os campos atuais da linha da tabela.
  Modifica os atributos desse objeto usando a função {muda_obj(obj,alts)}
  atualizando a linha correspondente da tabela.  Devolve o objeto 
  {obj} em caso de sucesso. 
  
  Especificamente, para cada chave no dicionário {alts}, substitui 
  o valor corrente desse atributo em {obj} pelo valor
  associado em {alts}.  As chaves de {alts} devem ser um 
  subconjuto dos nomes das colunas da tabela, como 
  definido em {cols}."""
  return tabela_generica_IMP.atualiza(nome_tb, cache, let, cols, cria_obj, muda_obj, ident, alts)

def limpa_tabela(nome_tb, cols):
  """Apaga todas as entradas da tabela {nome_tb}, e reinicializa o
  contador de linhas em 0.  Retorna {None} em caso de sucesso."""
  return tabela_generica_IMP.limpa_tabela(nome_tb, cols)
