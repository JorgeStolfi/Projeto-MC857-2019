# Implementação do módulo {comando_ver_carrinho}.

import gera_html_pag
import sessao
import produto
import compra
import usuario

import sys
from utils_testes import erro_prog, mostra

def processa(ses, args):
  pag = gera_html_pag.mostra_carrinho(ses, None)

  usr = sessao.obtem_usuario(ses)
  
  admin = usuario.obtem_atributos(usr)['administrador']
  if admin:
    erro_prog("O administrador não pode ver o carrinho")
  
  return pag
