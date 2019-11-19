# Este módulo processa a acao do usuário que consiste em adicionar
# um produto a partir dos seus atributos

import comando_adicionar_produto_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário aperta o botão 
    "adicionar" no formulário de acrescentar produto."""
    return comando_adicionar_produto_IMP.processa(ses, args)

