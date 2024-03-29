# Implementação do módulo {processa_comando_http}.

# Interfaces do projeto usadas por este módulo:

import sessao
import usuario

import comando_alterar_qtd_de_produto
import comando_buscar_compras
import comando_buscar_produtos
import comando_comprar_produto
import comando_definir_dados_de_produto
import comando_cadastrar_usuario
import comando_alterar_usuario
import comando_definir_endereco
import comando_definir_meio_de_pagamento
import comando_excluir_item_de_compra
import comando_fazer_login
import comando_fazer_logout
import comando_finalizar_compra
import comando_nova_compra
import comando_solicitar_form_de_dados_de_produto
import comando_solicitar_form_de_cadastrar_usuario
import comando_solicitar_form_de_alterar_usuario
import comando_solicitar_form_de_endereco
import comando_solicitar_form_de_meio_de_pagamento
import comando_solicitar_form_de_login
import comando_solicitar_form_de_acrescentar_produto
import comando_solicitar_form_de_contato
import comando_trocar_carrinho
import comando_ver_carrinho
import comando_ver_compra
import comando_ver_ofertas
import comando_ver_produto
import comando_ver_objeto
import comando_buscar_compras_por_produto
import comando_buscar_usuarios

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
      pag, ses_nova = processa_comando(tipo, ses, dados)
      pag_debug = str(pag)
      if len(pag_debug) > 207:
        pag_debug = pag_debug[0:100] + " [...] " + pag_debug[-100:]
      mostra(0, "pag = " + pag_debug + "")

      # Envia a página ao browser do usuário:
      self.devolve_pagina(ses_nova, pag)

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

    dados['cookies'] = self.extrai_cookies(dados['headers'])

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

  def extrai_cookies(self, dados):
    """Analisa a cadeia {cook_str} que é o campo 'Cookie'
        do dicionário {dados}, que veio com os headers HTTP, convertendo-a
    em um dicionário Python.

    Supõe que {cook_str} é uma cadeia com formato '{chave1}={valor1};
    {chave2}={valor2}; {...}'. Os campos de valor não podem conter ';'
    ou '='. Se algum valor estiver envolvido em aspas, remove as aspas.
    Os campos de {cook_str} cujo valor é a cadeia 'None' ou vazia são omitidos."""
    cookies = {}.copy()
    if 'Cookie' in dados:
      cook_str = dados['Cookie']
      cook_els = re.split(r'[ ;]+', cook_str)
      for cook_el in cook_els:
        # A cadeia {cook_el} deve ser '{chave}={valor}'
        cook_pair = re.split(r'[=]', cook_el)
        assert len(cook_pair) == 2
        cook_key = cook_pair[0]
        assert cook_key != ""
        cook_val = (cook_pair[1]).strip("\"'")
        if cook_val != "" and cook_val != "None":
          cookies[cook_key] = cook_val
    return cookies

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
      # Enumera os nomes dos campos presentes no formulário:
      for chave in formulario.keys():
        # Pega a lista de todos os campos com nome {chave}:
        item_list = formulario.getlist(chave)
        # Enumera os campos com esse nome:
        for val in item_list:
          # Armazena no dicionário:
          if chave in ffs:
            erro_prog("o formulário tem mais de um campo com nome '" + chave + "'")
          ffs[chave] = val
    return ffs

  def obtem_sessao(self, dados):
    """Determina a sessão à qual o comando HTTP se refere, ou {None}
    se o usuário não está logado, a partir do dicionário de cookies
    contidos em {dados}."""
    if not 'cookies' in dados:
      # Não temos cookies?
      return None
    cookies = dados['cookies']
    if 'id_sessao' in cookies:
      id_sessao = cookies['id_sessao']
      ses = sessao.busca_por_identificador(id_sessao)
    else:
      ses = None
    return ses

  def devolve_pagina(self, ses, pag):
    """Manda para o usuário a {pag} dada, que deve ser um string
    com o conteúdo da página em HTML 5.0., com os preâmulos adequados
    segundo o protocolo HTTP.
    Se {pag} é {None}, sinaliza no preâmbulo o código 404 com conteúdo 'text/plain',
    mensagem 'Não encontrado'. Caso contrário, devolve a página com código 200 e
    'content-type' 'text/html'.

    Se {ses} não é {None}, deve ser um objeto da classe {ObjSession}.
    Nesse caso, a função inclui no preâmbulo cookies que identificam a
    sessão e o o usuário."""

    if pag == None:
      aviso_prog("Página a devolver é {None}", True)
      codigo = 404;  # Error - Not found.
      msg = "Pagina nao encontrada - Page not found"
      tipo = 'text/plain'
      pag = gera_html_pag.mensagem_de_erro(ses, msg)
      if pag == None:
        aviso_prog("Função {gera_html_pag.mensagem_de_erro} devolveu {None}", True)
        #  Na marra:
        pag = "<!doctype html>\n<html>\n<body>\n" + msg + "\n</body>\n</head>"
    else:
      codigo = 200;  # No error.
      tipo = 'text/html'

    self.send_response(codigo)
    self.send_header('Content-type', tipo)

    # Manda cookies que identificam usuário e sessão:
    if ses != None:
      id_sessao = sessao.obtem_identificador(ses)
      cookie = sessao.obtem_cookie(ses)
      usr = sessao.obtem_usuario(ses)
      id_usuario = usuario.obtem_identificador(usr)
    else:
      id_sessao = ""
      cookie = ""
      usr = None
      id_usuario = ""
    self.send_header('Set-Cookie', 'id_usuario=' + id_usuario)
    self.send_header('Set-Cookie', 'id_sessao=' + id_sessao)
    self.send_header('Set-Cookie', 'cookie_sessao=' + cookie)

    self.end_headers()
    self.wfile.write(pag.encode('utf-8'))

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
  servidor, com as informações convertidas em um dicionario {dados}.

  A sessão {ses} deve ser a sessão deduzida a partir dos cookies que
  viram com o comando HTTP.

  Esta função devolve a página {pag} a ser enviada ao usuário.  Devolve também
  a sessão {ses_nova} corrente.  Esta sessão pode ser diferente de {ses}, se o
  comando for login ou logout."""

  mostra(0, "dados = " + str(dados) + "")

  mostra_cmd = True # Deve mostrar os dados do comando no final da página?

  cmd = dados['real_path']; del dados['real_path']

  # Define página a retornar {pag} e a sessão {ses_nova} para futuros comandos:
  ses_nova = ses  # Geralmente a sessão não muda
  if tipo == 'GET' or tipo == 'POST':
    # Obtem os argumentos do comando:
    if tipo == 'GET':
      # Comando causado por acesso inicial ou botão simples:
      args = dados['query_data']; del dados['query_data'] # Argumentos do comando "GET", no próprio URL "cmd?n1=v1&n2=v2...".
    elif tipo == 'POST':
      # Comando causado por botão do tipo "submit" dentro de um <form>...</form>:
      args = dados['form_data']; del dados['form_data'] # Campos do formulário.
    else:
      assert False

    # Despacha o comando:
    # !!! Completar a lista abaixo com todos os módulos {comando_*.py} que existem. !!!
    if cmd == '' or cmd == '/' or cmd == '/principal':
      # Acesso sem comando, ou usuário apertou "Principal" no menu geral.
      pag =  gera_html_pag.principal(ses, [])

    elif cmd == '/solicitar_form_de_login':
      # Usuário apertou o botão "Entrar" (login) do menu geral:
      # ATENÇÃO: Este comando só mostra o formulário de login, não muda a sessão ainda.
      pag = comando_solicitar_form_de_login.processa(ses, args)

    elif cmd == '/solicitar_form_de_contato':
      # Usuário apertou o botão "Contato" do menu geral:
      # ATENÇÃO: Este comando só mostra o formulário de contato, não muda a sessão ainda.
      pag = comando_solicitar_form_de_contato.processa(ses, args)

    elif cmd == '/fazer_logout':
      # Usuário apertou o botão "Sair" (logout) do menu geral:
      # ATENÇÃO: devolve também a nova sessão (que geralmente vai ser {None}).
      pag, ses_nova = comando_fazer_logout.processa(ses, args)

    elif cmd == '/ver_carrinho':
      # Usuário apertou o botão "Meu Carrinho" do menu geral:
      pag = comando_ver_carrinho.processa(ses, args)

      
    elif cmd == '/buscar_compras':
      # Usuário apertou o botão "Minhas compras" do menu geral:
      pag = comando_buscar_compras.processa(ses, args)

    elif cmd == '/solicitar_form_de_dados_de_produto':
      # Usuário apertou o botão "Acrescentar produto" do menu geral:
      pag = comando_solicitar_form_de_dados_de_produto.processa(ses, args)

    elif cmd == '/definir_dados_de_produto':
      # Usuário apertou o botão "Confirma" num formulário de acrescentar/alterar produto:
      pag = comando_definir_dados_de_produto.processa(ses, args)

    elif cmd == '/fazer_login':
      # Usuário preencheu o formulário de login apertou "Entrar":
      # ATENÇÃO: devolve também a nova sessão (que pode ser {None} se o login não deu certo).
      pag, ses_nova = comando_fazer_login.processa(ses, args)

    elif cmd == '/solicitar_form_de_cadastrar_usuario':
      # Usuário apertou o botão "Cadastrar" do menu geral:
      pag = comando_solicitar_form_de_cadastrar_usuario.processa(ses, args)

    elif cmd == '/cadastrar_usuario':
      # Usuário apertou "Cadastrar" em formulário de cadastrar usuário:
      pag = comando_cadastrar_usuario.processa(ses, args)

    elif cmd == '/solicitar_form_de_alterar_usuario':
      # Usuário apertou o botão "Minha Conta" do menu geral:
      pag = comando_solicitar_form_de_alterar_usuario.processa(ses, args)

    elif cmd == '/alterar_usuario':
      # Usuário apertou "Confirmar" em formulário de alterar usuário:
      pag = comando_alterar_usuario.processa(ses, args)

    elif cmd == '/buscar_produtos':
      # Usuário preencheu o campo de busca de produtos e apertou "Buscar":
      pag = comando_buscar_produtos.processa(ses, args)
   
    elif cmd == '/buscar_usuarios':
      # Usuário preencheu o campo de busca de produtos e apertou "Buscar":
      pag = comando_buscar_usuarios.processa(ses, args)
   
    elif cmd == '/ver_produto':
      # Usuário apertou o botão "Ver" ou equivalente numa descrição curta do produto:
      pag = comando_ver_produto.processa(ses, args)

    elif cmd == '/ver_objeto':
      # Usuário apertou o botão "Ver Objeto" ou equivalente no menu geral:
      pag = comando_ver_objeto.processa(ses, args)
      
    elif cmd == '/ver_compra':
      pag = comando_ver_compra.processa(ses, args)

    elif cmd == '/ver_ofertas':
      # Usuário apertou o botão "Ofertas" ou equivalente no menu geral:
      pag = comando_ver_ofertas.processa(ses, args)

    elif cmd == '/nova_compra':
      #Usuário apertou o botão "Nova Compra" no menu 
      pag = comando_nova_compra.processa(ses, args)

    elif cmd == '/comprar_produto':
      # Usuário preencheu a quantidade desejada na página de um produto e apertou o botão "Comprar":
      pag = comando_comprar_produto.processa(ses, args)

    elif cmd == '/alterar_qtd_de_produto':
      # Usuário alterou a quantidade desejada numa descrição de produto ou num item de uma compra:
      pag = comando_alterar_qtd_de_produto.processa(ses, args)

    elif cmd == '/excluir_item_de_compra':
      # Usuário apertou o botão "Excluir" do carrinho:
      pag = comando_excluir_item_de_compra.processa(ses, args)

    elif cmd == '/finalizar_compra':
      # Usuário apertou o botão "Finalizar compra" na descrição do carrinho:
      pag = comando_finalizar_compra.processa(ses, args)

    elif cmd == '/solicitar_form_de_endereco':
      # Usuário apertou o botão "Alterar endereço" num formulário de dados de compra:
      pag = comando_solicitar_form_de_endereco.processa(ses, args)

    elif cmd == '/definir_endereco':
      # Usuário apertou o botão "Confirmar" num formulário de alterar endereço de entrega:
      pag = comando_definir_endereco.processa(ses, args)

    elif cmd == '/solicitar_form_de_meio_de_pagamento':
      # Usuário apertou o botão "Definir/Alterar meio de pagamento" num formulário de dados de compra:
      pag = comando_solicitar_form_de_meio_de_pagamento.processa(ses, args)

    elif cmd == '/definir_meio_de_pagamento':
      # Usuário apertou o botão "Confirmar" num formulário de alterar meio de pagamento de compra:
      pag = comando_definir_meio_de_pagamento.processa(ses, args)

    elif cmd == '/trocar_carrinho':
      # Usuário apertou o botão "Usar como carrinho" numa descrição de um pedido de compra:
      pag = comando_trocar_carrinho.processa(ses, args)

    elif cmd == '/buscar_compras_por_produto':
      # Usuário apertou o botão "Ver compras com produto" numa descrição de um produto:
      pag = comando_buscar_compras_por_produto.processa(ses, args)

    elif cmd == '/solicitar_form_de_acrescentar_produto':
      # Administrador apertou o botão acrescentar produto  
      pag = comando_solicitar_form_de_acrescentar_produto.processa(ses, args)

    else:
      # Comando não identificado
      pag =  gera_html_pag.mensagem_de_erro(ses, ("** comando POST \"%s\" inválido" % cmd))

  elif tipo == 'HEAD':
    # Comando emitido por proxy server:
    # !!! (MAIS TARDE) Tratar este caso !!!
    args = {}.copy()
    pag =  gera_html_pag.mensagem_de_erro(ses, ("** comando HEAD \"%s\" não implementado" % cmd))
  else:
    # Tipo de comando inválido:
    args = {}.copy()
    pag =  gera_html_pag.mensagem_de_erro(ses, ("** comando \"%s\" não implementado" % tipo))

  if mostra_cmd:
    # Acrescenta os dados para depuração:
    pag = re.sub(r'</body>', ("<br/>%s<br/></body>" % formata_dados_http(cmd,args,dados)), pag)

  return pag, ses_nova

def formata_dados_http(cmd,args,resto):
  """Esta função de depuração devolve um string que é um trecho de HTML5 a ser inserido
  no final de uma página.  Ele mostra a função {cmd} que foi executada, o dicionário {args}
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
  return conteudo
