# Implementação do módulo {gera_html_form}.

# Interfaces importadas por esta implementação:
import gera_html_elem
import gera_html_botao
import usuario
from utils_testes import erro_prog, mostra

# Constantes
FAM_FONTE_PADRAO = "Courier"
TAM_FONTE_PADRAO = "18px"

#Funções exportadas por este módulo:

def buscar_produtos():
  cor_cinza = "#fff888"
  html_condicao = gera_html_elem.input(None, "text", "condicao", None, "Buscar o que?", None)
  html_submit_buscar = gera_html_botao.submit("Buscar", 'buscar_produtos', None, '#eeeeee')
  return header_form() + \
    "    <span style=\"text-color:" + cor_cinza + ";text-align: left;\">\n" + \
    "      " + html_condicao + "\n" + \
    "    </span>\n" + \
    "    " + html_submit_buscar + "\n" + \
    bottom_form()

def ver_produto(id_produto, qtd_produto):
  html_produto = gera_html_elem.input(None, "hidden", "id_produto", id_produto, None, None)
  html_qtd = ( gera_html_elem.input(None, "hidden", "quantidade", str(qtd_produto), None, None) if qtd_produto != None else "" )
  html_submit_ver = gera_html_botao.submit("Ver", 'ver_produto', None, '#eeeeee')
  
  return header_form() + \
    ( "    " + html_produto + "\n" ) + \
    ( "    " + html_qtd + "\n" if html_qtd != "" else "" ) + \
    ( "    " + html_submit_ver + "\n" ) + \
    bottom_form()

def trocar_carrinho(id_compra):
    fam_fonte = "Courier"
    tam_fonte = "18px"
    html_submit_ver = gera_html_botao.submit("Usar como carrinho", 'trocar_carrinho', {'id_compra': id_compra}, '#ffdd22')
    return \
     "<span style=\"\n" + \
     "  display: inline-block;\n" + \
     "  font-family:" + fam_fonte + ";\n" + \
     "  font-size:" + tam_fonte + ";\n" + \
     "  padding: 5px;\n" + \
     "\">\n" + \
     "  <form method=\"post\">\n" + \
     ( "    " + id_compra + "\n" ) + \
     ( "    " + html_submit_ver + "\n" ) + \
     "  </form>\n" + \
     "</span>"

def comprar_produto(id_compra, id_produto, qtd_produto):
  if id_compra != None:
    html_compra = gera_html_elem.input(None, "hidden", "id_compra", id_compra, None, None)
  else:
    html_compra = None
  html_produto = gera_html_elem.input(None, "readonly", "id_produto", id_produto, None, None)
  html_quantidade = gera_html_elem.input(None, "text", "quantidade", str(qtd_produto), None, "alterar_qtd_de_produto")
  html_submit_comprar = gera_html_botao.submit("Comprar", 'comprar_produto', None, '#55ee55')
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
  html_quantidade = gera_html_elem.input(None, "text", "quantidade", str(qtd_produto), None, "alterar_qtd_de_produto")
  html_submit_ver = gera_html_botao.submit("Ver", 'ver_produto', None, '#eeeeee')
  html_submit_excluir = gera_html_botao.submit("Excluir", 'excluir_item_de_compra', None, '#55ee55')
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_produto + "\n" ) + \
    ( "    " + html_quantidade + "\n" ) + \
    ( "    " + html_submit_ver + "\n" ) + \
    ( "    " + html_submit_excluir + "\n" ) + \
    bottom_form()

def ver_compra(id_compra):
  html_compra = gera_html_elem.input(None, "readonly", "id_compra", id_compra, None, None)
  html_submit_ver = gera_html_botao.submit("Ver", 'ver_compra', None, '#eeeeee')
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_submit_ver + "\n" ) + \
    bottom_form()

def fechar_compra(id_compra):
  html_compra = gera_html_elem.input(None, "readonly", "id_compra", id_compra, None, None)
  html_submit_fechar = gera_html_botao.submit("Fechar compra", 'fechar_compra', None, '#55ee55')
  return header_form() + \
    ( "    " + html_compra + "\n" if html_compra != None else "" ) + \
    ( "    " + html_submit_fechar + "\n" ) + \
    bottom_form()

def entrar():
  html_email = gera_html_elem.input("E-mail: ", "email", "email", None, None, None)
  html_senha = gera_html_elem.input("Senha: ", "text", "senha", None, None, None)
  html_fazer_login = gera_html_botao.submit("Entrar", 'fazer_login', None, '#55ee55')

  return header_form() + \
    ( "    <label>E-mail: </label>" + html_email + "\n" ) +  \
    "   <br/>" + \
    ( "    <label>Senha: </label>" + html_senha + "\n" ) + \
    "   <br/>" + \
    ( "   " + html_fazer_login + "\n" ) + \
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
  return definir_dados_de_usuario(None)

def alterar_usuario(usr):
  return definir_dados_de_usuario(usr)

# FUNÇÕES INTERNAS:

def definir_dados_de_usuario(usr):
  """Retorna o formulário de {cadastrar_usuario()} se {usr} for {None},
  ou {alterar_usuario(usr)} caso contrário."""

  if usr != None:
    id_usuario = usuario.obtem_identificador(usr)
    args = usuario.obtem_atributos(usr)
    if (args['administrador']==True):
      html_id_usuario = gera_html_elem.input(None, "text", "id_usuario", id_usuario, None, None)
    else:
      html_id_usuario = ""
  else:
    id_usuario = None
    html_id_usuario = None
    args = {}

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = (
    ( "Nome",            "text",     "nome",          None ),
    ( "E-mail",          "email",    "email",         "xxx@xxx.xxx.xx" ),
    ( "CPF",             "text",     "CPF",           "xxx.xxx.xxx-xx" ),
    ( "Telefone",        "text",     "telefone",      "+xx(xx)x-xxxx-xxxx" ),
    ( "Endereco",        "text",     "endereco",      "Rua e número\nBairro\nCidade, UF"),
    ( "CEP",             "text",     "CEP",           "xxxxx-xxx"),
    ( "Documento",       "text",     "documento",     "Número, tipo, órgão"),
    ( "Senha",           "password", "senha",         None),
    ( "Confirmar senha", "password", "conf_senha",    None),
    ( "Administrador",   "checkbox", "administrador", None),
  )

  # Converte os dados brutos das linhas para fragmentos HTML:
  linhas = [].copy()
  for rotulo, tipo, nome, dica in dados_linhas:
    html_rotulo = gera_html_elem.label(rotulo + ": ")
    if usr != None and (nome == 'CPF' or nome == 'email'):
      # Não permite alterar CPF ou email:
      tipo = "readonly"
    # Valor corrente do atributo:
    valor = (args[nome] if nome in args else None)
    # Converte para HTML:
    if valor == None:
      valor_html = None
    elif type(valor) is str:
      valor_html = valor
    elif type(valor) is bool:
      valor_html = ('on' if valor else 'off')
    elif type(valor) is float:
      valor_html = ("%.2f" % valor)
    elif type(valor) is int:
      valor_html = ("%d" % valor)
    else:
      erro_prog("valor inválido = \"" + str(valor) + "\"")
    html_campo = gera_html_elem.input(None, tipo, nome, valor_html, None, None)
    linhas.append((html_rotulo, html_campo,))

  # Monta a tabela com os fragmentos HTML:
  html_tabela = gera_html_elem.tabela(linhas)

  if usr == None:
    html_submit = gera_html_botao.submit("Cadastrar", 'definir_dados_de_usuario', None, '#55ee55')
  else:
    html_submit = gera_html_botao.submit("Alterar", 'definir_dados_de_usuario', None, '#55ee55')
  
  return header_form() + \
    ( "    " + html_id_usuario + "\n" if id_usuario != None else "") + \
    ( html_tabela + "\n" ) + \
    ( "    " + html_submit + "\n" ) + \
    bottom_form()

def escolher_pagamento():
  fam_fonte = "Courier"
  tam_fonte = "18px"
  html_nome = gera_html_elem.input("Nome: ", "text", "Nome", None, None, None)
  html_num1 = gera_html_elem.input("Número do cartão: ", "text", "n1", None, None, None)
  html_num2 = gera_html_elem.input(" - " , "text", "n2", None, None, None)
  html_num3 = gera_html_elem.input(" - ", "text", "n3", None, None, None)
  html_num4 = gera_html_elem.input(" - ", "text", "n4", None, None, None)
  html_val = gera_html_elem.input("Data de validade: ", "text", "mes_val", None, None, None)
  html_val2 = gera_html_elem.input("/", "text", "ano_val", None, None, None)
  html_sec = gera_html_elem.input("Código de segurança: ", "number", "código de segurança", None, None, None)
  html_submit = gera_html_botao.submit("Confirmar", 'definir_forma_de_pagamento', None, '#55ee55')
  return \
        "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "\">\n" + \
    "  <form method=\"post\">" + \
    (  html_nome + "\n" ) +  \
    "   <br/>" + \
    (  html_num1 + "\n" ) + \
    (  html_num2 + "\n" ) + \
    (  html_num3 + "\n" ) + \
    (  html_num4 + "\n" ) + \
    "   <br/>" + \
    (  html_val + "\n" ) + \
    (  html_val2 + "\n" ) + \
    "   <br/>" + \
    (  html_sec + "\n" ) + \
    (  html_submit + "\n" ) + \
    "   <br/>" + \
    "  </form>\n" + \
    "</span>"
