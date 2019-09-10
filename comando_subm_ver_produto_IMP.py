# Implementação do módulo {comando_subm_ver_produto}.

import gera_html_pag
import produto
import tabela_generica

def processa(bas, sessao, args):
  id_produto = args['id_produto']
  # Considerando prod como objeto da classe Produto
  prod = tabela_generica.busca_por_identificador(bas, id_produto)
  atrs_produto = prod.obtem_atributos()
  if 'quantidade' in args:
    qt = float(args['quantidade'])
    if qt > float(atrs_produto['quantidade']):
        # Maior quantidade disponivel para o produto
        qt = float(atrs_produto['quantidade'])
  else:
    qt = 1.0
  return gera_html_pag.mostra_produto(prod,qt)
