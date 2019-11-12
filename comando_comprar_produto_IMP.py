# Implementação do módulo {comando_comprar_produto}.

import gera_html_pag
import compra
import produto
import sessao
import sys
from utils_testes import erro_prog, mostra

def processa(ses, args):
  if ses == None:
    return gera_html_pag.mensagem_de_erro(ses, "Precisa fazer login")
  sys.stderr.write("comando_comprar_produto: args = " + str(args) + "\n")
  id_produto = args['id_produto']
  prod = produto.busca_por_identificador(id_produto)
  quantidade = float(args['quantidade'])
  carrinho = sessao.obtem_carrinho(ses)
  compra.acrescenta_item(carrinho, prod, quantidade)
  pag = gera_html_pag.mostra_compra(ses, carrinho, None)
  return pag
