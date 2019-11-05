#! /usr/bin/python3

# Interfaces usadas por este script:
import gera_html_botao
from gera_html_botao import simples, submit

import usuario
import produto
import sessao

from utils_testes import testa_gera_html as testa
import base_sql
import tabelas
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

prod1 = produto.busca_por_identificador("P-00000001")

# Testes das funções de {gera_html_botao}:

testa(gera_html_botao, simples, "simples_Principal", True, "Principal", 'principal', None, '#60a3bc')

testa(gera_html_botao, simples, "simples_Entrar", True, "Entrar", 'solicitar_form_de_login', None, '#55ee55')

testa(gera_html_botao, simples, "simples_Sair", True, "Sair", 'fazer_logout', None, '#60a3bc')

testa(gera_html_botao, simples, "simples_Cadastrar", True, "Cadastrar", 'solicitar_form_de_dados_de_usuario', None, '#60a3bc')

testa(gera_html_botao, simples, "simples_Meu_Carrinho", True, "Meu Carrinho", 'ver_carrinho', None, '#60a3bc')

testa(gera_html_botao, simples, "simples_OK", True, "OK", 'principal', None, '#55ee55')

testa(gera_html_botao, submit, "submit_Ver_produto", True, "Ver", 'ver_produto', None, '#60a3bc')

testa(gera_html_botao, submit, "submit_Comprar", True, "Comprar", 'comprar_produto', None, '#55ee55')

testa(gera_html_botao, submit, "submit_buscar_produtos", True, "Buscar", 'buscar_produtos', None, '#60a3bc')

testa(gera_html_botao, submit, "submit_Cadastrar", True, "Cadastrar", 'definir_dados_de_usuario', None, '#55ee55')

testa(gera_html_botao, submit, "submit_Alterar_usuario", True, "Cadastrar", 'definir_dados_de_usuario', {'id_usuario': "U-00000001"}, '#55ee55')

testa(gera_html_botao, submit, "submit_Entrar", True, "Entrar", 'fazer_login', None, '#55ee55')
