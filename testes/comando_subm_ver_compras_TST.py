import usuario
import sessao
import comando_subm_ver_compras
import base_sql
import sys

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

sys.stderr.write("Inicializando módulo {usuario}, limpando tabela:\n")
usuario.inicializa(True)

sys.stderr.write("Inicializando módulo {sessao}, limpando tabela:\n")
sessao.inicializa(True)
# ----------------------------------------------------------------------

usr1_atrs = {
  "nome": "Teste Primeiro", 
  "senha": "123456789", 
  "email": "primeiro@teste.com", 
  "CPF": "123.456.789-00", 
  "endereco": "Rua dos testers", 
  "CEP": "12345-678", 
  "telefone": "+55( 12)9 3456-7890"
}

usr1 = usuario.cria(usr1_atrs)

s1 = sessao.cria(usr1)

identificador = usuario.obtem_identificador(usr1)

userTest = comando_subm_ver_compras.processa(s1)

if( userTest == usr1):
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  sys.stderr.write("**erro - teste falhou\n")
  assert False