#! /usr/bin/python3

import gera_html_pag, base_produtos

def buscar_produtos(dados):
  busca = dados['busca']
  produtos = base_produtos.busca_por_nome(busca)
  return gera_html_pag.lista_de_produtos(produtos)
  
