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

# Testes das funções de {gera_html_botao}:

# !!! Consertar !!!

def testa(nome,funcao,*args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_botao.{nome}.html"."""
  
  prefixo = "testes/saida/gera_html_botao"
  narq = prefixo + "." + nome + '.html'
  f = open(narq, 'w')
  sys.stderr.write("gravando %s\n" % narq)
  cabe = \
    "<!doctype html>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n"
  roda = \
    "</body>\n" + \
    "</html>\n"  
  f.write(cabe)
  try:
    res = funcao(*args)
    f.buffer.write(res.encode('utf-8'))
  except Exception as ex:
    msg = "testa(" + nome + "): ** erro = " + str(ex) + "\n"
    sys.stderr.write(msg)
    f.buffer.write(msg.encode('utf-8'))
  f.write(roda)
  f.close()


testa("principal", gera_html_botao.principal)

testa("menu_entrar", gera_html_botao.menu_entrar)

testa("menu_sair", gera_html_botao.menu_sair)

testa("menu_cadastrar", gera_html_botao.menu_cadastrar)

testa("menu_carrinho", gera_html_botao.menu_carrinho)

testa("erro_ok", gera_html_botao.erro_ok)

testa("submit_ver_produto", gera_html_botao.submit_ver_produto)

testa("submit_comprar_produto", gera_html_botao.submit_comprar_produto)

testa("submit_buscar_produtos", gera_html_botao.submit_buscar_produtos)

testa("submit_cadastrar_usuario", gera_html_botao.submit_cadastrar_usuario)

testa("submit_entrar", gera_html_botao.submit_entrar)
