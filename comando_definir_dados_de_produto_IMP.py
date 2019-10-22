# Implementação do módulo {comando_definir_dados_de_produto}.

import produto; from produto import ObjProduto
import gera_html_pag
from utils_testes import erro_prog, mostra

def processa(ses, args):
  prod = produto.cria(args)
  # Verifica se o produto foi criado corretamente 
  # e retorna uma página de acordo com o resultado:
  if prod != None and type(prod) is ObjProduto:
    qtd = 1
    pag = gera_html_pag.mostra_produto(ses, None, prod, qtd)
  else:
    erro = "Erro ao gerar novo usuário"
    pag = gera_html_pag.mensagem_de_erro(erro)
  return pag
