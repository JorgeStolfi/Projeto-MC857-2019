# Implementação do módulo {comando_subm_ver_produto}.

import gera_html_pag
import produto
import tabela_generica

def processa(ses, args):
  id_produto = args['id_produto']
  # Considerando prod como objeto da classe Produto
  prod = produto.busca_por_identificador(bas, id_produto)
  atrs_produto = prod.obtem_atributos()
  if 'quantidade' in args:
    qt = float(args['quantidade'])
  else:
    qt = 1.0
  estoque = float(atrs_produto['estoque'])
  # !!! Se o estoque for zero, deveria retornar página de erro. !!! 
  if qt > estoque:
    # No maximo a maior quantidade disponivel para o produto
    qt = estoque
  carrinho = sessao.obtem_carrinho(ses)
  compra.acrescenta_item(carrinho, prod, qt)
  return gera_html_pag.mostra_produto(prod, qt)
