#Implementação de {tabela_de_produtos.py}

import sys
import identificador
import base_sql

def cria_tabela(bas):
  campos = \
    " indice integer NOT NULL PRIMARY KEY," + \
    " descr_curta varchar(60) NOT NULL," + \
    " descr_media varchar(128) NOT NULL," + \
    " descr_longa text NOT NULL," + \
    " unidade char(60) NOT NULL," + \
    " preco float(20) NOT NULL"
  bas.executa_comando_CREATE_TABLE("produtos", campos)

def busca_por_palavra(bas, pal):
  curta = "descr_curta LIKE '%" + pal + "%'"
  media = "descr_media LIKE '%" + pal + "%'"
  longa = "descr_longa LIKE '%" + pal + "%'"
  cond = \
    curta + " OR " + \
    media + " OR " + \
    longa
  produtos_econtrados = bas.executa_comando_SELECT("produtos", cond, ('indice'))
  print("Produtos encontrados: " + str(produtos_econtrados))

  ids = []
  for produto in produtos_econtrados:
    ids.push(identificador.de_indice("P", produto[0]))

  return ids

def busca_por_identificador(bas, ind_produto):
  ind = identificador.para_indice("P", ind_produto)
  cond = "indice = " + str(ind)
  produtos_econtrados = bas.executa_comando_SELECT("produtos", cond, ('indice'))
  print("Produtos encontrados: " + str(produtos_econtrados))

  atrs = {}
  if (len(produtos_econtrados) == 0):
    return atrs
  
  produto = produtos_econtrados[0]
  sys.stderr.write(str(produto) + "\n")

  atrs["descr_curta"] = produto[0]
  atrs["descr_media"] = produto[1]
  atrs["descr_longa"] = produto[2]
  atrs["unidade"] = produto[3]
  atrs["preco"] = produto[4]

  return atrs

def acrescenta(bas, atrs):
  ind = bas.executa_comando_INSERT("produtos", atrs)
  id_produto = identificador.de_indice("P", ind)
  return id_produto
  
def atualiza(bas, id_produto, atrs):
  ind = identificador.para_indice("P", id_produto)
  bas.executa_comando_UPDATE("produtos", ind, atrs)
