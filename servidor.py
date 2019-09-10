#! /usr/bin/python3

# Servidor do projeto MC857.

# Este script é o daemon servidor HTTP do website do projeto de MC857.

# O daemon é um programa python que roda sem parar no comutador local 
# ou no computador host do projeto, escutando na porta internet 8081. 
# Ao receber um comando HTTP (GET, POST, ou HEAD) enviado por 
# um usuário,  ele chama outros módulos do projeto para 
# criar uma página HTML5 com a resposta aproriada, e 
# envia a mesma de volta para o usuário.

# Interfaces do projeto usadas por este programa:
import processa_comando_http
import base_sql

def dispara():
  """Esta função inicia a execução do servidor."""
  dir = "DB/MC857"
  usr = None
  senha = None
  bas = base_sql.conecta(dir,usr,senha)
  host = '0.0.0.0' # Aceita pedidos de qualquer IP.
  porta = 8081 # Porta 8081 em vez de 80, para não precisar de acesso "root"
  objeto_servidor = processa_comando_http.cria_objeto_servidor(host,porta)
  print('disparando o servidor...')
  objeto_servidor.serve_forever()

# Programa principal do servidor:
dispara()
 
