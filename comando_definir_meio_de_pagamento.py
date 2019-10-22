# Este módulo processa o acionamento do botão "Pagar" num formulário de escolher meio de pagamento.

import comando_definir_meio_de_pagamento_IMP

def processa(ses, args):
  """Esta função será chamada quando um usuário acionar o botão "Pagar" 
  no formulário de escolher meio de pagamento, para uma compra {cpr} que está sendo 
  fechada.
  
  Retorna uma página HTML {pag}, contendo o formulario de dados para escolher o meio de pagamento 
  (Visa, PayPal, boleto, etc), que deve ser preenchido pelo usuário.  O formulário mostrará o
  identificador da compra e o preço total a pagar (incluindo frete).
  
  O identificador "C-{NNNNNNNN}" da compra estará em {args['id_compra']}.
  
  A sessão {ses} deve estar aberta, e o usuário da sessão deve ser o mesmo
  associado à compra {cpr}."""
  return comando_definir_meio_de_pagamento_IMP.processa(ses, args)

