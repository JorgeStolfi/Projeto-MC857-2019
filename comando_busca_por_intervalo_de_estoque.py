# Este módulo processa o comando usuário para mostrar
#  uma lista doss produtos que possuem estoque menor
#  ou igual a um determinado valor que o usuário digita.

import comando_busca_por_intervalo_de_estoque_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário {usr} logado na sessão {ses}
    aperta o botao "Estoque" na tela do produto.

    A função retorna uma página HTML que mostra uma lista de produtos, os quais
    possuem estoque menor ou igual a um determinado valor que o usuário digitou.
    """
    return comando_busca_por_intervalo_de_estoque_IMP.processa(ses, args)
