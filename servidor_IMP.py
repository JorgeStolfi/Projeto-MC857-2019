#! /usr/bin/python3
# Last edited on 2019-08-13 17:04:31 by stolfilocal

# Interfaces do projeto usadas por este módulo:
import processa_comando_http

# Outras interfaces usadas por este módulo:
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, cgi
import sys

import base

# Classe interna:

class Processador_de_pedido_HTTP(BaseHTTPRequestHandler):

  # Os métodos {do_GET}, {do_POST}, e {do_HEAD} destesão chamados pelo
  # servidor para processar um pedido HTTP do usuário. 
  # Chamam a devem devolver a resposta por meio de {self.wfile.write}.
  
  server_version = "MC857"

  def do_GET(self):
    """Este método chamado pela classe {BaseHTTPRequestHandler} 
    ao receber um pedido 'GET'."""
    dados = self.extrai_dados('GET')
    pagina = processa_comando_http.comando_GET(dados)
    self.devolve(pagina)

  def do_POST(self):
    """Este método chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'POST'."""
    dados = self.extrai_dados('POST')
    pagina = processa_comando_http.comando_POST(dados)
    self.devolve(pagina)

  def do_HEAD(self):
    """Este método chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'HEAD'."""
    dados = self.extrai_dados('HEAD')
    pagina = processa_comando_http.comando_HEAD(dados)
    self.devolve(pagina)
    
  # Método interno, usado pelos métodos acima:

  def extrai_dados(self,tipo):
    """Retorna todos os campos de um pedido do tipo {tipo} ('GET','POST', ou 'HEAD')
    na forma de um dicionário Python {dados}.  
    
    O valor do campo {dados['request_type']} é o {tipo} dado. Os demais 
    campos são extraídos do {self} conforme especificado 
    na classe {BaseHTTPRequestHandler}. 
    
    Os itens do preâmbulo {self.headers} são retornados na forma de um 
    sub-dicionário que é o valor do campo {dados['headers']}.""" 
    
    assert(self.command == tipo)

    dados = {}.copy() # Novo dicionário.
    dados['command'] = self.command
    dados['request_version'] = self.request_version
    dados['client_address'] = self.client_address
    dados['client_address_string'] = self.address_string()
    dados['path'] = self.path
    
    parsed_path = urllib.parse.urlparse(self.path)
    dados['real_path'] = parsed_path.path
    dados['query'] =  parsed_path.query
    
    dados['date_time'] = self.log_date_time_string()
    
    dados['server_version'] = self.server_version
    dados['sys_version'] = self.sys_version
    dados['protocol_version'] = self.protocol_version
    
    dados['headers'] = self.extrai_headers()
    
    dados['form_data'] = self.extrai_formulario()
    
    return dados
    
  def extrai_headers(self):
    """Converte o campo {self.headers} em um dicionario Python."""
    hds = {}.copy(); # Novo dicionario.
    for name, value in self.headers.items():
       hds[name] = value.rstrip()
    return hds
    
  def extrai_formulario(self):
    """Se o comando é 'POST', extrai os dados do formulário
    na forma de um dicionário Python."""
    ffs = {}.copy(); # Novo dicionário.
    if self.command == 'POST':
      formulario = cgi.FieldStorage(
        fp=self.rfile, 
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type']}
      )
      for chave in formulario.keys():
        item = formulario[chave]
        if item.filename:
           # Valor do item é um arquivo. Ignore por enquanto:
           ffs[chave] = "FILE(" + item.filename + ")"
        else:
          # Valor do item não é um arquivo:  
          ffs[chave] = item.value
    return ffs
    
  def devolve(self,pagina):
    """Manda para o usuário a {pagina} dada, que deve ser um string
    com o conteúdo da página em HTMP5.0.  
    
    Se {pagina} é {None}, devove código 404 com conteúdo 'text/plain',
    mensagem 'Não encontrado'. Se não devolve a página com código 200 e
    'content-type' 'text/html'."""
    
    if pagina == None:
      codigo = 404;  # Error - Not found.
      tipo = 'text/plain'
      conteudo = "Pagina nao encontrada - Page not found"
    else:
      codigo = 200;  # No error.
      tipo = 'text/html'
      conteudo = pagina
    
    self.send_response(codigo)
    self.send_header('Content-type',tipo)
    self.end_headers()
    self.wfile.write(conteudo.encode('utf-8'))
  
# Comandos para rodar o servidor:

def dispara():
  base.conecta()
  host = '0.0.0.0' # Aceita pedidos de qualquer IP.
  porta = 8081 # Porta 8081 em vez de 80, para não precisar de acesso "root"
  endereco = (host,porta)
  objeto_servidor = HTTPServer(endereco, Processador_de_pedido_HTTP)
  print('disparando o servidor...')
  objeto_servidor.serve_forever()
  