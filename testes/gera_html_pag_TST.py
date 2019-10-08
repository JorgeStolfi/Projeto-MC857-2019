#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# retornam cadeias de caracteres que são 
# páginas completas em HTML5

# !!! Fazer este programa de teste funcionar !!!
# !!! Ele ptecisa chamar cada função da interface pelo menos uma vez, gravando arquivos ".html" separados. !!!

#Interfaces utilizados por este teste
import sys
import tabelas
import usuario
import produto
import gera_html_pag
import base_sql
from produto import ObjProduto

# Cria alguns produtos:

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

prod1 = produto.busca_por_identificador("P-00000001")

# Testes das funções de {gera_html_pag}:

# !!! Consertar !!!

def testa(nome, funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_pag.{nome}.html"."""
  
  prefixo = "testes/saida/gera_html_pag"
  f = open(prefixo + "." + nome + '.html', 'w')
  try:
    res = funcao(*args)
    f.write(res)
  except Exteption as ex:
    msg = "testa(" + nome + "): ** erro = " + str(e) + "\n"
    sys.stderr.write(msg)
    f.write(msg)
  f.close()

testa("principal", gera_html_pag.principal)

testa("produto", gera_html_pag.produto, prod1)

testa("lista_de_produtos", gera_html_pag.lista_de_produtos, [ "P-00000001", "P-00000002" ])

testa("cadastrar_usuario", gera_html_pag.cadastrar_usuario)

conteudo = "Teste do método genérico"

testa("generica", gera_html_pag.generica, conteudo)
