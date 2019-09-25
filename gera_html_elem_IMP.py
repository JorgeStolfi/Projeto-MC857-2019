# Implementação do módulo {gera_html_elem}.

# Interfaces importadas por esta implementação:
from datetime import datetime, timezone
import gera_html_form
import gera_html_botao
import produto

#Funções exportadas por este módulo:

def cabecalho(title):
  return \
    "<!doctype html>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + title + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n" + \
    "<h1>" + title + "</h1>"

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
  return \
    """
    <nav>
      """ + gera_html_botao.inicio() + """
      """ + gera_html_form.buscar_produtos() + """
      """ + gera_html_botao.menu_sair() if logado else gera_html_botao.menu_entrar() + """
      """ + '' if logado else gera_html_botao.menu_cadastrar() + """
      """ + gera_html_botao.carrinho() if logado else '' + """
    </nav>
    """

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
    estilo_parag = "\n  width: 600px;\n  margin-top: 2px;\n  margin-bottom: 2px;\n  text-indent: 0px;"

    d_curta = atrs['descr_curta']
    html_d_curta = paragrafo(estilo_parag, bloco_texto(d_curta, None, "Courier", "20px", "bold", "2px", "left", "#263238", None))

    d_media = atrs['descr_media']
    html_d_media = paragrafo(estilo_parag, bloco_texto(d_media, None, "Courier", "12px", "normal", "0px", "left", "#000000", None))

    qt_inicial = (qt if qt != None else 1.0) # Quantidade a pedir no formulário de ver ou comprar o produto:
    if detalhe:
      d_longa = atrs['descr_longa']
      html_d_longa = paragrafo(estilo_parag, bloco_texto(d_longa, None, "Courier", "12px", "normal", "0px", "left", "#000000", None))
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
      html_qt = bloco_texto("!!! IMPLEMENTAR !!!", None, "Courier", "35px", "bold", "0px", "left", "#0000ff", "#fff888")

    str_preco = ("R$%.2f" % preco)
    html_preco = paragrafo(estilo_parag, bloco_texto(str_preco, None, "Courier", "20px", "bold", "2px", "left", "#000000", None))

    html_descr = html_d_curta + html_preco + "<hr>" + html_d_media + "<br>" + html_d_longa + html_qt + html_botao + "<hr>"
    bloco_descr = span("\n display: inline-block;", html_descr)

    tam_imagem = (200 if detalhe else 150)
    imagem = ("<img src=\"imagens/155951.png\" alt=\"" + id_produto + "\" style=\"float:left;height:%dpx;\"/>" % tam_imagem)
    # imagem = "&bullet;"
    imagem_click = "<a href=\"imagens/155951.png\" border=0px>" + imagem + "</a>"

    bloco_final = \
      span("\n padding: 15px; border-radius: 15px 50px 20px; display: block;\n  background-color: #ffffff; display: flex; align-items: center;", imagem_click + bloco_descr)
    return bloco_final

  def bloco_de_compra(comp):
    lista_de_itens = compra.obtem_itens(comp)
    
    estilo_parag = "\n  width: 600px;\n  margin-top: 2px;\n  margin-bottom: 2px;\n  text-indent: 0px;"
    bloco_final = ""
    
    for item in lista_de_itens:
      #NOME E DESCRICÃO DO PRODUTO, COM BOTÃO 'VER'
      desc = item.desc
      html_desc = paragrafo(estilo_parag, bloco_texto(desc, None, "Courier", "18px", "bold", "2px", "left", "#ff0000", "#88fff8"))
      str_preco = ("R$%.2f" % preco)
      html_preco = paragrafo(estilo_parag, bloco_texto(str_preco, None, "Courier", "20px", "bold", "2px", "left", "#000000", "#f8ff88"))
      html_botao = gera_html_form.ver_produto(id_produto)
      html_descr = html_desc + html_preco + html_botao
      #FOTO DO PRODUTO
      imagem = ("<img src=\"imagens/155951.png\" alt=\"" + id_compra + "\" style=\"float:left;height:%dpx;\"/>" % 80)
      imagem_click = "<a href=\"imagens/155951.png\" border=0px>" + imagem + "</a>
      #MONTA BLOCO PRODUTO
      bloco_descr = span("\n  display: inline-block;", html_descr)
      bloco_item = \
        span("\n  display: block;\n  background-color: #00ff00;", imagem_click + bloco_descr)
      bloco_final = bloco_final + bloco_item
      
    return bloco_final
 
