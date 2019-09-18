#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import comando_subm_ver_produto as verprod 
import sys
import produto
import sessao
import usuario
import base_sql
import identificador

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {produto}, limpando tabela: \n")
produto.inicializa(True)

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB/MC857",None,None)
assert res == None

usr_atrs = {
  "nome": "José Primeiro", 
  "senha": "123456789", 
  "email": "primeiroooo@gmail.com", 
  "CPF": "123.456.666-00", 
  "endereco": "Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP", 
  "CEP": "13083-418", 
  "telefone": "+55(19)9 9876-5432"
}

usr = usuario.cria(usr_atrs)
s = sessao.cria(usr)

# Cria um produto para teste. 
# Isto testa {produto.cria()} e {tabela_de_produtos.acrescenta()}:
atrs = {
  'descr_curta': "Escovador de ouriço",
  'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
  'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
  'preco': 120.00,
  'unidade': '1 aparelho' }
prod = produto.cria(atrs)

obtido = prod.obtem_identificador()

argdict =	{
  'id_produto': obtido, 
  'quantidade': 5.0 }

html = verprod.processa(s, argdict)
html = html + "\n" # In case the fragment does not end with newline.

sys.stdout.buffer.write(html.encode('utf-8'))
