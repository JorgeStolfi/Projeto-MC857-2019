# Implementação do módulo {comando_subm_ver_produto}.

import gera_html_pag
import produto
import tabela_generica
import gera_html_elem

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
  if estoque == 0:
      return gera_pagina_de_erro(f"Estoque vazio para o produto:{id_produto}")
  if qt > estoque:
    # No maximo a maior quantidade disponivel para o produto
    qt = estoque
  carrinho = sessao.obtem_carrinho(ses)
  compra.acrescenta_item(carrinho, prod, qt)
  return gera_html_pag.mostra_produto(prod, qt)

 def gera_pagina_de_erro(erro):
     cabe = gera_html_elem.cabecalho("Projeto MC857A 2019-2s")
     menu = gera_html_elem.menu_geral()
     roda = gera_html_elem.rodape()
     conteudo = f"<h1>{erro}</h1>"
     return cabe + "\n" + menu + "\n" + conteudo + "\n" + roda
