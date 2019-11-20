# Implementação do módulo {comando_buscar_por_intervalo_de_estoque}.

import gera_html_pag
import produto
import compra
import re
import sessao
import usuario
import itens_de_compras
import sys

def processa(ses, args):

  #DEVO Considerar que a funçano produto.busca_por_intervalo_de_estoque já existe
  # lista_de_produtos = produto.produto.busca_por_intervalo_de_estoque(args['quantidade'])

  #Gera uma página genérica enquanto a função produto.produto.busca_por_intervalo_de_estoque não está implementada.
  pag = gera_html_pag.lista_de_compras(ses, [], None)
  return pag
