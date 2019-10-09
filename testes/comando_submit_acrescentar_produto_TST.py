#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_submit_acrescentar_produto
import base_sql
import tabelas
import usuario
import sessao

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

sys.stderr.write("Criando sessao...\n")
ses1 = sessao.busca_por_identificador("S-00000001")

#cria descricao do produto
args1 = { 'descr_curta': 'Cabideiro' , 'descr_media':'cabideiro com capacidade para 420 cabides',  'descr_longa':'lindo cabideiro com suporte para 420 cabides, ideal para voce, seus pais, filhos, irmaos , tios e cachorros', 'unidade':'01 (hum) cabideiro', 'preco':69.0, 'estoque':1, 'imagem':'155951.png'}

sys.stderr.write("Criando o produto com as seguinte informaceos:\n")
sys.stderr.write(str(args1)+'\n')

html = comando_submit_acrescentar_produto.processa(ses1, args1)
html = html + "\n"

sys.stdout.buffer.write(html.encode('utf-8'))
