import gera_html_pag, tabela_de_produtos

def buscar_produtos(dados):
  busca = dados['busca']
  produtos = tabela_de_produtos.busca_por_nome(busca)
  return gera_html_pag.lista_de_produtos(produtos)
  
