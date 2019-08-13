#! /usr/bin/python3
# Last edited on 2019-08-12 20:14:57 by stolfilocal

# Script principal.
# Este script é o servidor do website. O programa dosa sem parar,
# escutando na porta 8081. Ao receber um comando HTTP GET ou POST
# enviado por um usuário,  escrever no standard output uma página HTML5
# com a resposta aproriada.

# Interfaces usadas por este script:
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

import gera_html_pag

# Cria uma subclasse da classe {BaseHTTPRequestHandler}:

class processador_de_pedido_MC857(BaseHTTPRequestHandler):

  def do_GET(self):
    """Este método chamado pela classe mãe ao receber um pedido 'GET'.
    
    Deve devolver a resposta por meio de {self.send_response},
    {self.send_header}, {self.end_headers}, e {self.wfile.write}."""
    
    # Código de erro HTTP da resposta ('200', sem serro):
    self.send_response(200)
    
    # Atributos da resposta:
    self.send_header('Content-type','text/html')
    self.end_headers()
    
    # Página de resposta:
    pagina = gera_html_pag.entrada()
    self.wfile.write(pagina.encode('utf-8'))

    return

# Comandos para rodar o servidor:

def roda_servidor():
  """Esta função inicia o loop do servidor."""
  # Porta 8081 para não precisar de acesso "root"
  endereco = ('127.0.0.1', 8081)
  servidor = HTTPServer(endereco, processador_de_pedido_MC857)
  print('running server...')
  servidor.serve_forever()


roda_servidor()
