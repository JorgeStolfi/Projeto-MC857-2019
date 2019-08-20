import sessao
from sessao import Sessao

# import usuario
# from usuario import Usuario

def valida_estado_sessao(s, esta_aberta):
    """
        Verifica se o valor do método aberta() esta retornando o resultado esperado

        Parametros
            -----------
            s : Sessao
                Objeto da classse Sessao, que está sendo testado
            esta_aberta : Boolean
                Se a sessao deve estar aberta, valor deve ser True, caso contrário, False
    """
    if s.aberta() != esta_aberta:
        print('O metodo aberta() deveria ter retornado ' + str(esta_aberta) + ', mas retornou ' + str(s.aberta()))
    else:
        print('O método aberta() retornou o resultado esperado')
    

s = sessao.cria()
valida_estado_sessao(s, False)

#TODO: Descomentar esse teste quando a classe Usuario estiver corrigida
# usr = Usuario()
# s.login(usr)
# valida_estado_sessao(s, True)

s.logout()
valida_estado_sessao(s, False)