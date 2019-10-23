# Este módulo processa o acionamento do botão "Escolher meio de pagamento" num formulário de compra.

import comando_solicitar_form_de_meio_de_pagamento_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Escolher/Alterar meio de pagamento" 
  na descrição de uma compra {cpr} que está sendo finalizada.
  
  O identificador "C-{NNNNNNNN}" da compra estará em {args['id_compra']}.  A compra deve
  estar no estado 'aberto', e seu endereço de entrega (incluindo o CEP) deve estar definido.
  A sessão {ses} deve estar aberta, e o usuário da sessão deve ser o mesmo
  associado à compra {cpr}.
  
  Retorna uma página HTML {pag}, contendo o formulario de dados para escolher o meio de pagamento 
  (Visa, PayPal, boleto, etc), que deve ser preenchido pelo usuário.  O formulário mostrará o
  identificador da compra e o preço total a pagar (incluindo frete)."""
  return comando_solicitar_form_de_meio_de_pagamento_IMP.processa(ses, args)

