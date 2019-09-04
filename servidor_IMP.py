#! /usr/bin/python3

# Interfaces do projeto usadas por este módulo:
import processa_comando_http

# Outras interfaces usadas por este módulo:

import base_sql
  
# Comandos para rodar o servidor:

def dispara():
  dir = "DB/MC857"
  usr = None
  senha = None
  bas = base_sql.conecta(dir,usr,senha)
  host = '0.0.0.0' # Aceita pedidos de qualquer IP.
  porta = 8081 # Porta 8081 em vez de 80, para não precisar de acesso "root"
  objeto_servidor = processa_comando_http.cria_servidor(host,porta)
  print('disparando o servidor...')
  objeto_servidor.serve_forever()
  
