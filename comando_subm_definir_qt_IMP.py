# Implementação do módulo {comando_subm_ver_produto}.

import gera_html_pag
import produto
import tabela_generica

def processa(ss, args):
  id_produto = args['id_produto']
  # Considerando prod como objeto da classe Produto
  prod = produto.busca_por_identificador(bas, id_produto)
  atrs_produto = prod.obtem_atributos()
  if ('quantidade' in args) and ('quantidade' in atrs_produto):
    # No maximo a maior quantidade disponivel para o produto
    qt = min(float(args['quantidade']), float(atrs_produto['quantidade']))
  else:
    qt = 1.0
  carrinho = ss.obtem_carrinho()
  carrinho.acrescenta_item(prod, qt)
  ss.salva_carrinho(carrinho)
  return gera_html_pag.mostra_produto(prod,qt)
