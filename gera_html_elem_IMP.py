# Implementação do módulo {gera_html_elem}.

# Interfaces do projeto importadas por esta implementação:
import gera_html_form
import gera_html_elem
import gera_html_botao
import produto
import compra
import usuario
from utils_testes import erro_prog

# Outros módulos importados por esta implementação:
from datetime import datetime, timezone
import re
import sys

#Funções exportadas por este módulo:

def cabecalho(title, grande):

  if grande:
    header_title = "<h1>" + title + "</h1>"
  else:
    header_title = "<h2>" + title + "</h2>"

  return \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + title + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n" + \
    header_title

def rodape():
  nowraw = datetime.now(timezone.utc)
  nowfmt = nowraw.strftime("%Y-%m-%d %H:%M:%S %z")
  return \
    "<small><p>\n" + \
    "Page created on " + nowfmt + "\n" + \
    "</p></small>\n" + \
    "</body>\n" + \
    "</html>\n"

def menu_geral(logado, nome_usuario, admin):
  html_menu = menu_geral_linha(menu_geral_botoes_linha_1(logado, nome_usuario, admin))
  if admin:
    html_menu += menu_geral_linha(menu_geral_botoes_linha_2())
  return html_menu

def menu_geral_linha(botoes):
  """Monta uma linha do menu geral, dada uma lista de fragmentos HTML que
  descrevem os botões."""
  html = "<nav>"
  for bt in botoes:
    html += "  " + bt
  html += "</nav>"
  return html

def menu_geral_botoes_linha_1(logado, nome_usuario, admin):
  """Gera uma lista de fragmentos de HTML que descrevem os botões da linha 1 do menu
  geral.  Estes botões são mostrados para todos os usuários, mas
  dependem do tipo de usuário (normal ou administrador) e se o
  usuário está logado."""

  # Botões da primeira linha que sempre aparecem:
  html_bt_principal = gera_html_botao.simples("Principal", 'principal', None, '#60a3bc')
  html_bt_ofertas = gera_html_botao.simples("Ofertas", 'ver_ofertas', None, '#ffdd22')
  html_fm_buscar = gera_html_form.buscar_produtos()
  botoes = ( html_bt_principal, html_bt_ofertas, html_fm_buscar)
  if logado:
    # Gera outros botões de usuario normal logado
    botoes += menu_geral_botoes_linha_1_logado(nome_usuario, admin)
  else:
    # Gera outros botões de usuário deslogado:
    botoes += menu_geral_botoes_linha_1_deslogado()
  return botoes

def menu_geral_botoes_linha_1_logado(nome_usuario, admin):
  """Gera uma lista de fragmentos HTML com os botões da linha 1 do menu
  geral, para um usuário que está logado."""
  if admin:
    botoes = (
    gera_html_botao.simples("Minha Conta", 'solicitar_form_de_alterar_usuario', None, '#eeeeee'),
    gera_html_botao.simples("Sair", 'fazer_logout', None, '#eeeeee'),
    bloco_texto("Oi " + nome_usuario, "inline_block", "Courier", "18px", "bold", None, None, None, None),
  )
  else:
    botoes = ( 
      gera_html_botao.simples("Meu Carrinho", 'ver_carrinho', None, '#eeeeee'),
      gera_html_botao.simples("Minhas Compras", 'buscar_compras', None, '#eeeeee'),
      gera_html_botao.simples("Minha Conta", 'solicitar_form_de_alterar_usuario', None, '#eeeeee'),
      gera_html_botao.simples("Sair", 'fazer_logout', None, '#eeeeee'),
      bloco_texto("Oi " + nome_usuario, "inline_block", "Courier", "18px", "bold", None, None, None, None),
    )
  return botoes

def menu_geral_botoes_linha_1_deslogado():
  """Gera uma lista de fragmentos HTML com os botões da linha 1 do menu
  geral, para um usuário que não está logado."""
  botoes = (
    gera_html_botao.simples("Entrar", 'solicitar_form_de_login', None, '#55ee55'),
    gera_html_botao.simples("Cadastrar", 'solicitar_form_de_cadastrar_usuario', None, '#eeeeee'),
  )
  return botoes

def menu_geral_botoes_linha_2():
  """Gera uma lista de fragmentos de HTML com os botões da linha 2 do menu
  geral.  Estes botãoes são mostrados apenas se o usuário está logado
  e é um administrador."""

  botoes = (
    gera_html_botao.simples("Acrescentar produto", "solicitar_form_de_acrescentar_produto", None, '#ffdd22'),
    gera_html_botao.simples("Compras de produto", "buscar_compras_por_produto", None, '#eeeeee'),
    gera_html_form.buscar_objeto()
  )
  return botoes

def bloco_de_produto(id_compra, prod, qtd, detalhe, **kwargs):
  id_produto = produto.obtem_identificador(prod)
  atrs = produto.obtem_atributos(prod)
  c = kwargs.get('c', None)

  if c == '1':
      grupo = atrs['grupo']
      if grupo != None:
          return
  # Monta o parágrafo de descrição
  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

  d_curta = atrs['descr_curta']
  html_d_curta = paragrafo(estilo_parag, bloco_texto(d_curta, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  html_variedade = ""
  variedade = atrs['variedade']
  if variedade != None:
    html_variedade = paragrafo(estilo_parag, bloco_texto(variedade, None, "Courier", "20px", "bold", "2px", "left", "#000000", None))

  html_grupo = ""
  if detalhe == True:
      grupo = atrs['grupo']
      if grupo != None:
        html_grupo = paragrafo(estilo_parag, bloco_texto(grupo, None, "Courier", "20px", "bold", "2px", "left", "#000000", None))

  d_media = atrs['descr_media']
  html_d_media = paragrafo(estilo_parag, bloco_texto(d_media, None, "Courier", "16px", "normal", "0px", "left", "#000000", None))

  em_oferta = atrs['oferta']
  html_em_oferta = ""
  if em_oferta:
    html_em_oferta = paragrafo(estilo_parag, bloco_texto("OFERTA!", None, "Courier", "24px", "normal", "5px 5px 5px 5px", "center", "#000000", "#ffff00"))

  qtd_inicial = (qtd if qtd != None else 1.0) # Quantidade a pedir no formulário de ver ou comprar o produto:
  if detalhe:
    d_longa = atrs['descr_longa']
    html_d_longa = paragrafo(estilo_parag, bloco_texto(d_longa, None, "Courier", "14px", "normal", "0px", "left", "#000000", None))
    html_botao = gera_html_form.comprar_produto(id_compra, id_produto, qtd_inicial)
  else:
    html_d_longa = ""
    html_botao = gera_html_form.ver_produto(id_produto, qtd_inicial)

  str_preco = ("R$ %.2f" % preco)
  html_preco = bloco_texto(str_preco, "inline-block", "Courier", "20px", "bold", "2px", "left", "#000000", None)

  # !!! Peso e volume devem ser mostrados apenas ao mostrar detalhes do produto. !!!

  # Peso e o volume só é mostrado caseo seja detalhado
  html_peso = ""
  html_volume = ""
  if detalhe:
    peso = atrs['peso']
    str_peso  = ("%.0f gramas" % peso)
    html_peso = bloco_texto(str_peso, "inline-block", "Courier", "20px", "bold", "2px", "left", "#000000", None)

    volume = atrs['volume']
    str_volume = ("%.2f mililitros" % volume)
    html_volume = bloco_texto(str_volume, "inline-block", "Courier", "20px", "bold", "2px", "left", "#000000", None)

  html_descr = html_em_oferta + html_d_curta + html_variedade + html_grupo + html_d_media + html_d_longa + html_preco + html_botao + html_peso + html_volume

  bloco_descr = span("\n display: inline-block;", html_descr)

  tam_img = (200 if detalhe else 100)
  nome_img = atrs['imagem']
  html_img_crua = ("<img src=\"imagens/" + nome_img + "\" alt=\"" + id_produto + "\" style=\"float:left;height:%dpx;\"/>" % tam_img)
  # imagem = "&bullet;"
  html_img = "<a href=\"imagens/" + nome_img + "\" border=0px>" + html_img_crua + "</a>"

  # !!! Reduzir o espaço vertical usado por cada produto, quando {detalhe} é falso !!!
  width_pct = ("80%" if detalhe else "33%")
  estilo_final = f"width: {width_pct}; padding: 15px; border-radius: 15px 50px 20px; display: inline-block;\ndisplay: flex; align-items: center; float:left"
  bloco_final = span(estilo_final, html_img + bloco_descr)
  return bloco_final

def bloco_de_usuario(user):
  atrs = usuario.obtem_atributos(user)

  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

  nome = atrs['nome']
  html_nome = paragrafo(estilo_parag, bloco_texto(nome, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  email = atrs['email']
  html_email = paragrafo(estilo_parag, bloco_texto(email, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  CPF = atrs['CPF']
  html_CPF = paragrafo(estilo_parag, bloco_texto(CPF, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  endereco = atrs['endereco']
  html_endereco = paragrafo(estilo_parag, bloco_texto(endereco, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  CEP = atrs['CEP']
  html_CEP = paragrafo(estilo_parag, bloco_texto(CEP, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  telefone = atrs['telefone']
  html_telefone = paragrafo(estilo_parag, bloco_texto(telefone, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  documento = atrs['documento']
  html_documento = paragrafo(estilo_parag, bloco_texto(documento, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

  html_final = html_nome + html_email + html_CPF + html_endereco + html_CEP + html_telefone + html_documento
  bloco_final = span("\n display: inline-block;", html_final)
  
  width_pct = ("33%")
  estilo_final = f"width: {width_pct}; padding: 15px; border-radius: 15px 50px 20px; display: inline-block;\ndisplay: flex; align-items: center; float:left"
  bloco_final = span(estilo_final, bloco_final)
  return bloco_final

def bloco_de_lista_de_produtos(idents):
  todos_prods = ""
  for id_prod in idents:
    prod = produto.busca_por_identificador(id_prod)
    bloco_prod = gera_html_elem.bloco_de_produto(None, prod, None, False)
    todos_prods = todos_prods + bloco_prod + "\n"
  lista_html = div("display:inline-block", todos_prods)
  return lista_html

def bloco_de_lista_de_usuarios(idents):
  todos_user = ""
  for id_usuario in idents:
    user = usuario.busca_por_identificador(id_usuario)
    bloco_prod = gera_html_elem.bloco_de_usuario(user)
    todos_user = todos_user + bloco_prod + "\n"
  lista_html = div("display:inline-block", todos_user)
  return lista_html

def bloco_de_compra(cpr, detalhe):
  id_compra = compra.obtem_identificador(cpr)
  atrs_compra = compra.obtem_atributos(cpr)
  itens = compra.obtem_itens(cpr)
  num_itens = len(itens)
  preco_total = compra.calcula_total(cpr)
  custo_frete = compra.calcular_frete(cpr, atrs_compra['CEP'])
  custo_total = preco_total + custo_frete
  id_usr = compra.obtem_cliente(cpr)
  # Monta o parágrafo de descrição
  estilo_parag = "width: 600px; margin-top: 10px; margin-bottom: 2px; text-indent: 0px;  line-height: 75%;"
  html_ident = paragrafo(estilo_parag, bloco_texto(id_compra, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))
  html_usr = paragrafo(estilo_parag, bloco_texto(str(id_usr), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  html_num_itens = paragrafo(estilo_parag, bloco_texto(str(num_itens), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  html_custo_total = paragrafo(estilo_parag, bloco_texto("Custo total: " + str(custo_total), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))

  if detalhe:
    itens = compra.obtem_itens(cpr)
    linhas = [].copy()
    cmdverProduto = "ver_produto"
    for prod, qtd, prc in itens:
      atrs = produto.obtem_atributos(prod)
      d_curta = atrs['descr_curta']
      palavras = atrs['palavras']
      html_d_curta = d_curta
      html_qtd = gera_html_form.alterar_qtd_de_produto(qtd, prod.id_produto, id_compra)
      html_prc = "R$ " + "{:10.2f}".format(prc)
      html_excl = gera_html_form.excluir_item_de_compra(prod.id_produto, id_compra)
      html_ver_prod = gera_html_botao.submit("Ver", 'ver_produto', None, '#60a3bc')
      linhas.append(( d_curta, html_qtd, html_prc, html_excl ))
    html_itens = tabela(linhas)
    html_endereco = atrs_compra['CEP'] + " " + atrs_compra['endereco'].replace("\n", "<br>")
    html_ends = paragrafo(estilo_parag, bloco_texto(str(html_endereco), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
    html_preco_total = paragrafo(estilo_parag, bloco_texto("Custo total dos produtos: " + str(preco_total), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
    html_frete = paragrafo(estilo_parag, bloco_texto("Custo de frete: " + str(custo_frete), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  else:
    html_itens = ""
    html_ends = ""
    html_preco_total = ""
    html_frete = ""
  # Admnistrador
  atrs_cliente = usuario.obtem_atributos(atrs_compra['cliente'])
  html_admin = ""
  if (atrs_cliente['administrador']):
    status_atual = atrs_compra['status']
    html_recebido = ""
    html_entregue = ""
    # Muda status de pagando para pago
    if (status_atual == 'pagando'):
      atributos_pago = {'id_compra': compra.obtem_identificador(cpr), 'novo_status': 'pago'}
      html_recebido = gera_html_botao.submit("Pagamento Recebido", 'mudar_status_de_compra', atributos_pago, '#55ee55')
    # Muda status de despachado para entregue
    elif (status_atual == 'despachado'):
      atributos_entregue = {'id_compra': compra.obtem_identificador(cpr), 'novo_status': 'entregue'}
      html_entregue = gera_html_botao.submit("Entregue", 'mudar_status_de_compra', atributos_entregue, '#55ee55')
    html_admin = html_recebido if (html_recebido != None and html_recebido != "") else html_entregue

  html_finalizar = ""
  if (num_itens > 0 and detalhe):
    atributos_finalizar = {'id_compra': id_compra}
    html_finalizar = gera_html_botao.simples("Finalizar", 'finalizar_compra', atributos_finalizar, '#ffffff')

  html_trocar_carrinho = gera_html_form.trocar_carrinho(id_compra)
  atrs_alterar = { 'id_compra': id_compra }
  html_alterar_endereco = ""
  html_alt_met_pag = ""
  html_ver = ""
  if detalhe:
    html_alt_met_pag = gera_html_botao.simples("Alterar método de pagamento", 'solicitar_form_de_meio_de_pagamento', atrs_alterar, '#ffffff')
    html_alterar_endereco = gera_html_botao.simples("Alterar Endereço", 'solicitar_form_de_endereco', atrs_alterar, '#ffffff')
  else:
    html_ver = gera_html_botao.submit("Ver", 'ver_compra', {"id_compra" : id_compra}, '#60a3bc')
  html_descr = \
    html_trocar_carrinho + \
    html_usr + html_ident  + \
    html_num_itens + \
    html_preco_total + \
    html_frete + \
    html_custo_total + \
    html_itens + \
    html_alt_met_pag + \
    html_ends + \
    html_alterar_endereco + \
    html_finalizar + \
    html_ver + \
    html_admin
  bloco_descr = span(" display:inline-block;", html_descr)
  bloco_final = \
  span("padding: 15px; border-radius: 15px 50px 20px; display: block;  background-color: #ffffff; display: flex; align-items: center;", bloco_descr)
  return bloco_final

def bloco_de_erro(msg):
  fam_fonte = "Courier"
  # Cabeçalho espalhafatoso:
  html_tit = bloco_texto("ERRO!", None, fam_fonte, "24px", "bold", "5px", "left", "#880000", None)

  # Processa quebras de linha em {msg}:
  msg = re.sub(r'\n', r'<br/>\n', msg)

  # Formata a mensagem:
  html_msg = bloco_texto(msg, None, fam_fonte, "20px", "bold", "5px", "left", "#000000", None)

  # Contrói o botão "OK":
  html_botao = gera_html_botao.simples("OK", 'principal', None, '#55ee55')

  # Junta as partes:
  html_tudo = html_tit + "<br/>" + html_msg + "<br/>" + html_botao

  # Formata:
  estilo_parag = " width: 600px; margin-top: 2px;margin-bottom: 2px; text-indent: 0px; align: center;"
  bloco_final = paragrafo(estilo_parag, html_tudo)

  return bloco_final

def span(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<span" + est + ">" + conteudo + "</span>"
  return html

def div(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<div" + est + ">" + conteudo + "</div>"
  return html

def form(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<form method=\"post\"" + est + ">" + conteudo + "</form>"
  return html

def paragrafo(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<p" + est + ">" + conteudo + "</p>\n"
  return html

def bloco_texto(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo):
  estilo = \
    ( " display: " + disp + ";" if disp != None else "") + \
    ( " font-family:" + fam_fonte + ";" if fam_fonte != None else "") + \
    ( " font-weight:" + peso_fonte + ";" if peso_fonte != None else "") + \
    ( " font-size:" + tam_fonte + ";" if tam_fonte != None else "") + \
    ( " padding:" + pad + ";" if pad != None else "") + \
    ( " background-color:" + cor_fundo + ";" if cor_fundo != None else "") + \
    ( " color:" + cor_texto + ";" if cor_texto != None else "") + \
    ( " text-align:" + halign + ";" if halign != None else "")
  return span(estilo, texto)

def tabela(linhas):
  """Gera o HTML para uma tabela "<table>...</table>".

  O parâmetro {linhas} deve ser uma lista ou tupla cujos elementos descrevem as linhas.
  Cada elemento de {linhas} deve ser uma lista ou tupla de fragmentos HTML, que são
  inseridos nas células da linha correspondente da tabela."""

  html_tab = "    <table>\n"
  for lin in linhas:
    html_lin = "      <tr>\n"
    for el in lin:
      html_el = "        <td>" + el + "</td>\n"
      html_lin += html_el
    html_lin += "      </tr>\n"
    html_tab += html_lin
  html_tab += "    </table>"
  return html_tab

def input(rotulo, tipo, nome, val_ini, dica, cmd):
  html_rotulo = label(rotulo, ": ")
  html_tipo = " type =\"" + tipo + "\""
  html_nome = " name=\"" + nome + "\" id=\"" + nome + "\""
  if tipo == "number": html_nome += " min=\"1\""
    
  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")
  html_val_ini = ( " value =\"" + val_ini + "\"" if val_ini != None else "" )
  if val_ini == 'on' and tipo == 'checkbox':
    html_val_ini += ' checked '
  html_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  html_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  html = html_rotulo + "<input" + html_tipo + html_nome + html_val_ini + html_dica + "/>"
  return html


def label(rotulo, sep):
  if rotulo == None or rotulo == "":
    return ""
  else:
    return "<label>" + rotulo + (sep if sep != None else "") + "</label>"
