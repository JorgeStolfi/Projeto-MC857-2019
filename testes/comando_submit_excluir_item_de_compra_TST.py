#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

from comando_submit_excluir_item_de_compra import processa
import base_sql
import tabelas
import usuario
import produto
import sessao
import compra

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()
sys.stderr.write("Objetos criados...\n")

sys.stderr.write("Obtendo sessão por identificador...\n")
ses1 = sessao.busca_por_identificador("S-00000001")
sys.stderr.write("Sessao: " + str(ses1) + "\n")

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)
sys.stderr.write("cpr1 = " + str(cpr1) + "\n")
cpr1_itens = compra.obtem_itens(cpr1)
sys.stderr.write("cpr1_itens = " + str(cpr1_itens) + "\n")

# Produto que existe em {cpr1}:
prod1_ident = "P-00000001"
prod1 = produto.busca_por_identificador(prod1_ident)
sys.stderr.write("prod1 = " + str(prod1) + "\n")
assert prod1 != None
assert compra.obtem_quantidade(cpr1, prod1) != 0

# Produto que não existe em {cpr1}:
prod2_ident = "P-00000004"
prod2 = produto.busca_por_identificador(prod2_ident)
sys.stderr.write("prod2 = " + str(prod2) + "\n")
assert prod2 != None
assert compra.obtem_quantidade(cpr1, prod2) == 0

def testa(nome, funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/comando_submit_excluir_item_de_compra.{nome}.html"."""
  
  prefixo = "testes/saida/comando_submit_excluir_item_de_compra"
  f = open(prefixo + "." + nome + '.html', 'w')
  try:
    res = funcao(*args)
    f.buffer.write(str(res).encode('utf-8'))
  except Exception as ex:
    msg = "testa(" + nome + "): ** erro = " + str(ex) + "\n"
    sys.stderr.buffer.write(str(msg).encode('utf-8'))
    f.buffer.write(str(msg).encode('utf-8'))
  f.close()

testa("excluir_existe", processa, ses1, { 'id_produto': prod1_ident, 'id_compra': cpr1_ident})

testa("excluir_nao_existe", processa, ses1, { 'id_produto': prod2_ident, 'id_compra': cpr1_ident})
