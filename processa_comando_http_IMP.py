# Implementação do módulo {processa_comando_http}.

# Interfaces do projeto usadas por este módulo:
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse, cgi
import sys

import base_sql
import gera_html_pag, gera_html_elem
import comando_botao_entrar
import comando_botao_cadastrar
import comando_botao_sair
import comando_subm_ver_produto
import comando_subm_comprar_produto
import comando_subm_buscar_produtos
import comando_subm_entrar
import comando_subm_cadastrar

# Outras interfaces usadas por este módulo:
import json, sys, re

# Classe interna:

class Processador_de_pedido_HTTP(BaseHTTPRequestHandler):
  """Classe necessária para usar `HTTPServer`.  Os métodos
  {do_GET}, {do_POST}, e {do_HEAD} desta classe são chamados pelo
  servidor para processar um pedido HTTP do usuário.

  Eles devem devolver a resposta por meio de {devolve_pagina(hstr)}
  onde {hstr} é uma página em formato HTML (ou {None} em
  caso de erro), ou {devolve_imagem(himg)} onde {himg}
  é uma imagem."""

  # CAMPOS E MÉTODOS HERDADOS

  # Versao da classe, passada no dicionário {dados} aos métodos abaixo:
  server_version = "MC857"

  def do_GET(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'GET'."""
    return self.do_geral('GET')


  def do_POST(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'POST'."""
    return self.do_geral('POST')

  def do_HEAD(self):
    """Este método é chamado pela classe {BaseHTTPRequestHandler}
    ao receber um pedido 'HEAD'."""
    return self.do_geral('HEAD')

  # CAMPOS E MÉTODOS INTERNOS

  def do_geral(self,tipo):
    # Processa um comando HHTP do {tipo} indicado ('GET','POST', ou 'HEAD').

    sys.stderr.write("processando um comando HTTP %s ...\n" % tipo)

    # Extrai os dados do comando HTTP na forma de um dicionário:
    dados = self.extrai_dados(tipo)

    if tipo == 'GET' and dados['real_path'][0:9] == '/imagens/':
      # Pedido de uma imagem:
      nome_imagem = dados['real_path'][1:]
      with open(nome_imagem, 'rb') as arq:
        imagem = arq.read()
      self.devolve_imagem(imagem)
    else:
      # Pedido de uma página HTML:

      # Determina a sessao à qual este comando se refere:
      sessao = self.obtem_sessao(dados)

      # Processa o comando e constrói a página HTML de resposta:
      pagina = processa_comando(tipo,sessao,dados)
      pag_debug = str(pagina)
      if len(pag_debug) > 207:
        pag_debug = pag_debug[0:100] + " [...] " + pag_debug[-100:]
      sys.stderr.write("pagina = " + pag_debug + "\n")

      # Envia a página ao browser do usuário:
      self.devolve_pagina(pagina)

  def obtem_sessao(self,dados):
    """Determina a sessão à qual o comando HTTP se refere, ou {None}
    se o usuário não está logado."""
    # !!! Usar cookies !!!
    return None

  def extrai_dados(self,tipo):
    """Retorna todos os campos de um pedido do tipo {tipo} ('GET','POST', ou 'HEAD')
    na forma de um dicionário Python {dados}.

    O valor do campo {dados['request_type']} é o {tipo} dado. Os demais
    campos são extraídos do {self} conforme especificado
    na classe {BaseHTTPRequestHandler}, com as seguintes adições:

     'headers': o valor é um sub-dicionário que é uma cópia
       de {self.headers}, contendo os itens do preâmbulo do pedido HTTP
       ('contents-type', etc.).

     'real_path': valor de {urlparse.urlparse(self.path).path}.
       No caso de 'GET', é a sub-cadeia do URL entre o último '/'
       e o '?'.  No caso de 'POST', é o atributo 'action' do <form>
       ou 'formaction' do botão tipo 'submit', com '/' na frente.

     'query':  o valor de {urlparse.urlparse(self.path).query}.
       no caso de 'GET', é a cadeia que segue o '?', possivelmente
       com códigos URL; por exemplo, 'foo=bar&bar=%28FOO%29&foo=qux'

     'query_data': o valor é um sub-dicionário com os argumentos de
       'query' destrinchados e com códigos URL convertidos
       para caracters Unicode.  Os valores são listas, para indicar
       repetição. Por exemplo, o 'query' acima viraria
       {'foo': ['bar','qux'], 'bar': ['(FOO)']}.  No caso de 'POST',
       é um dicionário vazio.

     'form_data': no caso de um comando 'POST',
       o valor é um sub-dicionário com os campos do formulário
       submetido. No caso de 'GET', é um dicionário vazio.
    """

    assert(self.command == tipo)

    dados = {}.copy() # Novo dicionário.

    # Campos originais do {BaseHTTPRequestHandler}
    dados['command'] = self.command
    dados['request_version'] = self.request_version
    dados['client_address'] = self.client_address
    dados['client_address_string'] = self.address_string()

    dados['date_time'] = self.log_date_time_string()
    dados['server_version'] = self.server_version
    dados['sys_version'] = self.sys_version
    dados['protocol_version'] = self.protocol_version

    dados['path'] = self.path # Por exemplo "/busca?

    # Campos adicionados por este módulo:
    parsed_path = urllib.parse.urlparse(self.path)
    dados['real_path'] = parsed_path.path
    dados['query'] =  parsed_path.query

    dados['headers'] = self.extrai_cabecalhos_http()

    dados['query_data'] = urllib.parse.parse_qs(dados['query'])

    dados['form_data'] = self.extrai_dados_de_formulario()

    return dados

  def extrai_cabecalhos_http(self):
    """Converte o campo {self.headers} em um dicionario Python, limpando
    brancos supérfluos."""
    hds = {}.copy(); # Novo dicionario.
    for name, value in self.headers.items():
       hds[name] = value.rstrip()
    return hds

  def extrai_dados_de_formulario(self):
    """Se o comando é 'POST', extrai os dados do formulário, dos
    campos {self.rfile} e {self,headers}, na forma de um dicionário Python."""
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

  def devolve_pagina(self,pagina):
    """Manda para o usuário a {pagina} dada, que deve ser um string
    com o conteúdo da página em HTML 5.0.

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

  def devolve_imagem(self,imagem):
    """Manda para o usuário a {imagem} dada, que deve ser um string
    com o conteúdo de uma imagem PNG."""

    codigo = 200;  # No error.
    tipo = 'image/PNG'

    self.send_response(codigo)
    self.send_header('Content-type',tipo)
    self.end_headers()
    self.wfile.write(imagem)

def processa_comando(tipo, sessao, dados):
  """Esta função processa um comando HTTP 'GET', 'POST', ou 'HEAD' recebido pelo
  servidor, com as informações convertidas em um dicionario {dados}."""
  sys.stderr.write("dados = " + str(dados) + "\n")

  # !!! Completar a lista abaixo com todos os módulos {comando_*.py} que existem. !!!
  if tipo == 'GET':
    # Comando causado por acesso inicial ou botão simples:
    if dados['real_path'] == '':
      # Acesso sem comando: mostra página de entrada.
      return gera_html_pag.entrada(sessao,dados['query_data'])
    elif dados['real_path'] == '/menu_cadastrar':
      # Usuário apertou o botão "Cadastrar" do menu principal:
      return comando_botao_cadastrar.processa(sessao,dados['query_data'])
    elif dados['real_path'] == '/menu_entrar':
      # Usuário apertou o botão "Entrar" (login) do menu principal:
      return comando_botao_entrar.processa(sessao,dados['query_data'])
    elif dados['real_path'] == '/menu_sair':
      # Usuário apertou o botão "Sair" (logout) do menu principal:
      return comando_botao_sair.processa(sessao,dados['query_data'])
    elif dados['real_path'][0:9] == '/imagens/':
      # Pedido de uma imagem:
      arquivo = dados['real_path'][9:]
      return
    else:
      # Comando não identificado:
      return mostra_comando(dados)
  elif tipo == 'POST':
    # Comando causado por botão do tipo "submit" dentro de um <form>...</form>:
    if dados['real_path'] == '/submit_entrar':
      # Usuário preencheu o formulário de login apertou "Entrar":
      return comando_subm_entrar.processa(sessao,dados['form_data'])
    elif dados['real_path'] == '/submit_cadastrar_usuario':
      # Usuário preencheu o formulário de cadastrar novo usuário e apertou "Cadastrar":
      return comando_subm_cadastrar_usuario.processa(sessao,dados['form_data'])
    elif dados['real_path'] == '/submit_buscar_produtos':
      # Usuário preencheu o campo de busca de produtos e apertou "Buscar":
      return comando_subm_buscar_produtos.processa(sessao,dados['form_data'])
    elif dados['real_path'] == '/submit_ver_produto':
      # Usuário apertou o botão "Comprar" ou equivalente numa descrição curta do produto:
      return comando_subm_ver_produto.processa(sessao,dados['form_data'])
    elif dados['real_path'] == '/submit_comprar_produto':
      # Usuário preencheu a quantidade desejada na página de um produto e apertou o botão "Comprar":
      return comando_subm_comprar_produto.processa(sessao,dados['form_data'])
    else:
      # Comando não identificado
      return mostra_comando(dados)
  elif tipo == 'HEAD':
    # Comando emitido por proxy server:
    return mostra_comando(dados)
  else:
    # Tipo de comando inválido:
    return mostra_comando(dados)

def mostra_comando(dados):
  """Esta função de depuração devolve um string que é uma página HTML5 que mostra o conteúdo
  do dicionário {dados}."""
  cor_fundo = "#fff844"
  dados_lin = json.dumps(dados,indent='&nbsp;&nbsp;',sort_keys=True,separators=(',<br/>',': '))
  dados_lin = re.sub(r'\[','[<br/>',dados_lin)
  dados_lin = re.sub(r'\{','{<br/>',dados_lin)
  dados_lin = re.sub(r'\},','  \},',dados_lin)
  tipo = dados['command']
  texto = "<hr/>Metodo %s chamado com dados:<br/>%s<hr/>" % (tipo, dados_lin)
  cor_fundo = "#0000ff"
  conteudo = gera_html_elem.bloco_texto(texto,'inline-block', "Courier","18px","normal","5px","left",None,cor_fundo)
  #bloco_texto(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo)
  pagina = gera_html_pag.generica(conteudo)
  return pagina

def cria_objeto_servidor(host,porta):
  endereco = (host,porta)
  serv = HTTPServer(endereco, Processador_de_pedido_HTTP)
  return serv
