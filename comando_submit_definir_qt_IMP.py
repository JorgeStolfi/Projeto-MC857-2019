# Implementação do módulo {comando_submit_ver_produto}.

import gera_html_pag
import produto
import tabela_generica
import gera_html_elem
from utils_testes import erro_prog, mostra

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
  if estoque == 0:
      return gera_pagina_de_erro(f"Estoque vazio para o produto:{id_produto}")
  if qt > estoque:
    # !!! Deveria dar mensagem de erro -- cliente que quer 3 pode não querer 2 !!!
    # No maximo a maior quantidade disponivel para o produto
    qt = estoque
  carrinho = sessao.obtem_carrinho(ses)
  compra.acrescenta_item(carrinho, prod, qt)
  return gera_html_pag.mostra_produto(ses, prod, qt)
