# Implementação do módulo {comando_submit_ver_produto}.

import gera_html_pag
import produto
import tabela_generica
from utils_testes import erro_prog, mostra

def processa(ses, args):
  id_produto = args['id_produto']
  # Considerando prod como objeto da classe Produto
  prod = produto.busca_por_identificador(id_produto)
  # !!! Tem que verificar se o produto existe !!!
  atrs_produto = produto.obtem_atributos(prod)
  if ('quantidade' in args) and ('quantidade' in atrs_produto):
    # No maximo a maior quantidade disponivel para o produto
    qt = min(float(args['quantidade']), float(atrs_produto['estoque']))
  else:
    qt = 1.0
  return gera_html_pag.mostra_produto(ses, prod, qt)
