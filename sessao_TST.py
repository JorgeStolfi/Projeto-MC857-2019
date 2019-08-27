import sessao
import usuario

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
    

s = sessao.cria()

valida_estado_sessao(s, None, False)

usr = usuario.cria({
  'nome':'',
  'sobrenome':'',
  'nascDt':'',
  'senha':'',
  'email':'',
  'CPF':'',
  'endereco':'',
  'telefone':''
})

s.login(usr)
valida_estado_sessao(s, usr, True)

s.logout()
valida_estado_sessao(s, None, False)
