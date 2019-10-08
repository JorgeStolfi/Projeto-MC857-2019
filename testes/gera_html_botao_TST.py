#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import gera_html_botao
import base_sql
import tabelas
import usuario
import produto
import sessao

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

prod1 = produto.busca_por_identificador("P-00000001")

# Testes das funções de {gera_html_elem}:

# !!! Consertar !!!

def testa(nome,funcao,*args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_elem.{nome}.html"."""
  
  prefixo = "saida/gera_html_elem"
  f = open(prefixo + "." + nome + '.html', 'w')
  try:
    res = funcao(*args)
    f.write(res)
  except Exteption as ex:
    msg = "testa(" + nome + "): ** erro = " + str(e) + "\n"
    sys.stderr.write(msg)
    f.write(msg)
  f.close()


testa("principal", gera_html_botao.principal)

# !!! Testar os outros botãoes !!! 
