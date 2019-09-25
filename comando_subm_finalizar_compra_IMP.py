# Implementação do módulo {comando_subm_finalizar_compra_IMP}

import gera_html_pag
import compra
import produto
import sessao
import sys

def processa(ses, args):
    sys.stderr.write("finalizando compra!")
    carrinho = sessao.obtem_carrinho(ses)
    compra.calcula_total(carrinho)
    # envia para venda
    compra.fecha_compra(carrinho)
    sessao.muda_atributos(ses, carrinho)
    new_carrinho = sessao.obtem_carrinho(ses)
    return gera_html_pag.compra(carrinho)
     
