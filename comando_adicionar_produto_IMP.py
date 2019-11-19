# Implementação do módulo {comando_adicionar_produto}.

import produto
import sessao
import gera_html_pag

def processa(ses, args):
  prod = produto.cria(args)
  return gera_html_pag.mostra_produto(ses, None, prod, 1, None)

