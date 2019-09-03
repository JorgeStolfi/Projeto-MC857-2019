#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# retornam cadeias de caracteres que são 
# páginas completas em HTML5

#Interfaces utilizados por este teste
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import gera_html_pag
import base_sql
import produto
from produto import ObjProduto


f = open("saida/gera_html_pag_TST.txt", "w+")

f.write("Testando a entrada\n")
try:
    entrada = gera_html_pag.entrada()

    f.write("Entrada executado\n")
    f.write(entrada)
except Exception as e:
    f.write("Erro ao executar entrada\n")
    f.write(str(e))

f.write("\n\n\n***********************\n")
f.write("Testando produto\n")

#Criação do produto copiado do produto_TST
try:
    bas = base_sql.conecta("DB",None,None)

    atrs = {
    'descr_curta': "Escovador de ouriço",
    'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
    'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
    'preco': 120.00,
    'unidade': '1 aparelho' }
    prod = produto.cria(bas,atrs)

    html_produto = gera_html_pag.produto(prod)

    f.write("Produto executado\n")
    f.write(html_produto)
except Exception as e:
    f.write("Erro ao executar produto\n")
    f.write(str(e))

f.write("\n\n\n***********************\n")
f.write("Testando lista_de_produtos\n")
try:
    bas = base_sql.conecta("DB",None,None)

    atrs = {
    'descr_curta': "Escovador de ouriço",
    'descr_media': "Escovador para ouriços ou porcos-espinho portátil em aço inox e marfim orgânico, com haste elongável, cabo de força, 20 acessórios, e valise.",
    'descr_longa': "Fabricante: Ouricex SA\nOrigem: Cochinchina\nModelo: EO-22\nTensão: 110-230 V\nPotência: 1500 W\nDimensões: 300 x 200 x 3000 mm",
    'preco': 120.00,
    'unidade': '1 aparelho' }
    prod1 = produto.cria(bas,atrs)
    atrs = {
    'descr_curta': "Ferroada",
    'descr_media': "Espada élfica fabricada na cidade de Gondolin.",
    'descr_longa': "Fabricante: Gondolin Ferreiros SA\nOrigem: Gondolin\Dono Original: Bilbo\n",
    'preco': 2000.00,
    'unidade': '1 espada' }
    prod1 = produto.cria(bas,atrs)
    prods = []
    prods.append(prod1)
    prods.append(prod2)
    
    html_produtos = gera_html_pag.lista_de_produtos(prods)
    f.write("lista_de_produtos executado\n")
    f.write(html_produtos)
except Exception as e:
    f.write("Erro ao executar lista_de_produtos\n")
    f.write(str(e))

f.write("\n\n\n***********************\n")
f.write("Testando cadastrar_usuario\n")
try:
    cadastrar_usuario = gera_html_pag.cadastrar_usuario()

    f.write("cadastrar_usuario executado\n")
    f.write(cadastrar_usuario)
except Exception as e:
    f.write("Erro ao executar cadastrar_usuario\n")
    f.write(str(e))

f.write("\n\n\n***********************\n")
f.write("Testando generica\n")
try:
    conteudo = "Teste do método genérico"
    generica = gera_html_pag.generica(conteudo)

    f.write("generica executado\n")
    f.write(generica)
except Exception as e:
    f.write("Erro ao executar generica\n")
    f.write(str(e))


f.close()
