# Implementação do módulo {gera_html_pag}.

# Interfaces do projeto importadas por este módulo:
import produto
import sessao
import usuario
import compra
import gera_html_elem
import gera_html_form
import comando_ver_ofertas
import gera_html_botao
import pprint
from utils_testes import erro_prog, mostra

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML
import re, sys

def generica(ses, html_conteudo, erros):

  # Cabeçalho das páginas:
  html_cabe = gera_html_elem.cabecalho("Site de compras: Projeto MC857A 2019-2s", True)

  # Menu geral no alto da página:
  logado = (ses != None)
  if logado:
    usr = sessao.obtem_usuario(ses)
    nome_usuario = usuario.obtem_atributos(usr)['nome']
    admin = usuario.obtem_atributos(usr)['administrador']
  else:
    nome_usuario = None
    admin = False
  html_menu = gera_html_elem.menu_geral(logado, nome_usuario, admin)

  # Mensagens de erro:
  if erros == None:
    erros = []
  elif type(erros) == str:
    # Split lines, create a list:
    erros = re.split('[\n]', erros)
  assert type(erros) is list
  # Cleanup the messages:
  erros = [ er.strip() for er in erros ]
  erros = [ er for er in erros if len(er) > 0 ]
  if len(erros) != 0:
    erros = "<br/>\n" + "<br/>\n".join(erros)
    html_erros = gera_html_elem.bloco_de_erro(erros) + "\n"
  else:
    html_erros = ""

  # Rodapé da página:
  html_roda = gera_html_elem.rodape()

  # Monta a página:
  pagina = html_cabe + "<br/>" + html_menu + "<br/>" + html_erros + "<br/>" + html_conteudo + "<br/>" + html_roda

  # Formata o HTML para maior legibilidade:
  return bsoup(pagina, "html.parser").prettify()

def principal(ses, erros):
  if ses !=None:
    usr = sessao.obtem_usuario(ses)
    atrs = usuario.obtem_atributos(usr)
    nome = atrs['nome']
    texto1 = "<hr/>Seja bem vindo(a) <b>"+nome+"</b> ao nosso site de compras!"
  else:
    texto1 = "<hr/>Seja bem vindo(a) ao nosso site de compras!"
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto2 = "<hr/><i>DATA CORRENTE </i><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  cor_texto = "#000488"
  cor_fundo = "#eeeeee"
  bloco_texto1 =  gera_html_elem.bloco_texto(texto1, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)
  bloco_texto2 =  gera_html_elem.bloco_texto(texto2, None,"Courier","16px","normal","5px","center", cor_texto, cor_fundo)
  ofertas = produto.busca_ofertas()
  bloco_ofertas = gera_html_elem.bloco_de_lista_de_produtos(ofertas)
  conteudo = bloco_texto1 + bloco_ofertas + bloco_texto2
  pagina = generica(ses, conteudo, erros)
  return pagina

def mostra_produto(ses, id_compra, prod, qtd, erros):
  conteudo = gera_html_elem.bloco_de_produto(id_compra, prod, qtd, True)
  pagina = generica(ses, conteudo, erros)
  return pagina

def lista_de_produtos(ses, idents, erros):
  conteudo = gera_html_elem.bloco_de_lista_de_produtos(idents)
  pagina = generica(ses, conteudo, erros)
  return pagina

def entrar(ses, erros):
  conteudo = gera_html_form.entrar()
  pagina = generica(ses, conteudo, erros)
  return pagina

def contato(ses, erros):
  conteudo = gera_html_form.contato()
  pagina = generica(ses, conteudo, [])
  return pagina

def alterar_endereco(ses, id_compra, atrs, erros):
  if atrs == None:
    # Obtém atributos correntes da compra:
    cpr = compra.busca_por_identificador(id_compra)
    atrs = compra.obtem_atributos(cpr)
  conteudo = gera_html_form.preencher_endereco(id_compra, atrs)
  pagina = generica(ses, conteudo, erros)
  return pagina


def escolher_pagamento(ses, id_compra, atrs, erros):
  if atrs == None:
    # Obtém atributos correntes da compra:
    cpr = compra.busca_por_identificador(id_compra)
    atrs = compra.obtem_atributos(cpr)
  # !!! Completar !!!
  conteudo = gera_html_form.escolher_pagamento(id_compra, atrs)
  pagina = generica(ses, conteudo, erros)
  return pagina

def mostra_carrinho(ses, erros):
  if ses == None:
    erros = [ "É necessário fazer login para esta função", ] + (erros if erros != None else [])
    pagina = mensagem_de_erro(ses, erros)
    conteudo = ""
  else:
    carrinho = sessao.obtem_carrinho(ses)
    conteudo = gera_html_elem.bloco_de_compra(carrinho, True)

  pagina = generica(ses, conteudo, erros)
  return pagina

def mostra_compra(ses, cpr, erros):
  detalhe = True
  conteudo = gera_html_elem.bloco_de_compra(cpr, True)
  pagina = generica(ses, conteudo, erros)
  return pagina

def cadastrar_usuario(ses, atrs, erros):
  # Quem está cadastrando é administrador?
  if ses != None:
    usr_ses = sessao.obtem_usuario(ses)
    atrs_ses = usuario.obtem_atributos(usr_ses)
    admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)
  else:
    admin = False
  # Constrói formulário com dados:
  html_dados = gera_html_form.cadastrar_usuario(atrs, admin)
  conteudo = html_dados
  # Monta a página:
  pagina = generica(ses, conteudo, erros)
  return pagina

def alterar_usuario(ses, id_usuario, atrs, erros):
  # Quem está cadastrando é administrador?
  if ses == None:
    # Não deveria acontecer:
    erro_prog("usuário deveria estar logado")

  usr_ses = sessao.obtem_usuario(ses)
  atrs_ses = usuario.obtem_atributos(usr_ses)
  admin = (atrs_ses['administrador'] if 'administrador' in atrs_ses else False)

  # Constrói formulário com dados:
  conteudo = gera_html_form.alterar_usuario(id_usuario, atrs, admin)
  # Monta a página:
  pagina = generica(ses, conteudo, erros)
  return pagina

def mostra_sessao(ses, erros):
  if ses:
    s = ses.__dict__

    id_sessao = "<b>Id da sessao:</b> " + str(s['id_sessao'])
    abrt = "<br><b>Sessao aberta:</b> " + str(s['atrs']['abrt']) 
    cookie = "<br><b>Cookie:</b> " + str(s['atrs']['cookie']) 
    dic_carrinho =  pprint.pformat(s['atrs']['carrinho'].__dict__, indent=5)
    dic_usr = pprint.pformat(s['atrs']['usr'].__dict__, indent=5)
    carrinho = "<br><b>Carrinho:</b><br>" + dic_carrinho
    usr = "<br><b>Usuario:</b><br>" + dic_usr

    html_conteudo = id_sessao + abrt + cookie + "<br>" + usr + "<br>" + carrinho
    pagina = generica(ses, html_conteudo, None)
  else:
    pagina =  generica(ses, "", "Sessão não encontrada")
  
  return pagina

def mensagem_de_erro(ses, msg):
  pagina = generica(ses, "", msg)
  return pagina

def lista_de_compras(ses, idents, erros):
  sys.stderr.write(str(idents))
  sep = "<br/><hr/>" # Separador de blocos de compras.
  botao_nova_compra = gera_html_botao.simples("Nova Compra", 'nova_compra', None, '#eeeeee'),
  todas_cmprs = ""
  for id_item in idents:
    cmpr = itens_de_compra.busca_por_identificador(id_item)
    bloco_compra = gera_html_elem.bloco_de_compra(cmpr, False)
    todas_cmprs = todas_cmprs + sep + bloco_compra
  pagina = generica(ses, botao_nova_compra[0]+todas_cmprs + sep, erros)
  return pagina
