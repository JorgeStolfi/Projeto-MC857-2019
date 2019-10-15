# Implementação do módulo {comando_menu_ver_carrinho}.

import gera_html_pag
import sessao
import produto
import compra
import sys
from utils_testes import erro_prog, mostra

def processa(ses, args):
  pag = gera_html_pag.mostra_carrinho(ses)
  return pag
