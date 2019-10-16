# Implementação do módulo {gera_html_form}.

# Interfaces importadas por esta implementação:
import gera_html_elem
import gera_html_botao
from utils_testes import erro_prog, mostra

# Constantes
FAM_FONTE_PADRAO = "Courier"
TAM_FONTE_PADRAO = "18px"

#Funções exportadas por este módulo:

def buscar_produtos():
  cor_cinza = "#fff888"
  html_condicao = gera_html_elem.input(None, "text", "condicao", None, "Buscar o que?", None)
  html_submit_buscar = gera_html_botao.submit_buscar_produtos()
  return header_form() + \
    "    <span style=\"text-color:" + cor_cinza + ";text-align: left;\">\n" + \
    "      " + html_condicao + "\n" + \
    "    </span>\n" + \
    "    " + html_submit_buscar + "\n" + \
    bottom_form()

def ver_produto(id_produto, qtd_produto):
  html_produto = gera_html_elem.input(None, "hidden", "id_produto", id_produto, None, None)
  html_qtd = ( gera_html_elem.input(None, "hidden", "quantidade", str(qtd_produto), None, None) if qtd_produto != None else "" )
  html_submit_ver = gera_html_botao.submit_ver_produto()
  
  return header_form() + \
    ( "    " + html_produto + "\n" ) + \
    ( "    " + html_qtd + "\n" if html_qtd != "" else "" ) + \
    ( "    " + html_submit_ver + "\n" ) + \
    bottom_form()

def comprar_produto(id_compra, id_produto, qtd_produto):
  if id_compra != None:
    html_compra = gera_html_elem.input(None, "hidden", "id_compra", id_compra, None, None)
  else:
    html_compra = None
  html_produto = gera_html_elem.input(None, "readonly", "id_produto", id_produto, None, None)
  html_quantidade = gera_html_elem.input(None, "text", "quantidade", str(qtd_produto), None, "submit_alterar_quantidade")
  html_submit_comprar = gera_html_botao.submit_comprar_produto()
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_produto + "\n" ) + \
    ( "    " + html_quantidade + "\n" ) + \
    ( "    " + html_submit_comprar + "\n" ) + \
    bottom_form()

def alterar_quantidade(id_compra, id_produto, qtd_produto):
  if id_compra != None:
    html_compra = gera_html_elem.input(None, "hidden", "id_compra", id_compra, None, None)
  else:
    html_compra = None
  html_produto = gera_html_elem.input(None, "readonly", "id_produto", id_produto, None, None)
  html_quantidade = gera_html_elem.input(None, "text", "quantidade", str(qtd_produto), None, "submit_alterar_quantidade")
  html_submit_ver = gera_html_botao.submit_ver_produto()
  html_submit_excluir = gera_html_botao.submit_excluir_produto()
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_produto + "\n" ) + \
    ( "    " + html_quantidade + "\n" ) + \
    ( "    " + html_submit_ver + "\n" ) + \
    ( "    " + html_submit_excluir + "\n" ) + \
    bottom_form()

def ver_compra(id_compra):
  html_compra = gera_html_elem.input(None, "readonly", "id_compra", id_compra, None, None)
  html_submit_ver = gera_html_botao.submit_ver_compra()
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_submit_ver + "\n" ) + \
    bottom_form()

def fechar_compra(id_compra):
  html_compra = gera_html_elem.input(None, "readonly", "id_compra", id_compra, None, None)
  html_submit_fechar = gera_html_botao.submit_fechar_compra()
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_submit_fechar + "\n" ) + \
    bottom_form()

def entrar():
  html_email = gera_html_elem.input("E-mail: ", "email", "email", None, None, None)
  html_senha = gera_html_elem.input("Senha: ", "text", "senha", None, None, None)
  html_submit_entrar = gera_html_botao.submit_entrar()

  return header_form() + \
    ( "    <label>E-mail: </label>" + html_email + "\n" ) +  \
    "   <br/>" + \
    ( "    <label>Senha: </label>" + html_senha + "\n" ) + \
    "   <br/>" + \
    ( "   " + html_submit_entrar + "\n" ) + \
    bottom_form()

def header_form(fam_fonte=FAM_FONTE_PADRAO, tam_fonte=TAM_FONTE_PADRAO):
    return \
      "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">"

def bottom_form():
  return \
  "  </form>\n" + \
    "</span>"

def cadastrar_usuario():
  return cadastrar_ou_alterar_usuario(None) 
  
def alterar_usuario(usr):
  return cadastrar_ou_alterar_usuario(usr)

# FUNÇÕES INTERNAS:

def cadastrar_ou_alterar_usuario(usr):
  """Retorna o formulário de {cadastrar_usuario()} se {usr} for {None},
  ou {alterar_usuario(usr)} caso contrário."""
  
  if usr != None:
    id_usuario = usuario.obtem_identificador(usr)
    html_id_usuario = gera_html_elem.input(None, "readonly", "id_usuario", id_usuario, None, None)
    args = usuario.obtem_atributos(usr)
  else:
    id_usuario = None
    html_id_usuario = None
    args = {}
  
  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = (
    ( "Nome",            "text",     "nome",       None ),
    ( "E-mail",          "email",    "email",      "xxx@xxx.xxx.xx" ),
    ( "CPF",             "text",     "CPF",        "xxx.xxx.xxx-xx" ),
    ( "Telefone",        "text",     "telefone",   "+xx(xx)x-xxxx-xxxx" ),
    ( "Endereco",        "text",     "endereco",   "Rua e número\nBairro\nCidade, UF"),
    ( "CEP",             "text",     "CEP",        "xxxxx-xxx"),
    ( "Documento",       "text",     "documento",  "Número, tipo, órgão"),
    ( "Senha",           "password", "senha",      None), 
    ( "Confirmar senha", "password", "conf_senha", None),
  )
  
  # Converte os dados brutos das linhas para fragmentos HTML:
  linhas = [].copy()
  for rotulo, tipo, nome, dica in dados_linhas:
    html_rotulo = gera_html_elem.label(rot + ": ")
    if usr != None and (nome == CPF or nome  == email):
      # Não permite alterar CPF ou email:
      tipo = "readonly"
    # Valor corrente do atributo:
    valor = (args[nome] if nome in args else None)
    html_campo = gera_html_elem.input(None, tipo, nome, valor, None, None)
    linhas.append((html_rotulo, html_campo,))

  # Monta a tabela com os fragmentos HTML:
  html_tabela = gera_html_elem.tabela(4, linhas)
  
  if usr == None:
    html_submit = gera_html_botao.submit_cadastrar_usuario()
  else:
    html_submit = gera_html_botao.submit_alterar_usuario()
  
  return header_form() + \
    ( "    " + html_id_usuario + "\n" if id_usuario != None else "") + \
    ( html_tabela + "\n" ) + \
    ( "    " + html_submit + "\n" ) + \
    bottom_form()

