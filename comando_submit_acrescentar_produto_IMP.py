# Implementação do módulo {comando_submit_cadastrar_usuario}.

import produto; from produto import ObjProduto
import gera_html_pag
from utils_testes import erro_prog, mostra

def processa(ses, args):
  conteudo = ""
  prod = produto.cria(args)

  # Verifica se o usuário foi criado corretamente 
  # e retorna uma página de acordo com o resultado:
  if type(prod) is ObjProduto:
    conteudo = gera_html_pag.mostra_produto(ses,prod=prod,qt=1)
  else:
    erro = "Erro ao gerar novo usuário"
    conteudo = gera_html_pag.mensagem_de_erro(erro)
  return conteudo
