#! /usr/bin/python3

import os,sys,inspect
import base_sql 
import tabela_generica
import tabelas
import compra
import sessao
import usuario
import identificador
import utils_testes
from utils_testes import erro_prog, mostra


# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela, criando usuários para teste:\n")
usuario.cria_testes()

sys.stderr.write("Inicializando módulo {produtos}, limpando tabela, criando produtos para teste:\n")
compra.cria_testes()

sys.stderr.write("Inicializando módulo {compra}, limpando tabela, criando compras para teste:\n")
compra.cria_testes()

sys.stderr.write("Inicializando módulo {sessao}, limpando tabela:\n")
sessao.inicializa(True)

# ----------------------------------------------------------------------
sys.stderr.write("Obtendo dois usuários para teste:\n")

usr1 = usuario.busca_por_identificador("U-00000001")
usr2 = usuario.busca_por_identificador("U-00000002")

cmp1 = compra.busca_por_identificador("C-00000001")
cmp2 = compra.busca_por_identificador("C-00000003")

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

def verifica_sessao(rotulo, ses, indice, ident, usr, abrt, cookie, carrinho):
  """Testes básicos de consistência do objeto {ses} da classe {ObjSessao}, dados {indice},
  {ident} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write("verificando sessão %s\n" % rotulo)
  atrs = { 'usr': usr, 'abrt': abrt, 'cookie': cookie, 'carrinho': carrinho }
  ok = utils_testes.verifica_objeto(sessao, sessao.ObjSessao, ses, indice, ident, atrs)
  
  if ses != None and type(ses) is sessao.ObjSessao:
    
    sys.stderr.write("testando {obtem_usuario()}:\n")
    usr1 = sessao.obtem_usuario(ses)
    if usr1 != usr:
      aviso_prog("retornou " + str(usr1) + ", deveria ter retornado " + str(usr),True)
      ok = False
      
    sys.stderr.write("testando {aberta()}:\n")
    abrt1 = sessao.aberta(ses)
    if abrt1 != abrt:
      aviso_prog("retornou " + str(abrt1) + ", deveria ter retornado " + str(abrt),True)
      ok = False
       
    sys.stderr.write("testando {obtem_cookie()}:\n")
    cookie1 = sessao.obtem_cookie(ses)
    if cookie1 != cookie:
      aviso_prog("retornou " + str(cookie1) + ", deveria ter retornado " + str(cookie),True)
      ok = False
      
    sys.stderr.write("testando {obtem_carrinho()}:\n")
    carrinho1 = sessao.obtem_carrinho(ses)
    if carrinho1 != carrinho:
      aviso_prog("retornou " + str(carrinho1) + ", deveria ter retornado " + str(carrinho),True)
      ok = False
 
  if not ok:
    aviso_prog("teste falhou",True)
    ok_global = False

  sys.stderr.write("%s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
sys.stderr.write("testando {sessao.cria}:\n")
scook1 = "ABCDEFGHIJK"
s1 = sessao.cria(usr1, scook1, cmp1)
sindice1 = 1
sident1 = "S-00000001"
verifica_sessao("s1", s1, sindice1, sident1, usr1, True, scook1, cmp1)

scook2 = "BCDEFGHIJKL"
s2 = sessao.cria(usr2, scook2, cmp2)
sindice2 = 2
sident2 = "S-00000002"
verifica_sessao("s2", s2, sindice2, sident2, usr2, True, scook2, cmp2)

scook3 = "CDEFGHIJKLM"
s3 = sessao.cria(usr1, scook3, cmp1)
sindice3 = 3
sident3 = "S-00000003"
verifica_sessao("s3", s3, sindice3, sident3, usr1, True, scook3, cmp1)

sessao.fecha(s1)
verifica_sessao("fecha s1", s1, sindice1, sident1, usr1, False, scook1, cmp1)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
