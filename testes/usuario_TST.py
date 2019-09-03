#! /usr/bin/python3

import usuario; from usuario import ObjUsuario
import usuario_IMP; from usuario_IMP import ObjUsuario_IMP
import base_sql
import sys
import identificador

"""
Estrategia de teste

1. cria() TODO depende da base
    (a) sem atributos 
    (c) com atributos total

2. obtem_identificador TODO depende da base
    (a) antes de cria() => None
    (b) apos cria()

3. muda_atributos TODO depende da base
    (a) email ou cpf repetidos
    (b) sem elementos repetidos
"""

bas = base_sql.conecta("DB",None,None)

def mostra_usuario(nome,usr,atrs):
  """Imprime usuário {usr} e compara seus atributos com {atrs}."""
  sys.stderr.write(nome + " = " + str(usr) + "\n")
  if type(usr) is ObjUsuario_IMP:
    sys.stderr.write("  " + str(usr.obtem_atributos()) + "\n")
    sys.stderr.write("  " + str(usr.obtem_atributos() == usr_atrs) + "\n")
  

def testa_cria_usuario(nome,atrs):
  """Testa criação de usuário com atributos com {atrs}. Retorna o usuário."""
  usr = usuario.cria(bas,atrs)
  mostra_usuario(nome,usr,atrs)
  return usr

# Teste cria()
usr1_atrs = {"nome":"Joao Silva", "senha":"1234", "CPF":"91919191", \
            "endereco": "Rua 1, N 100", "telefone": "19 9999-9999", 
            "nascDt": "2001-01-01", "email": "joao@gmail.com"}
usr1 = testa_cria_usuario("usr1",usr1_atrs)

usr2_atrs = {"nome":"Maria Souza", "senha":"4321", "CPF":"82828282", \
            "endereco": "Rua 1, N 50", "telefone": "19 9999999", \
            "nascDt": "2002-02-02", "senha":"1111", "email": "maria@gmail.com"}
usr2 = testa_cria_usuario("usr2",usr2_atrs)

usr4_atrs = {"nome":"Muda Atributo", "senha":"4321", "CPF":"111111111", \
            "endereco": "Rua 1, N 50", "telefone": "19 9999999", \
            "nascDt": "2002-02-02", "senha":"4444", "email": "muda@gmail.com"}
usr4 = testa_cria_usuario("usr4",usr4_atrs)

# Teste muda_atributos
if type(usr2) is ObjUsuario_IMP:
  usr2.muda_atributos(bas,usr2) # Não deveria mudar os atributos
  mostra_usuario("usr2",usr2,usr2_atrs)

if type(usr2) is ObjUsuario_IMP:
  usr2.muda_atributos(bas,usr4) # Deveria assumir os valores do usr4
  mostra_usuario("usr2",usr2,usr4_atrs)

# Usuário sem dados: 
usr3_atrs = {}
usr3 = testa_cria_usuario("usr3",usr3_atrs)
