#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# retornam cadeias de caracteres que são 
# páginas completas em HTML5

#Interfaces utilizados por este teste
import sys
import tabela_de_produtos as tb_prod
import tabela_de_usuarios as tb_usr
import gera_html_pag
import base_sql
import produto
from produto import ObjProduto

# Cria alguns produtos:

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB/MC857",None,None)
assert res == None

sys.stderr.write("Criando tabela de usuarios...\n")
res = tb_usr.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

sys.stderr.write("Criando tabela de produtos...\n")
res = tb_prod.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

atrs_prod1 = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho'
}
prod1 = produto.cria(bas,atrs_prod1)

atrs_prod2 = {
  'descr_curta': "Ferroada",
  'descr_media': "Espada élfica fabricada na cidade de Gondolin.",
  'descr_longa': "Fabricante: Gondolin Ferreiros SA\nOrigem: Gondolin\Dono Original: Bilbo\n",
  'preco': 2000.00,
  'unidade': '1 espada' 
}
prod2 = produto.cria(bas,atrs_prod2)

# Testes das funções de {gera_html_pag}:

def testa(nome,funcao,*args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_pag.{nome}.html"."""
  
  prefixo = "saida/gera_html_pag"
  f = open(prefixo + "." + nome + '.html', 'w')
  try:
    res = funcao(*args)
    f.write(res)
  except Exteption as ex:
    msg = "testa(" + nome + "): ** erro = " + str(e) + "\n"
    sys.stderr.write(msg)
    f.write(msg)
  f.close()

testa("entrada", gera_html_pag.entrada)

testa("produto", gera_html_pag.produto,prod1)

testa("lista_de_produtos", gera_html_pag.lista_de_produtos, [ prod1, prod2 ])

testa("cadastrar_usuario", gera_html_pag.cadastrar_usuario)

conteudo = "Teste do método genérico"

testa("generica", gera_html_pag.generica, conteudo)
