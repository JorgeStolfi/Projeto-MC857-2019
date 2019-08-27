#! /usr/bin/python3

# Interfaces do projeto usadas por este módulo:
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, cgi
import sys

import gera_html_pag, gera_html_elem, processa_comando_compra, processa_comando_login, processa_comando_busca, processa_comando_cadastra

# Outras interfaces usadas por este módulo:
import json, sys, re

# Classe interna:

class Processador_de_pedido_HTTP(BaseHTTPRequestHandler):
  """Classe necessária para usar `HTTPServer`.  Os métodos
  {do_GET}, {do_POST}, e {do_HEAD} desta classe são chamados pelo
  servidor para processar um pedido HTTP do usuário. 
  Eles devem devolver a resposta por meio de {devolve(hstr)}
  onde {hstr} é uma página em formato HTML, ou {None} em 
  caso de erro."""
  
  server_version = "MC857"
    """Versao da classe, passada aos métodos abaixo."""

  def do_GET(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler} 
    ao receber um pedido 'GET'."""
    dados = self.extrai_dados('GET')
    pagina = processa_comando_http.comando_GET(dados)
    self.devolve(pagina)

  def do_POST(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'POST'."""
    dados = self.extrai_dados('POST')
    pagina = processa_comando_http.comando_POST(dados)
    self.devolve(pagina)

  def do_HEAD(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
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

def comando_GET(dados):
  """Esta função processa um comando HTTP 'GET' recebido pelo servidor, com as
  informações convertidas em um dicionario {dados}."""
  print(dados)
  if dados['path'] == '':
    return gera_html_pag.entrada()

  elif dados['path'] == '/login':
    return processa_comando_login.processa()
  elif dados['path'] == '/cadastro':
    return processa_comando_cadastra.processa()
  elif dados['path'] == '/produto':
    return processa_comando_busca.processa(dados['query'])
  elif dados['path'] == '/produtos':
    return processa_comando_busca.processa(dados['query'])
  elif dados['path'] == '/compra':
    return processa_comando_compra.processa()
  else:
    return mostra_comando(dados)

def comando_POST(dados):
  """Esta função processa um comando HTTP 'POST' recebido pelo servidor, com as
  informações convertidas em um dicionario {dados}."""
  print(dados)
  if dados['path'] == '/search':
      return processa_comando_busca.processa(dados['query'])      
  else:    
    return mostra_comando(dados)

def comando_HEAD(dados):
  """Esta função processa um comando HTTP 'HEAD' recebido pelo servidor, com as
  informações convertidas em um dicionario {dados}."""
  return mostra_comando(dados)
  
def mostra_comando(dados):
  """Esta função de depuração devolve um string que é uma página HTML5 que mostra o conteúdo
  do dicionário {dados}."""
  cor_fundo = "#fff844"
  dados_lin = json.dumps(dados,indent='&nbsp;&nbsp;',sort_keys=True,separators=(',<br/>',': '))
  dados_lin = re.sub(r'\[','[<br/>',dados_lin)
  dados_lin = re.sub(r'\{','{<br/>',dados_lin)
  tipo = dados['command']
  texto = "<hr/>Metodo %s chamado com dados:<br/>%s<hr/>" % (tipo, dados_lin);
  conteudo = gera_html_elem.bloco_texto(texto,"Courier","18px","5px","left",None,cor_fundo)
  pagina = gera_html_pag.generica(conteudo)
  return pagina

def cria_objeto_servidor(host,porta):
  endereco = (host,porta)
  serv = HTTPServer(endereco, Processador_de_pedido_HTTP)
  return serv
