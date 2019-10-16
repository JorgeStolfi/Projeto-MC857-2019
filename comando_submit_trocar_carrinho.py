# Este módulo processa o comando usuário tem mais de um carrinho e
# quer trocar o carrinho de compras por outro pedido de compras que
# está em aberto e associado a este usuário.

import comando_submit_trocar_carrinho_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário {usr} logado na sessão {ses}
    aperta o botao "Trocar carrinho" na tela do carrinho selecionando uma
    compra {cpr}.

    O identificador "C-{NNNNNNNN}" do novo pedido de compra {cpr} desejado
    deve estar em {args['id_compra']}.

    A função retorna uma página HTML que mostra os itens no novo carrinho
    carrinho {cpr} dessa sessão.

    A sessão não pode ser {None} e deve estar aberta, e o usuário {usr} deve ser
    dono do pedido de compras {cpr}."""
    return comando_submit_trocar_carrinho_IMP.processa(ses, args)
