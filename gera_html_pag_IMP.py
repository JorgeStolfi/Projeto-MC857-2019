# Implementação do módulo {gera_html_pag}.

# Interfaces importadas por este módulo:
import gera_html_elem, gera_html_form, gera_html_botao

# Outras interfaces usadas por este módulo:
from datetime import datetime, timezone
import produto
  
def generica(conteudo):
  cabe = gera_html_elem.cabecalho("Projeto MC857A 2019-2s")
  menu = gera_html_elem.menu_geral()
  roda = gera_html_elem.rodape()
  return cabe + "\n" + menu + "\n" + conteudo + "\n" + roda

def entrada_da_loja():
  now = datetime.now(timezone.utc)
  data = now.strftime("%Y-%m-%d %H:%M:%S %z")
  texto = "<hr/><i>DATA CORRENTE</i><br/><b>" + data + "</b><br/>TUDO EM ORDEM NESTE SERVIDOR<hr/>"
  
  cor_texto = "#000488"
  cor_fundo = "#fff844"
  conteudo = gera_html_elem.bloco_texto(texto,"Courier","18px","normal","5px","center",cor_texto,cor_fundo)
  pagina = generica(conteudo)
  return pagina

def mostra_produto(prod, qt):
  conteudo = gera_html_elem.bloco_de_produto(prod, qt, True)
  pagina = generica(conteudo)
  return pagina

def lista_de_produtos(idents):
  sep = gera_html_elem.div("\n  clear: left;", "<hr/>") # Separador de blocos de produtos.
  todos_prods = ""
  for id_prod in idents:
    prod = produto.busca_por_identificador(id_prod)
    bloco_prod = gera_html_elem.bloco_de_produto(prod, None, False)
    todos_prods = todos_prods + sep + bloco_prod
  pagina = generica(todos_prods + sep)
  return pagina

def entrar():
  conteudo = gera_html_form.entrar()
  pagina = generica(conteudo)
  return pagina

def cadastrar_usuario():
  conteudo = gera_html_form.cadastrar_usuario()
  pagina = generica(conteudo) 
  return pagina

def mostra_compra(comp):
  conteudo = gera_html_form.mostra_compra(comp)
  pagina = generica(conteudo) 
  return pagina

def mostra_usuario(usr):
  conteudo = gera_html_elem.informacao_usuario(usr)
  pagina = generica(conteudo)
  return pagina

def erro_busca_produto(msg):
  conteudo = gera_html_form.erro_generico(msg)
  pagina = generica(conteudo)
  return pagina