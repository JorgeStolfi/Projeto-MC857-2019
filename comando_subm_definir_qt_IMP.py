# Implementação do módulo {comando_subm_definir_qt}.

import gera_html_pag
import produto
import tabela_de_produtos

def processa(bas, sessao, args):
  id_produto = args['id_produto']
  prod = tabela_de_produtos.busca_por_identificador(bas, id_produto)
  if 'quantidade' in args:
    qt = float(args['quantidade'])
  else:
    qt = 1.0
  return gera_html_pag.mostra_produto(prod,qt)
