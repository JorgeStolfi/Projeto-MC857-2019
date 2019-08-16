#! /usr/bin/python3
# Last edited on 2019-08-13 00:44:21 by stolfilocal

# Funções para processar comandos HTTP (GET,POST, ou HEAD)
# recebidos do usuário.  

# Estas funções devem devolver um {string} que é
# uma página HTML5 completa; ou {None} para indicar que
# o pedido é inválido.  O argumento {dados}
# é um dicionário que contém os dados extraídos
# do pedido pela classe {BaseHTTPRequestHandler}.

# De modo geral, o valor de {dados['Xxx']} é o valor
# do atributo {self.Xxx} conforme descrito em {BaseHTTPRequestHandler}.
# Campos especiais: 
#
#  'real_path': valor de {urlparse.urlparse(self.path).path}.
#
#  'query':  valor de {urlparse.urlparse(self.path).query}.
#
#  'headers': o valor é um sub-dicionário {self.headers}
#    com os itens do preâmbulo do pedido HTTP 
#    ('contents-type', etc.).


# Implementação desta interface:
import processa_comando_http_IMP

def comando_GET(dados):
  """Esta função processa um comando HTTP 'GET' recebido pelo servidor."""
  return processa_comando_http_IMP.comando_GET(dados)

def comando_POST(dados):
  """Esta função processa um comando HTTP 'POST' recebido pelo servidor."""
  return processa_comando_http_IMP.comando_POST(dados)

def comando_HEAD(dados):
  """Esta função processa um comando HTTP 'HEAD' recebido pelo servidor."""
  return processa_comando_http_IMPcomando_.HEAD(dados)
