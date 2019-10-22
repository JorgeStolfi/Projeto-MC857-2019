# Implementação do módulo {gera_html_pag}.

# Interfaces do projeto importadas por este módulo:
import produto
import sessao
import usuario
import compra
import gera_html_elem
import gera_html_form
import gera_html_botao
from utils_testes import erro_prog, mostra

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone
  
def generica(ses, conteudo):
  cabe = gera_html_elem.cabecalho("Projeto MC857A 2019-2s", True)
  logado = (ses != None)
  if logado:
    usr = sessao.obtem_usuario(ses)
    nome_usuario = usuario.obtem_atributos(usr)['nome']
  else:
    nome_usuario = None
  menu = gera_html_elem.menu_geral(logado, nome_usuario)
  roda = gera_html_elem.rodape()
  return cabe + "\n" + menu + "\n" + conteudo + "\n" + roda

def principal(ses):
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto = "<hr/><i>DATA CORRENTE</i><br/><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  
  cor_texto = "#000488"
  cor_fundo = "#fff844"
  conteudo = gera_html_elem.bloco_texto(texto, None,"Courier","18px","normal","5px","center", cor_texto, cor_fundo)
  pagina = generica(ses, conteudo)
  return pagina

def mostra_produto(ses, id_compra, prod, qtd):
  conteudo = gera_html_elem.bloco_de_produto(id_compra, prod, qtd, True)
  pagina = generica(ses, conteudo)
  return pagina

def lista_de_produtos(ses, idents):
  sep = gera_html_elem.div("\n  clear: left;", "<hr/>") # Separador de blocos de produtos.
  todos_prods = ""
  for id_prod in idents:
    prod = produto.busca_por_identificador(id_prod)
    bloco_prod = gera_html_elem.bloco_de_produto(None, prod, None, False)
    todos_prods = todos_prods + sep + bloco_prod
  pagina = generica(ses, todos_prods + sep)
  return pagina

def entrar(ses):
  conteudo = gera_html_form.entrar()
  pagina = generica(ses, conteudo)
  return pagina

def cadastrar_usuario(ses):
  conteudo = gera_html_form.cadastrar_usuario()
  pagina = generica(ses, conteudo) 
  return pagina

def mostra_carrinho(ses):
  if ses != None:
    carrinho = sessao.obtem_carrinho(ses)
    conteudo = gera_html_elem.bloco_de_compra(carrinho, True)
    pagina = generica(ses, conteudo)
  else:
    pagina = mensagem_de_erro(ses, "É necessário fazer login para esta função")
  return pagina

def mostra_compra(ses, cpr):
  detalhe = True
  conteudo = gera_html_elem.bloco_de_compra(cpr, True)
  pagina = generica(ses, conteudo) 
  return pagina

def mostra_usuario(ses, usr):
  conteudo = gera_html_form.alterar_usuario(usr)
  pagina = generica(ses, conteudo)
  return pagina

def mensagem_de_erro(ses, msg):
  conteudo = gera_html_elem.bloco_de_erro(msg)
  pagina = generica(ses, conteudo)
  return pagina

def lista_de_compras(ses, idents):
  sep = gera_html_elem.div("\n  clear: left;", "<hr/>") # Separador de blocos de compras.
  todas_cmprs = ""
  for id_cmpr in idents:
    cmpr = compra.busca_por_identificador(id_cmpr)
    bloco_compra = gera_html_elem.bloco_de_compra(cmpr, False)
    todas_cmprs = todas_cmprs + sep + bloco_compra
  pagina = generica(ses, todas_cmprs + sep)
  return pagina
