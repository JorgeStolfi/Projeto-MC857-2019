# Implementação do módulo {processa_comando_http}.

# Interfaces do projeto usadas por este módulo:

import sessao
import usuario

import comando_menu_cadastrar_usuario
import comando_menu_entrar
import comando_menu_sair
import comando_menu_ver_carrinho
import comando_menu_ver_todas_as_compras
import comando_menu_acrescentar_produto

import comando_submit_buscar_produtos
import comando_submit_cadastrar_usuario
import comando_submit_comprar_produto
import comando_submit_acrescentar_produto
import comando_submit_alterar_qt_de_produto
import comando_submit_entrar
import comando_submit_alterar_qt_de_item_de_compra
import comando_submit_excluir_item_de_compra
import comando_submit_finalizar_compra
import comando_menu_ver_todas_as_compras
import comando_submit_ver_produto
import comando_submit_trocar_carrinho
import comando_menu_ver_usuario
import comando_submit_alterar_endereco_de_entrega

import gera_html_elem
import gera_html_pag

import utils_testes
from utils_testes import erro_prog, mostra

# Outras interfaces usadas por este módulo:
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys, re, cgi
import urllib.parse

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

  def do_geral(self, tipo):
    # Processa um comando HHTP do {tipo} indicado ('GET','POST', ou 'HEAD').

    mostra(0, ("processando um comando HTTP %s ..." % tipo))

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
      ses = self.obtem_sessao(dados)

      # Processa o comando e constrói a página HTML de resposta:
      pagina = processa_comando(tipo, ses, dados)
      pag_debug = str(pagina)
      if len(pag_debug) > 207:
        pag_debug = pag_debug[0:100] + " [...] " + pag_debug[-100:]
      mostra(0, "pagina = " + pag_debug + "")

      # Envia a página ao browser do usuário:
      self.devolve_pagina(pagina)

  def obtem_sessao(self, dados):
    """Determina a sessão à qual o comando HTTP se refere, ou {None}
    se o usuário não está logado."""
    # !!! (MAIS TARDE) Usar cookies !!!
    return sessao.busca_por_identificador("S-00000001")

  def extrai_dados(self, tipo):
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
    campos {self.rfile} e {self, headers}, na forma de um dicionário Python."""
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

  def devolve_pagina(self, pagina):
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
    self.send_header('Content-type', tipo)
    self.end_headers()
    self.wfile.write(conteudo.encode('utf-8'))

  def devolve_imagem(self, imagem):
    """Manda para o usuário a {imagem} dada, que deve ser um string
    com o conteúdo de uma imagem PNG."""

    codigo = 200;  # No error.
    tipo = 'image/PNG'

    self.send_response(codigo)
    self.send_header('Content-type', tipo)
    self.end_headers()
    self.wfile.write(imagem)

def cria_objeto_servidor(host, porta):
  endereco = (host, porta)
  serv = HTTPServer(endereco, Processador_de_pedido_HTTP)
  return serv

# FUNÇÕES INTERNAS

def processa_comando(tipo, ses, dados):
  """Esta função processa um comando HTTP 'GET', 'POST', ou 'HEAD' recebido pelo
  servidor, com as informações convertidas em um dicionario {dados}."""
  mostra(0, "dados = " + str(dados) + "")
  
  mostra_cmd = True # Deve mostrar os dados do comando no final da página?

  # !!! Completar a lista abaixo com todos os módulos {comando_*.py} que existem. !!!
  cmd = dados['real_path']; del dados['real_path']
  if tipo == 'GET':
    # Comando causado por acesso inicial ou botão simples:
    args = dados['query_data']; del dados['query_data'] # Argumentos do comando "GET", no próprio URL "cmd?n1=v1&n2=v2...".
    if cmd == '' or cmd == '/' or cmd == '/principal':
      # Acesso sem comando, ou usuário apertou "Principal" no menu geral.
      pagina =  gera_html_pag.principal(ses)
    elif cmd == '/menu_cadastrar':
      # Usuário apertou o botão "Cadastrar" do menu geral:
      pagina =  comando_menu_cadastrar_usuario.processa(ses, args)
    elif cmd == '/menu_usuario':
      # Usuário apertou o botão "Minha Conta" do menu geral:
      pagina =  comando_menu_ver_usuario.processa(ses, args)
    elif cmd == '/menu_entrar':
      # Usuário apertou o botão "Entrar" (login) do menu geral:
      pagina =  comando_menu_entrar.processa(ses, args)
    elif cmd == '/menu_sair':
      # Usuário apertou o botão "Sair" (logout) do menu geral:
      pagina =  comando_menu_sair.processa(ses, args)
    elif cmd == '/menu_carrinho':
      # Usuário apertou o botão "Meu Carrinho" do menu geral:
      pagina =  comando_menu_ver_carrinho.processa(ses, args)
    elif cmd == '/menu_ver_todas_as_compras':
      # Usuário apertou o botão "Minhas compras" do menu geral:
      pagina =  comando_menu_ver_todas_as_compras.processa(ses, args)
    elif cmd == '/menu_acrescentar_produto':
      # Usuário apertou o botão "Acrescentar produto" do menu geral:
      pagina =  comando_menu_acrescentar_produto.processa(ses, args)
    else:
      # Comando não identificado:
      pagina = gera_html_pag.mensagem_de_erro(ses, ("** comando GET \"%s\" inválido" % cmd)) 
  elif tipo == 'POST':
    # Comando causado por botão do tipo "submit" dentro de um <form>...</form>:
    args = dados['form_data']; del dados['form_data'] # Campos do formulário.
    if cmd == '/submit_entrar':
      # Usuário preencheu o formulário de login apertou "Entrar":
      pagina =  comando_submit_entrar.processa(ses, args)
    elif cmd == '/submit_cadastrar_usuario':
      # Usuário preencheu o formulário de cadastrar novo usuário e apertou "Cadastrar":
      pagina =  comando_submit_cadastrar_usuario.processa(ses, args)
    elif cmd == '/submit_buscar_produtos':
      # Usuário preencheu o campo de busca de produtos e apertou "Buscar":
      pagina =  comando_submit_buscar_produtos.processa(ses, args)
    elif cmd == '/submit_ver_produto':
      # Usuário apertou o botão "Comprar" ou equivalente numa descrição curta do produto:
      pagina =  comando_submit_ver_produto.processa(ses, args)
    elif cmd == '/submit_comprar_produto':
      # Usuário preencheu a quantidade desejada na página de um produto e apertou o botão "Comprar":
      pagina =  comando_submit_comprar_produto.processa(ses, args)
    elif cmd == '/submit_alterar_qt_de_produto':
      # Usuário alterou a quantidade desejada numa descrição de produto:
      pagina =  comando_submit_alterar_qt_de_produto.processa(ses, args)
    elif cmd == '/submit_excluir_item_de_compra':
      # Usuário apertou o botão "Excluir" do carrinho:
      pagina =  comando_submit_excluir_item_de_compra.processa(ses, args)
    elif cmd == '/submit_finalizar_compra':
      # Usuário apertou o botão "Finalizar compra" na descrição do carrinho:
      pagina =  comando_submit_finalizar_compra.processa(ses, args)
    elif cmd == '/submit_alterar_endereco_de_entrega':
      # Usuário apertou o botão "Alterar endereço" na descrição de um pedido de compra:
      pagina =  comando_submit_alterar_endereco_de_entrega.processa(ses, args)
    elif cmd == '/submit_trocar_carrinho':
      pagina = comando_submit_trocar_carrinho.processa(ses, args)
    else:
      # Comando não identificado
      pagina =  gera_html_pag.mensagem_de_erro(ses, ("** comando POST \"%s\" inválido" % cmd)) 
  elif tipo == 'HEAD':
    # Comando emitido por proxy server:
    # !!! (MAIS TARDE) Tratar este caso !!!
    args = {}.copy()
    pagina =  gera_html_pag.mensagem_de_erro(ses, ("** comando HEAD \"%s\" não implementado" % cmd)) 
  else:
    # Tipo de comando inválido:
    args = {}.copy()
    pagina =  gera_html_pag.mensagem_de_erro(ses, ("** comando \"%s\" não implementado" % tipo)) 
    
  if mostra_cmd:
    # Acrescenta os dados para depuração:
    pagina = re.sub(r'</body>', ("<br/>%s<br/></body>" % formata_dados_http(cmd,args,dados)), pagina)
  return pagina

def formata_dados_http(cmd,args,resto):
  """Esta função de depuração devolve um string que é um trecho de HTML5 a ser inserido 
  no final de uma página.  Ele mostra a função {cmd} a executar, o dicionário {args} 
  com os argumentos da mesma, e o dicionário {resto} com os demais parâmetros do comando
  HTTP recebido, num formato razoavelmente legível."""
  resto_d = resto.copy()
  tipo = resto_d['command']; del resto_d['command'] # 'GET', 'POST', ou 'HEAD'
  # Dados principais:
  args_lin = utils_testes.formata_dict(args)
  resto_lin = utils_testes.formata_dict(resto_d)
  
  # Monta um bloco HTML com os dados de depuração:
  texto = ("Resposta a comando HTTP \"%s\" recebido com dados principais:" % tipo)
  texto = texto + ("<br/>cmd = \"%s\"<br/>args =<br/>%s" % (cmd, args_lin))
  texto = texto + ("<br/><hr/>Outros dados:<br/>%s" % resto_lin)
  conteudo = gera_html_elem.bloco_texto(texto, None,"Courier","18px","normal","5px","left", None, None)
  conteudo = "<hr/>\n" + gera_html_elem.div("background-color:#bbbbbb;", conteudo) + "<hr/>\n"
  # !!! Extrair informações abaixo dos dados !!!
  ses = None
  return conteudo
