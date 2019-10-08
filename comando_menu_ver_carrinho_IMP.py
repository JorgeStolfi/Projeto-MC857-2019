# Implementação do módulo {comando_menu_ver_carrinho}.

import gera_html_pag
import sessao
import produto
import compra
import sys
from utils_testes import erro_prog, mostra

def processa(ses, args):
  # Chama a funcao que gera a pagina HTML do carrinho a partir da sessao do usuario
  
  #TEMPORARIO ATE ARRUMAR O gera_html_pag.mostra_carrinho
  #pagina_carrinho = gera_html_pag.mostra_carrinho(ses)
  compra = sessao.obtem_carrinho(ses)

  pagina_carrinho = "<html><table><tbody>"
  pagina_carrinho = pagina_carrinho + "<tr><td>Produto</td><td>Quantidade</td><td>Preço</td></tr>"
  for prod, qt, prc in compra.itens:
    atrs = produto.obtem_atributos(prod)
    d_curta = atrs['descr_curta']
    pagina_carrinho = pagina_carrinho + "<tr><td>"+d_curta+"</td><td>"+str(qt)+"</td><td>"+str(prc)+"</td></tr>"

  pagina_carrinho = pagina_carrinho + "</tbody></table></html>"
  
  return pagina_carrinho
