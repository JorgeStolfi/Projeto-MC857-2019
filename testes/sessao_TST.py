#! /usr/bin/python3

import sessao
import usuario
import base_sql

def valida_estado_sessao(s, usr, ab):
  """ Dado um objeto {s} da classe {ObjSessao}, verifica se os metodos {s.obtem_usuario} e {s.aberta()}
  esta retornando os resultados esperados {usr,ab}."""
  if s.obtem_usuario() != usr:
    print('O metodo obtem_usuario() deveria ter retornado ' + str(usr) + ', mas retornou ' + str(s.obtem_usuario()))
  else:
    print('O metodo obtem_usuario() retornou o resultado esperado')
  if s.aberta() != ab:
    print('O metodo aberta(ObjSessao) deveria ter retornado ' + str(ab) + ', mas retornou ' + str(s.aberta()))
  else:
    print('O metodo aberta() retornou o resultado esperado')
    
bas = base_sql.conecta("DB/MC857",None,None)    

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
s = sessao.cria(bas,usr)

valida_estado_sessao(s, usr, True)

s.logout(bas)
valida_estado_sessao(s, None, False)
