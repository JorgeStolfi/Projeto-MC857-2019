# Implementação do módulo {gera_html_botao}.

# Interfaces do projeto usados por este módulo:
import gera_html_elem

def estilo_de_botao(cor_fundo):
  """Retorna um fragmento HTML para uso no atributo "style" de um botão
  (simples ou submit). Especifica a {cor_fundo} indicada,
  com fonte, tamanho etc. padronizados."""
  fam_fonte = "Courier"
  peso_fonte = "Bold"
  tam_fonte = "18px"
  estilo = \
    " color: #000000; " + \
    " font-family:" + fam_fonte + ";" + \
    " font-weight:" + peso_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    " background:" + cor_fundo + ";" + \
    " padding: 2px 5px 2px 5px; " + \
    " border-radius: 5px; " + \
    " transition: all 0.4s ease 0s;"
  return estilo

def simples(texto, URL, args, cor_fundo):
  if args != None:
    # Acrescenta argumentos ao {URL}:
    sep = '?'
    for key, val in args.items():
      if val != None and val != "":
        URL += (sep + key + "=" + str(val))
        sep = '&'
    
  # Constrói o botão propriamente dito:
  estilo = estilo_de_botao(cor_fundo)
  html = "<button type=\"button\" style=\"" + estilo + "\" onclick=\"location.href='" + URL + "'\">" + texto + "</button>"
  return html

def submit(texto, URL, args, cor_fundo):
  args_html = ""
  if args != None:
    # Acrescenta argumentos ao {args_html}:
    for key, val in args.items():
      kv_html = gera_html_elem.input(None, 'hidden', key, val, None, None)
      args_html += kv_html

  # O botão propriamente dito:
  estilo = estilo_de_botao(cor_fundo)
  html = args_html + "<input type=\"submit\" style=\"" + estilo + "\n\" formaction=\"" + URL + "\" value=\"" + texto + "\"/>"
  return html
