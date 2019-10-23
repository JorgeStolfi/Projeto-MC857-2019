# Este módulo processa o comando usuário para mostrar
#  uma lista das compras que incluem o produto. Se o
#  usuário corrente for administrador, buscar todas as
# compras de todos os usuários. Senão, mostrar apenas as
# compras do usuário corrente.

import comando_busca_compras_por_produto_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário {usr} logado na sessão {ses}
    aperta o botao "Ver compras com de produto" na tela do produto.

    O identificador "P-{NNNNNNNN}" do produto {pdt} desejado
    deve estar em {args['id_produto']}.

    A função retorna uma página HTML que mostra os as compras do que contém
    o produto. Se o usuário é um admin é retornado a lista de todas as compras
    deste produto, caso contrário, apenas as compras para o cliente.

    A sessão não pode ser {None} e deve estar aberta"""
    return comando_busca_compras_por_produto_IMP.processa(ses, args)
