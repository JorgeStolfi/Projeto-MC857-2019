#! /usr/bin/python3

import base_sql
import tabela_generica
import sessao; from sessao import ObjSessao
import usuario; from usuario import ObjUsuario
import sys
import identificador

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela:\n")
usuario.inicializa()
colunas_usuarios = usuario.campos()
res = tabela_generica.limpa_tabela("usuarios", colunas_usuarios)
sys.stderr.write("  res(limpa) = " + str(res) + "\n")

sys.stderr.write("Inicializando módulo {sessao}, limpando tabela:\n")
sessao.inicializa()
colunas_sessoes = sessao.campos()
res = tabela_generica.limpa_tabela("sessoes", colunas_sessoes)
sys.stderr.write("  res(limpa) = " + str(res) + "\n")

def valida_estado_sessao(s, sid, usr, ab):
  """ Dado um objeto {s} da classe {ObjSessao}, verifica se os metodos {s.obtem_usuario} e {s.aberta()}
  esta retornando os resultados esperados {usr,ab}."""
  if s.obtem_identiicador() != sid:
    sys.stderr.write('A funcao obtem_identificador deveria ter retornado ' + str(sid) + ', mas retornou ' + str(s.obtem_identificador()) + "\n")
  if s.obtem_usuario() != usr:
    sys.stderr.write('A funcao obtem_usuario deveria ter retornado ' + str(usr) + ', mas retornou ' + str(s.obtem_usuario()) + "\n")
  if s.aberta() != ab:
    sys.stderr.write('A funcao aberta deveria ter retornado ' + str(ab) + ', mas retornou ' + str(s.aberta()) + "\n")
  atrs_esp = { 'usr': usr, 'aberta': ab }
  atrs_s = s.obtem_atributos()
  if len(atrs_s) != len(atrs_s) or atrs['usr'] != usr or atrs['aberta'] != ab:
    sys.stderr.write('A funcao obtem_atributos deveria ter retornado ' + str(atrs_esp) + ', mas retornou ' + str(atrs_s) + "\n")
  return

usr_atrs = {
  "nome": "José Primeiro", 
  "senha": "123456789", 
  "email": "primeiro@gmail.com", 
  "CPF": "123.456.789-00", 
  "endereco": "Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP", 
  "CEP": "13083-418", 
  "telefone": "+55(19)9 9876-5432"
}

usr = usuario.cria(usr_atrs)

s1 = sessao.cria(usr)
sid1 = "S-00000001"
valida_estado_sessao(s1, sid1, usr, True)

s2 = sessao.cria(usr)
sid2 = "S-00000002"
valida_estado_sessao(s2, sid2, usr, True)

s2 = sessao.cria(usr)
sid3 = "S-00000003"
valida_estado_sessao(s3, sid3, usr, True)

sessao.logout(s1)
valida_estado_sessao(s1, sid1, usr, False)

sb = sessao.busca_por_identificador(sid2)
if sb != s2:
  sys.stderr.write('A funcao busca_por_identificador deveria ter retornado ' + str(s2) + ', mas retornou ' + str(sb) + "\n")
