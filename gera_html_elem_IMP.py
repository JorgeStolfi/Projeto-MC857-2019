# Implementação do módulo {gera_html_elem}.

# Interfaces do projeto importadas por esta implementação:
import gera_html_form
import gera_html_elem
import gera_html_botao
import produto
import compra
import usuario
import comando_excluir_item_de_compra
import comando_alterar_qtd_de_produto

# Outros módulos importados por esta implementação:
from datetime import datetime, timezone

#Funções exportadas por este módulo:

def cabecalho(title, grande):

  if grande:
    header_title = "<h1>" + title + "</h1>"
  else:
    header_title = "<h2>" + title + "</h2>"

  return \
    "<!doctype html>\n" + \
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
  html_bt_principal = "  " + gera_html_botao.simples("Principal", 'principal', None, '#eeeeee') + "\n"
  html_fm_buscar = "  " + gera_html_form.buscar_produtos() + "\n"

  html_bt_user = ""
  if logado:
    html_bt_user = menu_geral_logado(nome_usuario)
    if admin:
      html_bt_compras_produto = " " + gera_html_botao.simples("Compras de produto", "buscar_compras_por_produto", None, '#eeeeee') + '\n'
    else:
      html_bt_compras_produto = " "
  else:
    html_bt_user = menu_geral_deslogado()
  html_menu = \
    "<nav>\n" + \
      html_bt_principal + \
      html_fm_buscar + \
      html_bt_user + \
    "</nav>"

  if admin:
    html_menu += \
      "<nav>\n" + \
        menu_geral_admin() + \
      "</nav>\n"

  return html_menu

def menu_geral_logado(nome_usuario):
  return gera_html_botao.simples("Minha Conta", 'solicitar_form_de_dados_de_usuario', None, '#eeeeee') + "\n" + \
    " " + gera_html_botao.simples("Meu Carrinho", 'ver_carrinho', None, '#eeeeee') + "\n" + \
    " " + gera_html_botao.simples("Minhas Compras", 'buscar_compras', None, '#eeeeee') + "\n" + \
    " " + gera_html_botao.simples("Minha Conta", 'solicitar_form_de_dados_de_usuario', None, '#eeeeee') + "\n" + \
    " " + gera_html_botao.simples("Ofertas", 'ver_ofertas', None, '#ffdd22') + "\n" + \
    " " + gera_html_botao.simples("Acrescentar produto", "solicitar_form_de_dados_de_produto", None, '#ffdd22') + "\n" \
    " " + gera_html_botao.simples("Sair", 'fazer_logout', None, '#eeeeee') + "\n" + \
    " " + bloco_texto("Oi " + nome_usuario, "inline_block", "Courier", "18px", "bold", None, None, None, None) + "\n"

def menu_geral_deslogado():
  return gera_html_botao.simples("Entrar", 'solicitar_form_de_login', None, '#55ee55') + "\n" + \
    " " + gera_html_botao.simples("Cadastrar", 'solicitar_form_de_dados_de_usuario', None, '#eeeeee') + "\n" + \
    " " + gera_html_botao.simples("Ofertas", 'ver_ofertas', None, '#ffdd22') + "\n" + \
    " " + gera_html_botao.simples("Acrescentar produto", "solicitar_form_de_dados_de_produto", None, '#ffdd22') + "\n"

def menu_geral_admin():
  return gera_html_botao.simples("Compras de produto", "buscar_compras_por_produto", None, '#eeeeee') + '\n'


def bloco_de_produto(id_compra, prod, qtd, detalhe):
  id_produto = produto.obtem_identificador(prod)
  atrs = produto.obtem_atributos(prod)

  # Monta o parágrafo de descrição
  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

  d_curta = atrs['descr_curta']
  html_d_curta = paragrafo(estilo_parag, bloco_texto(d_curta, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

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

  if qtd == None:
    # Preço unitário, sem campo de quantidade:
    preco = atrs['preco']
    html_qtd = ""
  else:
    preco = produto.calcula_preco(prod, qtd)
    # !!! Deveria ser um campo editável !!!
    html_qtd = bloco_texto(("%d" % qtd), None, "Courier", "36px", "bold", "0px", "left", "#0000ff", "#fff888")

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

  html_descr = html_em_oferta + html_d_curta  + html_d_media + html_d_longa + html_qtd + html_preco + html_botao + html_peso + html_volume

  bloco_descr = span("\n display: inline-block;", html_descr)

  tam_img = (200 if detalhe else 100)
  nome_img = atrs['imagem']
  html_img_crua = ("<img src=\"imagens/" + nome_img + "\" alt=\"" + id_produto + "\" style=\"float:left;height:%dpx;\"/>" % tam_img)
  # imagem = "&bullet;"
  html_img = "<a href=\"imagens/" + nome_img + "\" border=0px>" + html_img_crua + "</a>"

  # !!! Reduzir o espaço vertical usado por cada produto, quando {detalhe} é falso !!!
  bloco_final = \
    span("\n width: 48%; padding: 15px; border-radius: 15px 50px 20px; display: inline-block;\ndisplay: flex; align-items: center; float:left", html_img + bloco_descr)
  return bloco_final

def bloco_de_compra(cpr, detalhe):
  id_compra = compra.obtem_identificador(cpr)
  atrs_compra = compra.obtem_atributos(cpr)
  itens = compra.obtem_itens(cpr)
  num_itens = len(itens)
  preco_total = compra.calcula_total(cpr)
  id_usr = compra.obtem_cliente(cpr)
  # Monta o parágrafo de descrição
  estilo_parag = "\n  width: 600px;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
  html_ident = paragrafo(estilo_parag, bloco_texto(id_compra, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))
  html_usr = paragrafo(estilo_parag, bloco_texto(str(id_usr), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  html_num_itens = paragrafo(estilo_parag, bloco_texto(str(num_itens), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  html_preco_total = paragrafo(estilo_parag, bloco_texto(str(preco_total), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  html_endereco = atrs_compra['CEP'] + " " + atrs_compra['endereco'].replace("\n", "<br>")
  html_ends = paragrafo(estilo_parag, bloco_texto(str(html_endereco), None, "Courier", "16px", "normal", "0px", "left", "#000000", None))
  if detalhe:
    itens = compra.obtem_itens(cpr)
    linhas = [].copy()
    cmdAlterarQtd = "alterar_qtd_de_produto"
    cmdverProduto = "ver_produto"
    for prod, qtd, prc in itens:
      atrs = produto.obtem_atributos(prod)
      d_curta = atrs['descr_curta']
      palavras = atrs['palavras']
      html_d_curta = d_curta
      html_palavras = palavras
      html_qtd = input(None, "number", "qtd", str(qtd), None, cmdAlterarQtd)
      html_prc = "R$ " + "{:10.2f}".format(prc)
      html_excl = gera_html_botao.submit("Excluir", 'excluir_item_de_compra', None, '#ffffff')
      # html_trocar_carrinho = gera_html_botao.submit("Usar como carrinho", 'trocar_carrinho', {'id_compra': id_compra},'#ffdd22'))
      html_ver_prod = gera_html_botao.submit("Ver", 'ver_produto', None, '#eeeeee')
      # !!! Falta custo de frete e valor total a pagar !!!
      # linhas.append(( d_curta, html_qtd, html_prc, html_excl ))
      linhas.append(( d_curta, html_qtd, html_prc, html_palavras, html_excl ))
    html_itens = tabela(linhas)
  else:
    html_itens = ""
  
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
    html_admin = html_recebido if (html_recebido != "") else html_entregue 
  
  html_finalizar = ""
  if (num_itens > 0):
    atributos_finalizar = {'id_compra': id_compra}
    html_finalizar = gera_html_botao.simples("Finalizar", 'finalizar_compra', atributos_finalizar, '#ffffff')

  html_trocar_carrinho = gera_html_form.trocar_carrinho(id_compra)
  atrs_alterar = { 'id_compra': id_compra }
  html_alterar_endereco = gera_html_botao.simples("Alterar Endereço", 'solicitar_form_de_endereco', atrs_alterar, '#ffffff')
  html_alt_met_pag = gera_html_botao.simples("Alterar método de pagamento", 'solicitar_form_de_meio_de_pagamento', atrs_alterar, '#ffffff')
  html_descr = \
    html_trocar_carrinho + \
    html_usr + html_ident  + \
    html_num_itens + \
    html_preco_total + \
    html_itens + \
    html_alt_met_pag + \
    html_ends + \
    html_alterar_endereco + \
    html_finalizar + \
    html_admin
  bloco_descr = span("\n display: inline-block;", html_descr)
  bloco_final = \
  span("\n  padding: 15px; border-radius: 15px 50px 20px; display: block;\n  background-color: #ffffff; display: flex; align-items: center;", bloco_descr)
  return bloco_final

def bloco_de_erro(msg):
  fam_fonte = "Courier"
  # Cabeçalho espalhafatoso:
  html_tit = bloco_texto("ERRO!", None, fam_fonte, "24px", "bold", "5px", "left", "#880000", None)

  # Formata a mensagem:
  html_msg = bloco_texto(msg, None, fam_fonte, "20px", "bold", "5px", "left", "#000000", None)

  # Contrói o botão "OK":
  html_botao = gera_html_botao.simples("OK", 'principal', None, '#55ee55')

  # Junta as partes:
  html_tudo = html_tit + "<br/>" + html_msg + "<br/>" + html_botao

  # Formata:
  estilo_parag = "\n  width: 600px;\n  margin-top: 2px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  align: center;"
  bloco_final = paragrafo(estilo_parag, html_tudo)

  return bloco_final

def span(estilo, conteudo):
  est = (" style=\"" + estilo + "\n\"" if estilo != "" else "")
  html = "<span" + est + ">" + conteudo + "</span>"
  return html

def div(estilo, conteudo):
  est = (" style=\"" + estilo + "\n\"" if estilo != "" else "")
  html = "<div" + est + ">" + conteudo + "</div>"
  return html

def paragrafo(estilo, conteudo):
  est = (" style=\"" + estilo + "\n\"" if estilo != "" else "")
  html = "<p" + est + ">" + conteudo + "</p>\n"
  return html

def bloco_texto(texto, disp, fam_fonte, tam_fonte, peso_fonte, pad, halign, cor_texto, cor_fundo):
  estilo = \
    ( "\n  display: " + disp + ";" if disp != None else "") + \
    ( "\n  font-family:" + fam_fonte + ";" if fam_fonte != None else "") + \
    ( "\n  font-weight:" + peso_fonte + ";" if peso_fonte != None else "") + \
    ( "\n  font-size:" + tam_fonte + ";" if tam_fonte != None else "") + \
    ( "\n  padding:" + pad + ";" if pad != None else "") + \
    ( "\n  background-color:" + cor_fundo + ";" if cor_fundo != None else "") + \
    ( "\n  color:" + cor_texto + ";" if cor_texto != None else "") + \
    ( "\n  text-align:" + halign + ";" if halign != None else "")
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
  html_rotulo = label(rotulo)
  html_tipo = " type =\"" + tipo + "\""
  html_nome = " name=\"" + nome + "\" id=\"" + nome + "\""
  if tipo == "number":
      html_nome += ' min="1" max="5"\ '
  if val_ini != None and dica != None:
    erro_prog("{val_ini} e {dica} são mutuamente exclusivos")
  html_val_ini = ( " value =\"" + val_ini + "\"" if val_ini != None else "" )
  html_dica = ( " placeholder=\"" + dica + "\"" if dica != None else "" )
  html_cmd = ( " onchange=\"window.location.href=" + cmd + "\"" if cmd != None else "" )
  html = html_rotulo + "<input" + html_tipo + html_nome + html_val_ini + html_dica + "/>"
  return html
    

def label(rotulo):
  if rotulo == None or rotulo == "":
    return ""
  else:
    return "<label>" + rotulo + "</label>"
