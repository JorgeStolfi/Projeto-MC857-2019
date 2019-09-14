#! /usr/bin/python3

# Servidor do projeto MC857.

# Este script é o daemon servidor HTTP do website do projeto de MC857.

#! /usr/bin/python3

# Este programa executável Python3 é o daemon do servidor. Ele roda sem
# parar no computador local ou no computador host do projeto, escutando
# na porta internet 8081. Ao receber um comando HTTP (GET, POST, ou
# HEAD) enviado por um usuário, ele chama outros módulos do projeto para
# criar uma página HTML5 com a resposta aproriada, e envia a mesma de
# volta para o usuário.

# Interfaces do projeto usadas por este programa:
import base_sql
import tabelas
import processa_comando_http

def dispara():
  """Esta função inicia a execução do servidor."""
  
  # Conecta com a base de dados e inicializa as tabelas de objetos:
  dir = "DB/MC857"
  usr = None
  senha = None
  res = base_sql.conecta(dir,usr,senha); assert res == None
  limpa = False
  tabelas.inicializa_todas(limpa)
  
  # Inicia o processo servidor:
  host = '0.0.0.0' # Aceita pedidos de qualquer IP.
  porta = 8081 # Porta 8081 em vez de 80, para não precisar de acesso "root"
  objeto_servidor = processa_comando_http.cria_objeto_servidor(host,porta)
  print('disparando o servidor...')
  objeto_servidor.serve_forever()

# Programa principal do servidor:
dispara()
 
