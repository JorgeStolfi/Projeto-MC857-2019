#Implementação de {tabela_de_produtos.py}

import sys
import identificador
import base_sql

def cria_tabela(bas):
  cmd = "CREATE  TABLE produtos (" + \
    " indice int(8) NOT NULL AUTO_INCREMENT," + \
    " descr_curta varchar(12) NOT NULL," + \
    " descr_media varchar(30) NOT NULL," + \
    " descr_longa varchar(60) NOT NULL," + \
    " unidade char(60) NOT NULL," + \
    " preco float(20) NOT NULL," + \
    " PRIMARY KEY indice" + \
    ")"
  bas.executa_comando(cmd)

def busca_por_palavra(bas, pal):
  curta = "descr_curta LIKE '%" + pal + "%'"
  media = "descr_media LIKE '%" + pal + "%'"
  longa = "descr_longa LIKE '%" + pal + "%'"
  cmd = "SELECT indice FROM produtos WHERE" + \
    curta + " OR " + \
    media + " OR " + \
    longa
  produtos_econtrados = bas.executa_comando(cmd)
  print("Produtos encontrados: " + str(produtos_econtrados))

  indices = []
  if (len(produtos_econtrados) == 0):
    return indices

  for produto in produtos_econtrados:
    indices.push(identificador.de_indice("P", produto[0]))

  return indices

def busca_por_identificador(bas, ind_produto):
  ind = identificador.para_indice("P", ind_produto)
  cmd = "SELECT * FROM produtos WHERE indice = " + str(ind)
  produtos_econtrados = bas.executa_comando(cmd)
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

def acrescenta(bas,atrs):
  nomes = "descr_curta,descr_media,descr_longa,unidade,preco"
  valores = \
    atrs["descr_curta"] + ", " + \
    atrs["descr_media"] + ", " + \
    atrs["descr_longa"] + ", " + \
    atrs["unidade"] + ", " + \
    str(atrs["preco"])
  cmd = "INSERT INTO produtos (" + nomes + ") VALUES (" + valores + ");"
  bas.executa_comando(cmd)
  ind = bas.indice_inserido()
  id_produto = identificador.de_indice("P", ind)
  return id_produto
  
def atualiza(bas,ind_produto,atrs):
  ind = identificador.para_indice("P", ind_produto)
  pares = ""
  for ch in ('descr_curta', 'descr_media', 'descr_longa', 'unidade', 'preco'):
      if ch in atrs:
        if pares != "": pares = pares + ", "
        pares = pares + ch + " = " + str(atrs[ch])
  cmd="UPDATE produtos SET " + pares + " WHERE indice = " + str(ind)
  bas.executa_comando(cmd)
