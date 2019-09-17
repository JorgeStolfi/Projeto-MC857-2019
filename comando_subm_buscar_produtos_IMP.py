# Implementação do módulo {comando_subm_buscar_produtos}.

import gera_html_pag, tabela_de_produtos

def processa(bas, sessao, args):
  texto_busca = args['cond']
  # busca produtos de acordo com o texto digitado (cond)
  prods = tabela_de_produtos.busca_por_nome(bas, texto_busca)
  # gera página html com os produtos encontrados
  return gera_html_pag.lista_de_produtos(prods)
  
