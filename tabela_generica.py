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
#     menos o índice da linha e o identificador do objeto
#     (vide descrição em {cria_tabela} abaixo).
#
#   {atrs_SQL} é um dicionário Python com os atributos do objeto, menos o identificador, tal como 
#     representados na base de dados SQL.
#
#   {def_obj} é uma função que é chamada pelas funções abaixo para
#     construir ou modificar objetos na memória, dados seus atributos na
#     base de dados. Ela recebe parâmetros {(obj,ident,atrs_SQL)} onde
#     {obj} é {None} ou um objeto da classe associaada à tabela
#     ({ObjUsuario}, {Objproduto}, etc.); {ident} é um identificador de
#     objetos dessa classe ("U-{NNNNNNNN}", "P-{NNNNNNNN}", etc.); e
#     {atrs_SQL} é um dicionário que associa nomes de colunas a seus
#     valores.
#
#     Se {obj} for {None}, a função {def_obj} deve criar um novo objeto
#     da classe correta, com identificador {ident} e atributos
#     {atrs_SQL}. Neste caso, {atrs_SQL} deve ter todas as colunas da
#     tabela. Se {obj} não é {None}, {def_obj} deve alterar os campos do
#     objeto {obj} dado; neste caso, {atrs_SQL} pode ter apenas um
#     subconjuto das colunas da tabela.
#     
#     Nos dois casos, a função {def_obj} precisa converter
#     os valores em {atrs_SQL} do formato SQL para o formato na memória
#     como especificado em {cols}, e devolver o objeto criado ou modificado.
# 
#     A função {def_obj} é chamada quando a entrada do objeto {obj}
#     no cache está inconsistente com sua linha na base de dados.
#     Portanto, a função {def_obj} não deve tentar fazer buscas na 
#     tabela {nome_tb}, nem acessar essa linha dessa tabela.
#     Ela pode porém chamar {busca_por_identificador} para 
#     converter identificadores em objetos.
#
# Em caso de erro, as funções abaixo abortam com mensagem de erro.

# Implementação da interface:
import tabela_generica_IMP

def cria_tabela(nome_tb, cols):
  """Cria a tabela {nome_tb} dentro da base de dados,
  com as colunas descritas em {cols}.  Não retorna nenhum resultado.
  
  O parâmetro {cols} é uma seqüência de tuplas. Cada tupla 
  descreve uma coluna da tabela (exceto o índice), e
  tem os seguintes elementos: 
   
    [0] A chave do atributo (um string, por exemplo 'nome' ou 'telefone'),
   
    [1] O tipo Python (por exemplo, {type(int)})
   
    [2] O tipo SQL usado para armazenar o atributo na base
        (por exemplo, 'INTEGER' ou 'TEXT').
       
    [3] Um booleano que diz se a coluna pode ser {NULL} na 
      tabela SQL.
        
  Certos valores de atributos na memória exigem conversão para poderem ser
  armazenados ou recueperados da base em disco.  Por exemplo, um atributo
  que tem tipo {bool} na memória é gravado na base como um valor de tipo SQL
  'INTEGER', que é 0 se {False}, 1 se {True}.  Se o valor de um atributo na
  memória é um objeto {obj} (por exemplo, o atributo 'usr' de uma sessão, que é
  um {ObjUsuario}), a coluna correspondente na base de dados terá tipo 
  SQL 'INTEGER', e o valor será o índice do objeto {obj} na sua 
  respectiva tabela.
  
  Se o tipo de um atributo na memória é lista, tupla, ou dicionário,
  esse atributi não pode ser armazenado numa coluna da base SQL.
  Nesse caso o item [2] da descrição acima deve ser {None}, e o 
  item [3] é irrelevante.
      
  Esta função deveria ser chamada apenas uma vez em cada 
  inicialização do servidor, depois de chamar {base_sql.conecta}."""
  return tabela_generica_IMP.cria_tabela(nome_tb, cols)

def acrescenta(nome_tb, cache, let, cols, def_obj, atrs_SQL):
  """Acrescenta mais um objeto {obj} com atributos {atrs_SQL} na tabela {nome_tb} 
  da base {bas}, e também no seu {cache}. Cada valor de {atrs_SQL} 
  deve ser consistente com os tipo SQL especificado no parâmetro {cols}. 
  Devolve o objeto criado {obj}.
  
  O identificador {id} do objeto será "{let}-{ind}", onde {ind} é o
  índice da linha correspondente na tabela, formatado em 8 dígitos. 
  
  A função chamará {obj=def_obj(None,id,atrs_SQL)} para criar o objeto
  {obj} na memória, depois de acrescentar a linha no banco de dados mas
  antes de atualizar o cache."""
  return tabela_generica_IMP.acrescenta(nome_tb, cache, let, cols, def_obj, atrs_SQL)

def atualiza(nome_tb, cache, let, cols, def_obj, ident, mods_SQL):
  """Procura na tabela {nome_tb} e no seu {cache}
  um objeto {obj} com o identificador {ident}, que deve ter a forma 
  "{let}-{ind}" onde {ind} é o índice na tabela.  O objeto 
  deve existir.  Se o objeto não estiver no {cache}, cria o mesmo
  com {obj=def_obj(None,ident,atrs_SQL)} onde {atrs_SQL} são os campos 
  atuais da linha da tabela.
  
  Em qualquer caso, para cada entada {chv:val_novo} no dicionário
  {mods_SQL}, esta função substitui o valor corrente da coluna {chv}
  dessa linha por {val_novo}. As chaves de {mods_SQL} devem ser um
  subconjuto dos nomes das colunas da tabela, como definido em {cols}.
  Em seguida modifica os campos do objeto {obj} na memória chamando
  {def_obj(obj,ident,mods_SQL)}.  
  
  A função devolve o próprio objeto {obj}."""
  return tabela_generica_IMP.atualiza(nome_tb, cache, let, cols, def_obj, ident, mods_SQL)

def busca_por_identificador(nome_tb, cache, let, cols, def_obj, ident):
  """Procura na tabela {nome_tb} e no seu {cache}
  um objeto com o identificador {ident}, que deve ter a forma 
  "{let}-{ind}" onde {ind} é o índice na tabela. 
  
  Mais precisamente, se já existir um objeto {obj} com identificador {ident}
  no dicionario {cache}, pega esse objeto.  Caso contrário
  extrai da tabela {nome_tb} a linha com índice {ind},
  cria um {obj} objeto com {obj=def_obj(None,ident,atrs_SQL)} onde {atrs_SQL} é
  o conteúdo dessa linha, e armazena {obj} no cache.  Nos dois casos, devolve o 
  objeto {obj}.  Se não existir a linha {ind} na tabela, devolve {None}."""
  return tabela_generica_IMP.busca_por_identificador(nome_tb, cache, let, cols, def_obj, ident)

def busca_por_indice(nome_tb, cache, let, cols, def_obj, ind):
  """Mesmo que {busca_por_identificador}, mas quer o indice inteiro {ind} da linha da tabela,
  em vez do identificador do objeto."""
  return tabela_generica_IMP.busca_por_indice(nome_tb, cache, let, cols, def_obj, ind)

def busca_por_campo(nome_tb, let, cols, chave, valor, res_cols):
  """Procura na tabela {nome_tb} objetos que tem o valor {val}
  na coluna de nome {chave}.  A {chave} deve ser o nome de uma
  coluna da tabela, como definido em {cols}.
  
  Se {res_cols} não for {None}, deve ser uma 
  lista ou tupla de nomes de colunas da tabela.  Nesse caso,
  o resultado será uma lista de tuplas, uma para cada linha 
  que satisfaz o critério de busca; onde cada tupla terá os valores
  dessas colunas.
  
  Se {res_cols} for {None}, devolve uma lista com os 
  *identificadores* dos objetos encontrados (não os objetos em si). 
  
  Em qualquer caso, se nenhuma linha satisfizer o critério da busca, 
  devolve uma lista vazia."""
  return tabela_generica_IMP.busca_por_campo(nome_tb, let, cols, chave, valor, res_cols)

def busca_por_semelhanca(nome_tb, let, cols, chaves, valores):
  #@TODO documentar interface
  # Devolve lista de identificadores (não objetos)
  return tabela_generica_IMP.busca_por_semelhanca(nome_tb, let, cols, chaves, valores)

def busca_por_valor(nome_tb, let, cols, chaves, valores):
  """Procura na tabela {nome_tb} objetos cujo o valor {preco}
  na coluna de nome {chave} eh menor que valores.
  
  Devolve uma lista com os *identificadores* dos objetos
  encontrados (não os objetos em si). Se nenhuma linha
  satisfizer o critério da busca, devolve uma lista vazia."""
  return tabela_generica_IMP.busca_por_valor(nome_tb, let, cols, chaves, valores)

def limpa_tabela(nome_tb, cols):
  """Apaga todas as entradas da tabela {nome_tb}, e reinicializa o
  contador de linhas em 0.  Não retorna nenhum resultado.
  Esta função deve ser chamada apenas no início da execução, 
  logo depois de {base_sql.conecta}, pois invalida o cache e 
  todos os objetos na memória que representam linhas desta tabela."""
  tabela_generica_IMP.limpa_tabela(nome_tb, cols)

