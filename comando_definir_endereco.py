# Este módulo processa a acao do usuário que consiste em alterar o
# endereço de entrega numa página que mostra a decrição detalhada de uma compra.

import comando_definir_endereco_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário aperta o botão "Alterar endereço de
    entrega" na descrição de uma compra. 
    
    O identificador da compra "C-{NNNNNNNN}" deve estar em {args['id_compra']}.
    O novo endereço deve estar em três campos {string} separados de {args}: 
    'endereco_1', 'endereco_2', 'cidade_UF', e o novo CEP deve estar em {args['CEP']}.
    
    Este comando modifica esses atributos do pedido de compra, inclusive na base de dados.
    A função devolve uma página HTML com a descrição completa da compra, mostrando 
    o novo endereço.  
    
    A sessão {ses} não pode ser {None}, e o usuário associado à sessão deve ser o mesmo 
    associado à compra."""
    return comando_definir_endereco_IMP.processa(ses, args)
