#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import gera_html_form
import sys
import usuario
import identificador

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {gera_html_form}:

def testa(nome,  funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_form.{nome}.html"."""
  
  prefixo = "testes/saida/gera_html_form"
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

usr1 = sessao.obtem_usuario(ses)
assert usr1 != None

prod1_ident = "P-00000001"
prod1 = produto.busca_por_identificador(prod1_ident)
assert prod1 != None

prod2_ident = "P-00000002"
prod2 = produto.busca_por_identificador(prod2_ident)
assert prod2 != None

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)
assert cpr1 != None

testa("buscar_produtos", buscar_produtos)

testa("ver_produto", ver_produto, prod1_ident, 3)

testa("comprar_produto", comprar_produto, cpr1_ident, prod1_ident, 3)

testa("alterar_quantidade", alterar_quantidade, cpr1_ident, prod1_ident, 5)

testa("ver_compra", ver_compra, cpr1_ident)

testa("fechar_compra", fechar_compra, cpr1_ident)

testa("entrar", entrar)

testa("cadastrar_usuario", cadastrar_usuario)

testa("alterar_usuario", alterar_usuario, usr1)
