import sessao; from sessao import Sessao
import usuario; from usuario import Usuario

def valida_estado_sessao(s, usr, ab):
  """ Dado um objeto {s} da classe {Sessao}, verifica se os métodos {s.obtem_usuario} e {s.aberta()}
  esta retornando os resultados esperados {usr,ab}."""
  if s.obtem_usuario() != usr:
    print('O metodo obtem_usuario() deveria ter retornado ' + str(usr) + ', mas retornou ' + str(s.obtem_usuario()))
  else:
    print('O método obtem_usuario() retornou o resultado esperado')
  if s.aberta() != ab:
    print('O metodo aberta() deveria ter retornado ' + str(ab) + ', mas retornou ' + str(s.aberta()))
  else:
    print('O método aberta() retornou o resultado esperado')
    

s = sessao.cria()
valida_estado_sessao(s, None, False)

# usr = Usuario()
s.login(usr)
valida_estado_sessao(s, usr, True)

s.logout()
valida_estado_sessao(s, None, False)
