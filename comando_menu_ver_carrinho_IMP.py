# Implementação do módulo {comando_menu_ver_carrinho}.

import gera_html_pag
import sessao
from utils_testes import erro_prog, mostra

def processa(ses, args):
  # Chama a funcao que gera a pagina HTML do carrinho a partir da sessao do usuario
  pagina_carrinho = gera_html_pag.mostra_carrinho(ses)
  return pagina_carrinho
