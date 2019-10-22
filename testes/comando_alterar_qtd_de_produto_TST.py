#! /usr/bin/python3

# Interfaces usadas por este script:
import sys

import comando_alterar_qtd_de_produto
from comando_alterar_qtd_de_produto import processa

import base_sql
import tabelas
import usuario
import sessao
import compra
from utils_testes import testa_gera_html

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Teste de alteração de quantidade do produto fora de compra:

ses1 = sessao.busca_por_identificador("S-00000001")
args1 = {"quantidade": "3","id_produto": "P-00000002"}

testa_gera_html(comando_alterar_qtd_de_produto, processa, "sem_compra", False, ses1, args1)

# Teste de alteração de quantidade de um produto em um carrinho:

ses2 = sessao.busca_por_identificador("S-00000001")
cpr2 = compra.busca_por_identificador("C-00000001")
args2 = {"quantidade": "3", "id_compra": "C-00000001", "id_produto": "P-00000003"}

testa_gera_html(comando_alterar_qtd_de_produto, processa, "com_compra", False, ses2, args2)
