#! /usr/bin/python3

import base_sql
import tabela_generica
import sessao
import usuario
import identificador
import utils_testes
import sys

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela:\n")
usuario.inicializa(True)

sys.stderr.write("Inicializando módulo {sessao}, limpando tabela:\n")
sessao.inicializa(True)

# ----------------------------------------------------------------------
# Cria um usuário para teste:
usr1_atrs = {
  "nome": "José Primeiro", 
  "senha": "123456789", 
  "email": "primeiro@gmail.com", 
  "CPF": "123.456.789-00", 
  "endereco": "Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP", 
  "CEP": "13083-418", 
  "telefone": "+55(19)9 9876-5432"
}

usr1 = usuario.cria(usr1_atrs)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_sessao(rotulo, ses, indice, ident, usr, abrt):
  """Testes básicos de consistência do objeto {ses} da classe {ObjSessao}, dados {indice},
  {ident} e {atrs} esperados."""
  global ok_global
  atrs = { 'usr': usr, 'abrt': abrt }
  ok = utils_teste.verifica_objeto(rotulo, sessao, sessao.ObjSessao, usr, indice, ident, atrs)
  
  if ses != None and type(ses) is sessao.ObjSessao:
    
    sys.stderr.write("testando {obtem_usuario()}:\n")
    usr1 = sessao.obtem_usuario(ses)
    if usr1 != usr:
      sys.stderr.write("  **erro: retornou " + str(usr1) + ", deveria ter retornado " + str(usr) + "\n")
      ok = False
      
    sys.stderr.write("testando {aberta()}:\n")
    abrt11 = sessao.aberta(ses)
    if abrt1 != abrt:
      sys.stderr.write("  **erro: retornou " + str(abrt1) + ", deveria ter retornado " + str(abrt) + "\n")
      ok = False
  
  ok_global = ok_global and ok
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {sessao.cria}:\n")
s1 = sessao.cria(usr1)
sindice1 = 1
sident1 = "S-00000001"
verifica_sessao("s1", s1, sindice1, sident1, usr1, True)

s2 = sessao.cria(usr1)
sindice2 = 2
sident2 = "S-00000002"
verifica_sessao("s2", s2, sindice2, sident2, usr1, True)

s3 = sessao.cria(usr1)
sindice3 = 3
sident3 = "S-00000003"
verifica_sessao("s3", s3, sindice3, sident3, usr1, True)

sessao.logout(s1)
verifica_sessao("logout s1", s1, sindice1, sident1, usr1, False)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  # Terminou OK:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  # Termina com erro:
  sys.stderr.write("**erro - teste falhou\n")
  assert False
