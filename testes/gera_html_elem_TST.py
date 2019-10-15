#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import gera_html_elem
import base_sql
import tabelas
import usuario
import produto
import sessao
import compra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {gera_html_elem}:

def testa(nome,  funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_elem.{nome}.html"."""
  
  prefixo = "testes/saida/gera_html_elem"
  f = open(prefixo + "." + nome + '.html', 'w')
  try:
    res = funcao(*args)
    f.buffer.write(str(res).encode('utf-8'))
  except Exception as ex:
    msg = "testa(" + nome + "): ** erro = " + str(ex) + "\n"
    sys.stderr.buffer.write(str(msg).encode('utf-8'))
    f.buffer.write(str(msg).encode('utf-8'))
  f.close()

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

usr = sessao.obtem_usuario(ses)
assert usr != None
unome = usuario.obtem_atributos(usr)['nome']

prod1 = produto.busca_por_identificador("P-00000001")

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)

testa("span", gera_html_elem.span, "font-family: 'Courier'; font-size: 30px", "Hello World")

testa("div", gera_html_elem.div, "font-family: 'Courier'; font-size: 30px", "Hello World")

testa("paragrafo", gera_html_elem.paragrafo, "font-family: 'Courier'; font-size: 30px", "Hello World")

testa("bloco_texto", gera_html_elem.bloco_texto, "inline-block", "Hello World","Helvetica","18px","bold","30px","center","#000000","#ff8800")

testa("input-1", gera_html_elem.input, "Rotulo", "text", "voltagem", None, "Voltagem Máxima", "testa_input")
testa("input-2", gera_html_elem.input, "Rotulo", "text", "voltagem", "30 V", None, "testa_input")

testa("label-T", gera_html_elem.label, "Rotulo")
testa("label-N", gera_html_elem.label, None)

testa("tabela", gera_html_elem.tabela, (("TB11", "TB12longa", "TB13"), ("TB21", "TB22", "TB23")))

testa("cabecalho-F", gera_html_elem.cabecalho, "TESTE", False)
testa("cabecalho-T", gera_html_elem.cabecalho, "TESTE", True)

testa("rodape", gera_html_elem.rodape)

testa("menu_geral", gera_html_elem.menu_geral, True, unome)

testa("bloco_de_erro", gera_html_elem.bloco_de_erro, "Você errou, meu amigo!")

testa("bloco_de_produto-N-F", gera_html_elem.bloco_de_produto, cpr1_ident, prod1, None, False)
testa("bloco_de_produto-N-T", gera_html_elem.bloco_de_produto, cpr1_ident, prod1, None, True)
testa("bloco_de_produto-10-F", gera_html_elem.bloco_de_produto, cpr1_ident, prod1, 10, False)
testa("bloco_de_produto-10-T", gera_html_elem.bloco_de_produto, cpr1_ident, prod1, 10, True)

testa("bloco_de_compra-F", gera_html_elem.bloco_de_compra, cpr1, False)
testa("bloco_de_compra-T", gera_html_elem.bloco_de_compra, cpr1, True)
