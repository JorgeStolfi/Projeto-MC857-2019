# Implementação do módulo {gera_html_form}.

# Interfaces importadas por esta implementação:
import sys
import gera_html_elem
import gera_html_botao
import usuario
import compra
import sys
from utils_testes import erro_prog, mostra

#Funções exportadas por este módulo:

def buscar_produtos():
  cor_cinza = "#fff888"
  estilo = "text-color:" + cor_cinza + ";" + " text-align: left;"
  html_cond_input = gera_html_elem.input(None, "text", "condicao", None, "Buscar o que?", None)
  html_condicao = gera_html_elem.span(estilo, html_cond_input)
  html_submit_buscar = gera_html_botao.submit("Buscar", 'buscar_produtos', None, '#ed3330')
  html_campos = html_condicao  + " " + html_submit_buscar
  return monta_formulario(html_campos)

def buscar_objeto():
  cor_cinza = "#fff888"
  estilo = "text-color:" + cor_cinza + ";" + " text-align: left;"
  html_cond_input = gera_html_elem.input(None, "text", "id_objeto", None, "Identificador", None)
  html_condicao = gera_html_elem.span(estilo, html_cond_input)
  html_submit_buscar = gera_html_botao.submit("Buscar", 'ver_objeto', None, '#ed3330')
  html_campos = html_condicao  + " " + html_submit_buscar
  return monta_formulario(html_campos)

def ver_produto(id_produto, qtd_produto):
  html_id_produto = gera_html_elem.input(None, "hidden", "id_produto", id_produto, None, None)
  html_qtd = ( gera_html_elem.input(None, "hidden", "quantidade", str(qtd_produto), None, None) if qtd_produto != None else "" )
  html_submit_ver = gera_html_botao.submit("Ver", 'ver_produto', None, '#60a3bc')
  
  html_campos = \
    html_id_produto + \
    ( html_qtd if html_qtd != "" else "" ) + \
    html_submit_ver
  
  return monta_formulario(html_campos)

def trocar_carrinho(id_compra):
  html_submit_usar = gera_html_botao.submit("Usar como carrinho", 'trocar_carrinho', {'id_compra': id_compra}, '#ffdd22')
  html_campos = html_submit_usar
  return monta_formulario(html_campos)

def comprar_produto(id_compra, id_produto, qtd_produto):
  if id_compra != None:
    html_compra = gera_html_elem.input(None, "hidden", "id_compra", id_compra, None, None)
  else:
    html_compra = None
  html_produto = gera_html_elem.input(None, "readonly", "id_produto", id_produto, None, None)
  html_quantidade = gera_html_elem.input(None, "text", "quantidade", str(qtd_produto), None, "alterar_qtd_de_produto")
  html_submit_comprar = gera_html_botao.submit("Comprar", 'comprar_produto', None, '#55ee55')
  html_campos = \
    ( html_compra if html_compra != None else "" ) + \
    html_produto + \
    html_quantidade + \
    html_submit_comprar
  return monta_formulario(html_campos)

def alterar_quantidade(id_compra, id_produto, qtd_produto):
  if id_compra != None:
    html_compra = gera_html_elem.input(None, "hidden", "id_compra", id_compra, None, None)
  else:
    html_compra = None
  html_produto = gera_html_elem.input(None, "readonly", "id_produto", id_produto, None, None)
  html_quantidade = gera_html_elem.input(None, "text", "quantidade", str(qtd_produto), None, "alterar_qtd_de_produto")
  html_submit_ver = gera_html_botao.submit("Ver", 'ver_produto', None, '#60a3bc')
  html_submit_excluir = gera_html_botao.submit("Excluir", 'excluir_item_de_compra', None, '#55ee55')
  html_campos = \
    ( html_compra if html_compra != None else "" ) + \
    html_produto + \
    html_quantidade + \
    html_submit_ver + \
    html_submit_excluir
  return monta_formulario(html_campos)

def ver_compra(id_compra):
  html_compra = gera_html_elem.input(None, "readonly", "id_compra", id_compra, None, None)
  html_submit_ver = gera_html_botao.submit("Ver", 'ver_compra', None, '#60a3bc')
  html_campos = \
    ( html_compra if html_compra != None else "" ) + \
    tml_submit_ver
  return monta_formulario(html_campos)

def fechar_compra(id_compra):
  html_compra = gera_html_elem.input(None, "readonly", "id_compra", id_compra, None, None)
  html_submit_fechar = gera_html_botao.submit("Fechar compra", 'fechar_compra', None, '#55ee55')
  html_campos = \
    ( html_compra if html_compra != None else "" ) + \
    html_submit_fechar
  return monta_formulario(html_campos)

def excluir_item_de_compra(prod_id, compr_id):
  return alterar_qtd_de_produto(0.0, prod_id, compr_id)

def alterar_qtd_de_produto(qtd, prod_id, compr_id):
  html_qtd = gera_html_elem.input(None, "number", "quantidade", str(qtd), None, None)
  html_pid_escondido = gera_html_elem.input(None, "hidden", "id_produto", str(prod_id), None, None)
  html_cid_escondido = gera_html_elem.input(None, "hidden", "id_compra", str(compr_id), None, None)
  html_botao = gera_html_botao.submit("Atualizar", 'alterar_qtd_de_produto', None, '#55ee55')
  html_campos = \
    html_qtd +  \
    html_pid_escondido + \
    html_cid_escondido + \
    html_botao
  return monta_formulario(html_campos)

def entrar():
  linhas = [].copy()
  html_rotulo = gera_html_elem.label("E-mail", ": ")
  html_campo = gera_html_elem.input(None, "text", "email", None, None, None)
  linhas.append((html_rotulo, html_campo,))
  html_rotulo = gera_html_elem.label("Senha", ": ")
  html_campo = gera_html_elem.input(None, "password", "senha", None, None, None)
  linhas.append((html_rotulo, html_campo,))

  # Monta a tabela com os fragmentos HTML:
  html_tabela = gera_html_elem.tabela(linhas)
  
  html_bt_login = gera_html_botao.submit("Entrar", 'fazer_login', None, '#55ee55')

  html_campos = \
    html_tabela + \
    html_bt_login

  return monta_formulario(html_campos)
  
def cadastrar_usuario(atrs, admin):
  return dados_de_usuario(None, atrs, admin, "Cadastrar", "cadastrar_usuario")

def alterar_usuario(id_usuario, atrs, admin):
  return dados_de_usuario(id_usuario, atrs, admin, "Confirmar", "alterar_usuario")

def dados_de_usuario(id_usuario, atrs, admin, texto_bt, cmd):
  """Se {id_usuario} é {None}, retorna formulário de cadastrar novo usuário.
  Senão retorma o formulário para alterar os dados do usuário existente {usr} 
  cujo identificador é {id_usuario} e cujos atributos atuais estão em {atrs}.
  
  O formulário terá um botão "submit" com texto {texto_bt} e ação POST {cmd}."""

  if id_usuario != None:
    novo = False
    # Inclui campo 'id_usuario' no formulário:
    if admin != None:
      # Mostra o id do usuario somente se quem está alterando é administrador:
      html_id_usuario = gera_html_elem.input(None, "readonly", "id_usuario", id_usuario, None, None)
    else:
      html_id_usuario = gera_html_elem.input(None, "hidden", "id_usuario", id_usuario, None, None)
  else:
    novo = True
    html_id_usuario = ""
    
  # For simplicity:
  if atrs == None: atrs = {}.copy()
      
  # Substitui o atributo 'endereco' por 4 campos 'endereco_1', 'endereco_2', 'cidade_UF'
  quebra_endereco(atrs)

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = (
    ( "Nome",             "text",     "nome",          None,                  False, ),
    ( "E-mail",           "email",    "email",         "xxx@xxx.xxx.xx",      False, ),
    ( "CPF",              "text",     "CPF",           "xxx.xxx.xxx-xx",      False, ),
    ( "Telefone",         "text",     "telefone",      "+xx(xx)x-xxxx-xxxx",  False, ),
    ( "Endereço",         "text",     "endereco_1",    "Linha 1",             False, ),
    ( None,               "text",     "endereco_2",    "Linha 2",             False, ),
    ( "Cidade, UF",       "text",     "cidade_UF",     "Cidade, UF",          False, ),
    ( "CEP",              "text",     "CEP",           "xxxxx-xxx",           False, ),
    ( "Documento",        "text",     "documento",     "Número, tipo, órgão", False, ),
    ( "Senha",            "password", "senha",         None,                  False, ),
    ( "Confirmar senha",  "password", "conf_senha",    None,                  False, ),
    ( "Administrador",    "checkbox", "administrador", None,                  False, ),
  )
  
  html_tabela = tabela_de_campos(dados_linhas, atrs, admin)

  html_submit = gera_html_botao.submit(texto_bt, cmd, None, '#55ee55')

  html_cancel = gera_html_botao.simples("Cancelar", 'principal', None, '#ee5555')
  
  html_campos = \
    ( "    " + html_id_usuario + "\n" if html_id_usuario != "" else "") + \
    ( html_tabela + "\n" ) + \
    ( "    " + html_submit + "\n" ) + \
    ( "    " + html_cancel + "\n" )
  return monta_formulario(html_campos)

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
    "<span style=\"" + \
    " display: inline-block;" + \
    " font-family:" + fam_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    " padding: 5px;" + \
    "\">" + \
    "<form method=\"post\">" + \
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
    "  </form>" + \
    "</span>"

def preencher_endereco(id_compra, atrs):

  assert id_compra != None

  cpr = compra.busca_por_identificador(id_compra)
  atrs_cpr = compra.obtem_atributos(cpr)

  # Copia os atributos de endereço (apenas) a compra:
  novo_atrs = {}.copy()
  novo_atrs['id_compra'] = id_compra
  novo_atrs['endereco'] = (atrs_cpr['endereco'] if 'endereco' in atrs_cpr else None)
  novo_atrs['CEP'] = (atrs_cpr['CEP'] if 'CEP' in atrs_cpr else None)
  quebra_endereco(novo_atrs)

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, dica, e {adm_only}.
  dados_linhas = (
    ( "Compra",              "readonly", "id_compra",     None,         False, ),
    ( "Endereço",            "text",     "endereco_1",    "Linha 1",    False, ),
    ( None,                  "text",     "endereco_2",    "Linha 2",    False, ),
    ( "Cidade, UF",          "text",     "cidade_UF",     "Cidade, UF", False, ),
    ( "CEP",                 "text",     "CEP",           "xxxxx-xxx",  False, ),
  )

  html_tabela = tabela_de_campos(dados_linhas, novo_atrs, False)

  html_submit = gera_html_botao.submit("Confirmar", 'definir_endereco', None, '#55ee55')
  
  html_campos = \
    html_tabela + \
    html_submit

  return monta_formulario(html_campos)

def buscar_identificador():
  cor_cinza = "#fff888"
  html_condicao = gera_html_elem.input(None, "text", "id", None, "Identificador", None)
  html_submit_ver_produto = gera_html_botao.submit("Ver", 'ver_objeto', None, '#eeeeee')
  html_campos = \
    html_condicao + \
    html_submit_ver_produto

  return monta_formulario(html_campos)

# FUNÇÕES INTERNAS:
  
def tabela_de_campos(dados_linhas, atrs, admin):
  """Retorna HTML de uma tabela com duas colunas: rótulos "<label>...<label/> e campos 
  editáveis <input.../>".  Os valores iniciais dos campos são obtidos do 
  dicionário {atrs}.  O parâmetro booleano {admin} diz se o usuário
  que pediu o formulário é administrador ({True}) ou cliente ({False}).
  
  O parâmetro {dados_linhas} é uma seqüência de quíntuplas
  {(rot,tipo,chave,dica,adm_only)}, uma para cada linha da tabela. 
  
  O elemento {rot} é o texto a mostrar no rótulo, ou {None} para omitir o rótulo.
  O elemento {adm_only} é um booleano que diz se o campo só deve ser editável 
  para administradores. Se for {True}, o campo será "readonly" para usuários normais.
  
  O campo editável será 
  "<input type='{tipo}' name='{chave}' id='{chave}' value='{val}' placeholder='{dica}'/>"
  onde {val} é o valor {args[chave]} apropriadamente convertido para HTML.
  Se o {tipo} for "numeric" também tem "min='1'."""

  sys.stderr.write("TABELA: atrs = %s\n" %str(atrs))

  # Converte os dados brutos das linhas para fragmentos HTML:
  linhas = [].copy()
  for rot, tipo, chave, dica, adm_only in dados_linhas:
    if admin or not adm_only:
      # Valor corrente do atributo:
      val = (atrs[chave] if chave in atrs else None)
      # Converte {rot} para rótulo HTML:
      html_rotulo = gera_html_elem.label(rot, ": ")
      # Cria o elemento "<input .../>":
      html_campo = campo_editavel(tipo, chave, val, dica)
      if html_campo != None:
        linhas.append((html_rotulo, html_campo,))

  # Monta a tabela com os fragmentos HTML:
  html_tabela = gera_html_elem.tabela(linhas)
  
  return html_tabela

def campo_editavel(tipo, chave, val, dica):
  """Retorna o HTML de um item "input" do formulário
  de dados de usuário. Pode devolver {None} para não mostrar esse item.
  
  O elemento terá o dado {tipo} ("text", "password", etc.), nome {chave}, 
  valor inicial {val}, e a {dica} especificada (se {val} for {None}). 
  O valor inicial {val} é convertido para string de maneira adequada
  ao seu tipo.
  
  Se a chave for 'senha', não mostra o {val}"""

  if chave == 'senha': val = None

  # Converte val para HTML:
  if val == None:
    html_valor = None
  elif type(val) is str:
    html_valor = val
  elif type(val) is bool:
    html_valor = ('on' if val else 'off')
  elif type(val) is float:
    html_valor = ("%.2f" % val)
  elif type(val) is int:
    html_valor = ("%d" % val)
  else:
    erro_prog("valor inválido = \"" + str(val) + "\"")

  # Dica e valor inicial são mutuamente exclusivos: 
  if html_valor == None:
    html_dica = dica
  else:
    html_dica = None

  html_campo = gera_html_elem.input(None, tipo, chave, html_valor, html_dica, None)
  return html_campo

def quebra_endereco(atrs):
  """Quebra-galho.  Substitui o campo 'endereco' no dicionário {atrs}, se existir,
  por tres campos, 'endereco_1', 'endereco_2', e 'cidade_UF'."""
  if 'endereco' in atrs and atrs['endereco'] != None:
    linhas_endereco = atrs['endereco'].split('\n')
    atrs['endereco_1'] = linhas_endereco[0]
    atrs['endereco_2'] = linhas_endereco[1]
    atrs['cidade_UF'] = linhas_endereco[2]
    del atrs['endereco']

def monta_formulario(conteudo):
  """Dado um trecho de HTML {conteudo} que define os campos "<input ...>" necessários, envolve o mesmo 
  em "<form>...</form>", com rótulos etc num estilo padrão."""
  fam_fonte = "Courier"
  peso_fonte = None
  tam_fonte = "18px"
  estilo = \
    "  display: inline-block;" + \
    "  font-family: " + fam_fonte + ";" + \
    "  font-size: " + tam_fonte + ";" + \
    "  padding: 5px;"
  html_cru = gera_html_elem.form(None, conteudo)
  html = gera_html_elem.span(estilo, html_cru)
  return html
