# Implementação do módulo {comando_alterar_qtd_de_produto}.

import produto
import compra
import sessao
import gera_html_pag

import tabela_generica
import gera_html_elem
from utils_testes import erro_prog, mostra

def processa(ses, args):
  id_produto = args['id_produto']
  prod = produto.busca_por_identificador(id_produto)
  atrs_produto = produto.obtem_atributos(prod)
  if 'quantidade' in args:
    qtd = float(args['quantidade'])
  else:
    qtd = 1.0
  estoque = float(atrs_produto['estoque'])
  if estoque == 0:
    pag = gera_pagina_de_erro(f"Estoque vazio para o produto {id_produto}")
  elif qtd > estoque:
    qtd = estoque
    pag = gera_pagina_de_erro(f"Só temos {estoque} items do produto {id_produto}")
  else:
    if 'id_compra' in args:
      # Alteração de quantidade de produto em uma compra em aberto:
      id_compra = args['id_compra']
      cpr = compra.busca_por_identificador(id_compra)
      assert compra.obtem_status(cpr) == 'aberto'
      assert ses != None and sessao.obtem_usuario(ses) == compra.obtem_cliente(cpr)
      compra.troca_quantidade(cpr, prod, qtd);
      pag = gera_html_pag.mostra_compra(ses, cpr)
    else:
      # Alteração de quantidade de produto em uma descrição de produto:
      pag = gera_html_pag.mostra_produto(ses, None, prod, qtd)
  return pag

