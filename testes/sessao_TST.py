#! /usr/bin/python3

import base_sql
import tabela_de_sessoes
import tabela_de_usuarios
import sessao
import usuario
import sys

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Criando tabela de sessões...\n")
res = tabela_de_sessoes.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

sys.stderr.write("Criando tabela de usuários...\n")
res = tabela_de_usuarios.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

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
# ======================================================================
#! /usr/bin/python3

import tabela_de_sessoes as tb_ses
import tabela_de_usuarios as tb_usr
import sessao; from sessao import ObjSessao
import usuario; from usuario import ObjUsuario

sys.stderr.write("Conectando com base de dados...\n")
bas = base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Criando tabela de usuarios...\n")
res = tb_usr.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

sys.stderr.write("Criando tabela de sessões...\n")
res = tb_ses.cria_tabela(bas)
sys.stderr.write("Resultado = " + str(res) + "\n")

def valida_acrescenta(bas):
    ultimo = bas.indice_inserido()
    ses = sessao.cria(bas)
    novo = tb_ses.acrescenta(ses)
    if novo <= ultimo:
        print("O ID inserido esta incorreto")
        return False
    else:
        print("A entrada inserida está correta")
        return True

def valida_atualiza(bas):
    ult_id = bas.indice_inserido()
    ult_ses = tb_ses.busca_por_identificador(ult_id)
    if ult_ses.aberta() == True:
        ult_ses.logout()
    else:
        usr = usuario.cria(bas)
        ult_ses.login(usr)
    nova_aberta = ult_ses.aberta()
    bas.atualiza(ult_ses)

    res = bas.busca_por_identificador(ult_id)
    if res.aberta() != nova_aberta:
        print("O resultado esta errado")
        return False
    else:
        print("O resultado está correto")
        return True

def valida_cria_tabela(bas):
    cmd = "SELECT * FROM sessao"
    if bas.executa_comando_SELECT("sessoes","indice = 0",('indice'))):
        print("Tabela existe")
        return True
    else:
        print("Tabela nao existe")
        return False

def valida_busca_por_identificador(bas, id_sessao):
    ses = sessao.cria(bas)
    id_sessao = tb_ses.acrescenta(bas, ses)
    res = tb_ses.busca_por_identificador(id_sessao)
    if ses != res:
        print("O resultado esperado era " + str(ses) + " mas foi retornado " + str(res))
        return False
    else:
        print("Foi retornado o resultado esperado")
        return True

valida_busca_por_identificador(bas)
valida_acrescenta(bas)
valida_atualiza(bas)
