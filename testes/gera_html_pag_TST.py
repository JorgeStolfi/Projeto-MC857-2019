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
import compra
import sessao
import gera_html_pag
import base_sql
from produto import ObjProduto

# Cria alguns produtos:

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()
#usuario teste
usr1 = usuario.busca_por_CPF("123.456.789-00")

#sessao de teste
ses = sessao.busca_por_identificador("S-00000001")

#carrinho de teste

carr = sessao.obtem_carrinho(ses)
cpr_ident = "C-00000003"
cpr = compra.busca_por_identificador(cpr_ident)

#qt teste
qt = 2.3
#produto teste
prod1 = produto.busca_por_identificador("P-00000001")
lista_prod = ["P-00000001", "P-00000002"]

# Testes das funções de {gera_html_pag}:

def testa(nome, funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_pag.{nome}.html"."""
  
  prefixo = "testes/saida/gera_html_pag"
  narq = prefixo + "." + nome + '.html'
  f = open(narq, 'w')
  sys.stderr.write("gravando %s\n" % narq)
  try:
    res = funcao(*args)
    f.buffer.write(res.encode('utf-8'))
  except Exception as ex:
    msg = "testa(" + nome + "): ** erro = " + str(ex) + "\n"
    sys.stderr.write(msg)
    f.buffer.write(msg.encode('utf-8'))
  f.close()

testa("principal", gera_html_pag.principal, ses)

testa("produto", gera_html_pag.mostra_produto, ses, cpr_ident, prod1, qt)

testa("lista_de_produtos", gera_html_pag.lista_de_produtos, ses, lista_prod)

testa("cadastrar_usuario", gera_html_pag.cadastrar_usuario, ses)

conteudo = "Teste do método genérico"

testa("generica", gera_html_pag.generica,ses, conteudo)

testa("mostra_carrinho", gera_html_pag.mostra_carrinho, ses)

testa("mostra_compra_False", gera_html_pag.mostra_compra, ses, cpr)
testa("mostra_compra_True", gera_html_pag.mostra_compra, ses, cpr)

#Depende de outro modulo não impementado
#testa("mostra_usuario", gera_html_pag.mostra_usuario,ses,usr1)

msg = "voce cometeu um erro, rapaz"
testa("mensagem_de_erro", gera_html_pag.mensagem_de_erro, ses, msg)







