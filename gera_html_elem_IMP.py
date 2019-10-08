# Implementação do módulo {gera_html_elem}.

# Interfaces do projeto importadas por esta implementação:
import gera_html_form
import gera_html_elem
import gera_html_botao
import produto
import compra

# Outros módulos importados por esta implementação:
from datetime import datetime, timezone

#Funções exportadas por este módulo:

def cabecalho(title, grande):
  header_title = "<h1>" + title + "</h1>"

  if grande == False:
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

def menu_geral(logado, nome_usuario):
  html_bt_principal = "  " + gera_html_botao.principal() + "\n"
  html_fm_buscar = "  " + gera_html_form.buscar_produtos() + "\n"
  if logado:
    html_bt_sair = "  " + gera_html_botao.menu_sair() + "\n"
    html_nome = "  " + gera_html_elem.bloco_texto(nome_usuario, "inline_block", "Courier", "14px", "bold", None, None, None, "#ff44ff") + "\n"
    html_botao_carrinho =  "  " + gera_html_botao.menu_carrinho() + "\n"
    html_bt_entrar = ""
    html_bt_cadastrar = ""
  else:
    html_bt_sair = ""
    html_nome = ""
    html_botao_carrinho =  ""
    html_bt_entrar = "  " + gera_html_botao.menu_entrar() + "\n"
    html_bt_cadastrar = "  " + gera_html_botao.menu_cadastrar() + "\n"
  
  html_menu = \
    "<nav>\n" + \
      html_bt_principal + \
      html_fm_buscar + \
      html_bt_sair + \
      html_nome + \
      html_botao_carrinho + \
      html_bt_entrar + \
      html_bt_cadastrar + \
    "</nav>"
  return html_menu

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

def bloco_de_produto(prod, qt, detalhe):
    id_produto = produto.obtem_identificador(prod)
    atrs = produto.obtem_atributos(prod)

    # Monta o parágrafo de descrição
    estilo_parag = "\n  width: 600px;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"

    d_curta = atrs['descr_curta']
    html_d_curta = paragrafo(estilo_parag, bloco_texto(d_curta, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

    d_media = atrs['descr_media']
    html_d_media = paragrafo(estilo_parag, bloco_texto(d_media, None, "Courier", "16px", "normal", "0px", "left", "#000000", None))

    qt_inicial = (qt if qt != None else 1.0) # Quantidade a pedir no formulário de ver ou comprar o produto:
    if detalhe:
      d_longa = atrs['descr_longa']
      html_d_longa = paragrafo(estilo_parag, bloco_texto(d_longa, None, "Courier", "14px", "normal", "0px", "left", "#000000", None))
      html_botao = gera_html_form.comprar_produto(id_produto, qt_inicial)
    else:
      html_d_longa = ""
      html_botao = gera_html_form.ver_produto(id_produto, qt_inicial)

    if qt == None:
      # Preço unitário, sem campo de quantidade:
      preco = atrs['preco']
      html_qt = ""
    else:
      preco = produto.calcula_preco(prod, qt)
      html_qt = bloco_texto("!!! IMPLEMENTAR !!!", None, "Courier", "36px", "bold", "0px", "left", "#0000ff", "#fff888")

    str_preco = ("R$ %.2f" % preco)
    html_preco = bloco_texto(str_preco, "inline-block", "Courier", "20px", "bold", "2px", "left", "#000000", None)

    html_descr = html_d_curta  + html_d_media + html_d_longa + html_qt + html_preco + html_botao
    bloco_descr = span("\n display: inline-block;", html_descr)

    tam_img = (200 if detalhe else 100)
    nome_img = atrs['imagem']
    html_img_crua = ("<img src=\"imagens/" + nome_img + "\" alt=\"" + id_produto + "\" style=\"float:left;height:%dpx;\"/>" % tam_img)
    # imagem = "&bullet;"
    html_img = "<a href=\"imagens/" + nome_img + "\" border=0px>" + html_img_crua + "</a>"

    # !!! Reduzir o espaço vertical usado por cada produto, quando {detalhe} é falso !!!
    bloco_final = \
      span("\n  padding: 15px; border-radius: 15px 50px 20px; display: block;\n  background-color: #ffffff; display: flex; align-items: center;", html_img + bloco_descr)
    return bloco_final

def bloco_de_compra(cpr):
  # !!! A implementação abaixo está incorreta. Veja os "!!!" na interface. !!!

  itens = compra.obtem_itens(cpr)
  # 
  # estilo_parag = "\n  width: 600px;\n  margin-top: 2px;\n  margin-bottom: 2px;\n  text-indent: 0px;"
  # bloco_final = ""
  # 
  # for itm in itens:
  #   #NOME E DESCRICÃO DO PRODUTO, COM BOTÃO 'VER'
  #   desc = itm.desc
  #   html_desc = paragrafo(estilo_parag, bloco_texto(desc, None, "Courier", "18px", "bold", "2px", "left", "#ff0000", "#88fff8"))
  #   str_preco = ("R$%.2f" % preco)
  #   html_preco = paragrafo(estilo_parag, bloco_texto(str_preco, None, "Courier", "20px", "bold", "2px", "left", "#000000", "#f8ff88"))
  #   html_botao = gera_html_form.ver_produto(id_produto)
  #   html_descr = html_desc + html_preco + html_botao
  #   #FOTO DO PRODUTO
  #   imagem = ("<img src=\"imagens/155951.png\" alt=\"" + id_compra + "\" style=\"float:left;height:%dpx;\"/>" % 80)
  #   html_img = "<a href=\"imagens/155951.png\" border=0px>" + imagem + "</a>
  #   #MONTA BLOCO PRODUTO
  #   bloco_descr = span("\n  display: inline-block;", html_descr)
  #   bloco_item = \
  #     span("\n  display: block;\n  background-color: #00ff00;", html_img + bloco_descr)
  #   bloco_final = bloco_final + bloco_item
  # 
  erro_html = bloco_texto("!!! IMPLEMENTAR !!!", None, "Courier", "24px", "bold", "2px", "left", "#ff0000", "#88fff8")
  itens_html = bloco_texto(str(itens), None, "Courier", "14px", "normal", "2px", "left", "#000000", None)
  bloco_final = erro_html + "\n<br/><hr/>\n" + itens_html
  return bloco_final

def bloco_de_erro(msg):
  fam_fonte = "Courier"
  # Cabeçalho espalhafatoso:
  html_tit = bloco_texto("ERRO", None, fam_fonte, "24px", "bold", "20px", "left", "#880000", "#ffdd44")

  # Formata a mensagem:
  html_msg = bloco_texto(msg, None, fam_fonte, "20px", "bold", "2px", "left", "#000000", None)

  # Contrói o botão "OK":
  html_botao = gera_html_botao.erro_ok()

  # Junta as partes:
  html_tudo = html_tit + "<br/>" + html_msg + "<br/>" + html_botao
  
  # Formata:
  estilo_parag = "\n  width: 600px;\n  margin-top: 2px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  align: center;"
  bloco_final = paragrafo(estilo_parag, html_tudo)
  
  return bloco_final

 
