# Implementação do módulo {comando_submit_comprar_produto}.

import gera_html_pag
import compra
import produto
import sessao
import sys
from utils_testes import erro_prog, mostra

def processa(ses, args):
  
  sys.stderr.write("comando_submit_comprar_produto: args = " + str(args) + "\n")
  id_produto = args['id_produto']
  prod = produto.busca_por_identificador(id_produto)
  quantidade = float(args['quantidade'])
  # carrinho = sessao.obtem_carrinho(ses)
  carrinho = compra.busca_por_identificador("C-00000001") # !!! Temporário enquanto {sessao.obtem_carrinho} não existe.
  compra.acrescenta_item(carrinho, prod, quantidade)
  return gera_html_pag.mostra_compra(ses, carrinho)
