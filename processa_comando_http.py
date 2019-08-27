#! /usr/bin/python3

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

def cria_objeto_servidor(host,porta):
  """Devolve um objeto da classe {HTTPServer} que é usado pelo servidor HTTP
  para processar comandos GET, POST, e HEAD recebidos dos usuários remotos
  no {host} especificado (um string que é um endereço IP), pela porta especificada
  (um inteiro, p.ex. 80 ou 8081).  Se {host} for '0.0.0.0', aceita comandos de qualquer
  máquina."""
  return processa_comando_http_IMP.cria_objeto_servidor(host,porta)
