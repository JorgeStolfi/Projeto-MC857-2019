#! /usr/bin/python3

import usuario; from usuario import ObjUsuario
import usuario_IMP; from usuario_IMP import ObjUsuario_IMP
import tabela_generica
import base_sql
import sys
import identificador

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
base_sql.conecta("DB/MC857",None,None)

# ----------------------------------------------------------------------
sys.stderr.write("Inicializando módulo {usuario}, limpando tabela:\n")
usuario.inicializa()
colunas = usuario.campos()
res = tabela_generica.limpa_tabela("usuarios", colunas)
sys.stderr.write("  res(limpa) = " + str(res) + "\n")

# ----------------------------------------------------------------------
def mostra_usuario(rotulo,usr,id,atrs):
  """Imprime usuário {usr} e compara seus atributos com {id,atrs}."""
  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write(rotulo + " = \n")
  if usr == None:
    sys.stderr.write("None\n")
  elif type(usr) is ObjUsuario_IMP:
    sys.stderr.write("  id = " + str(usuario.obtem_identificador(usr)) + "\n")
    sys.stderr.write("  atrs = " + str(usuario.obtem_atributos(usr)) + "\n")
    if atrs != None:
      id_confere = (usuario.obtem_identificador(usr) == id)
      atrs_conferem = (usuario.obtem_atributos(usr) == atrs)
      sys.stderr.write("  CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")
  sys.stderr.write("%s\n" % ("-" * 70))
 
def testa_cria_usuario(rotulo,id,atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  usr = usuario.cria(atrs)
  mostra_usuario(rotulo,usr,id,atrs)
  return usr
 
# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.acrescenta}:\n")
usr1_atrs = {
  "nome": "José Primeiro", 
  "senha": "123456789", 
  "email": "primeiro@gmail.com", 
  "CPF": "123.456.789-00", 
  "endereco": "Rua Senador Corrupto, 123\nVila Buracão\nCampinas, SP", 
  "CEP": "13083-418", 
  "telefone": "+55(19)9 9876-5432"
}
uid1 = "U-00000000"
usr1 = testa_cria_usuario("usr1",uid1,usr1_atrs)

usr2_atrs = {
  "nome": "João Segundo", 
  "senha": "987654321", 
  "email": "segundo@ic.unicamp.br", 
  "CPF": "987.654.321-99", 
  "endereco": "Avenida dos Semáforos, 1003\nJardim Pelado\nCampinas, SP", 
  "CEP": "13083-007", 
  "telefone": "+55(19)9 9898-1212"
}
uid2 = "U-00000001"
usr2 = testa_cria_usuario("usr2",uid2,usr2_atrs)

usr3_atrs = {
  "nome": "Juca Terceiro", 
  "senha": "4321002134", 
  "email": "muda@gmail.com", 
  "CPF": "111.111.111-11", \
  "endereco": "Rua Zero, 0000\nVila Zero\nCampinas, SP", \
  "CEP": "13083-999", 
  "telefone": "+55(19)9 9999-9999"
}
uid3 = "U-00000002"
usr3 = testa_cria_usuario("usr3",uid3,usr3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.busca_por_identificador}:\n")

usr1_a = usuario.busca_por_identificador(uid1)
mostra_usuario("usr1_a",usr1_a,uid1,usr1_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.busca_por_email}:\n")

em2 = usr2_atrs['email']
usr2_a = usuario.busca_por_email(em2)
mostra_usuario("usr2_a",usr2_a,uid2,usr2_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.busca_por_CPF}:\n")

CPF1 = "123.456.789-00"
usr1_b = usuario.busca_por_CPF(CPF1)
mostra_usuario("usr1_b",usr1_b,uid1,usr1_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("testando {usuario.muda_atributos}:\n")

usr1_mods = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
usuario.muda_atributos(usr1,usr1_mods)
usr1_c = usuario.busca_por_identificador(uid1)
usr1_c_atrs = usr1_atrs
for k, v in usr1_mods.items():
  usr1_c_atrs[k] = v
mostra_usuario("usr1_c",usr1_c,uid1,usr1_c_atrs)

if type(usr2) is ObjUsuario_IMP:
  usuario.muda_atributos(usr2,usr2_atrs) # Não deveria mudar os atributos
  mostra_usuario("usr2",usr2,uid2,usr2_atrs)

if type(usr2) is ObjUsuario_IMP:
  usr3_m_atrs = usr3_atrs.copy()
  usr3_m_atrs['CPF'] = usr2_atrs['CPF'] # Não pode alterar CPF.
  usuario.muda_atributos(usr2,usr3_m_atrs) # Deveria assumir os valores do usr3
  mostra_usuario("usr2",usr2,uid2,usr3_m_atrs)


#! /usr/bin/python3
