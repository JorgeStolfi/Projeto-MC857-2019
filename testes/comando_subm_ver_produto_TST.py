#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import comando_subm_ver_produto as verprod 
import sys
import produto
import sessao
import base_sql
import tabela_de_produtos
import identificador

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Criando tabela de produtos...\n")
res = tabela_de_produtos.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

usr_atrs = {
  'nome':'',
  'sobrenome':'',
  'nascDt':'',
  'senha':'',
  'email':'',
  'CPF':'',
  'endereco':'',
  'telefone':''
}

usr = usuario.cria(bas,usr_atrs)
s = sessao.cria(bas,usr)

# Cria um produto para teste. 
# Isto testa {produto.cria()} e {tabela_de_produtos.acrescenta()}:
atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
prod = produto.cria(bas,atrs)

obtido = prod.obtem_identificador()

argdict =	{
  'id_produto': obtido, 
  'quantidade': 5.0 }

html = verprod.processa(bas, s, argdict)
html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
