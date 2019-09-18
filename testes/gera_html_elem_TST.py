#! /usr/bin/python3

#testes para gera_html_elem
import sys
import gera_html_elem

import produto
import usuario

# Cria produto e usuario para testes:

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB/MC857",None,None)
assert res == None

sys.stderr.write("Criando tabela de usuarios...\n")
res = tb_usr.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

sys.stderr.write("Criando tabela de produtos...\n")
res = tb_prod.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

atrs_prod = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'estoque': 500,
  'unidade': '1 aparelho'
}
prod = produto.cria(bas, atrs_prod)

# Testes das funções de {gera_html_elem}:

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


testa(cabecalho, gera_html_elem.cabecalho, "TESTE")

testa(rodape, gera_html_elem.rodape)

testa(menu_geral, gera_html_elem.menu_geral)

testa(bloco_texto, gera_html_elem.bloco_texto, "Hello World","Helvetica","18px","30px","center","#000000","#ff8800")

testa(bloco_de_produto, gera_html_elem.bloco_de_produto, prod)

testa(formulario_login, gera_html_elem.formulario_login, "800px","600px","solid","30px","35px")
