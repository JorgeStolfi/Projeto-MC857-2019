#! /usr/bin/python3

import sessao
import usuario
import base

def valida_estado_sessao(s, usr, ab):
  """ Dado um objeto {s} da classe {Sessao}, verifica se os metodos {s.obtem_usuario} e {s.aberta()}
  esta retornando os resultados esperados {usr,ab}."""
  if s.obtem_usuario() != usr:
    print('O metodo obtem_usuario() deveria ter retornado ' + str(usr) + ', mas retornou ' + str(s.obtem_usuario()))
  else:
    print('O metodo obtem_usuario() retornou o resultado esperado')
  if s.aberta() != ab:
    print('O metodo aberta(Sessao) deveria ter retornado ' + str(ab) + ', mas retornou ' + str(s.aberta()))
  else:
    print('O metodo aberta() retornou o resultado esperado')
    
bas = base.conecta("DB",None,None)    

s = sessao.cria(bas)

valida_estado_sessao(s, None, False)

usr_atrs = {
  'nome':'',
  'sobrenome':'',
  'nascDt':'',
  'senha':'',
  'email':'',
  'CPF':'',
  'endereco':'',
  'telefone':''
}
usr = usuario.cria(bas,usr_atrs)

s.login(usr)
valida_estado_sessao(s, usr, True)

s.logout()
valida_estado_sessao(s, None, False)
