# Implementação do módulo {gera_html_botao}.

# Interfaces do projeto usados por este módulo:
import gera_html_elem

def simples(texto, URL, args, cor_fundo):
  if args != None:
    # Acrescenta argumentos ao {URL}:
    sep = '?'
    for key, val in args.items():
      URL += (sep + key + "=" + val)
      sep = '&'
    
  # Constrói o botão propriamente dito:
  estilo = """
              color: #fff !important;
              text-transform: uppercase;
              text-decoration: none;
              padding: 2px 5px 2px 5px;
              border-radius: 5px;
              display: inline-block;
              border: none;
              transition: all 0.4s ease 0s;
           """
  estilo += "background:" + cor_fundo + ";"
  html_cru = "<a style=\"" + estilo + "\" href=\"" + URL + "\">" + texto + "</a>"

  # Define o estilo:
  fam_fonte = "Courier"
  tam_fonte = "18px"
  html = gera_html_elem.bloco_texto(html_cru, "inline_block", fam_fonte, tam_fonte, "bold", "5px", "center", "#000000", '#eeeeee')
  return html

def submit(texto, URL, args, cor_fundo):
  args_html = ""
  if args != None:
    # Acrescenta argumentos ao {args_html}:
    for key, val in args.items():
      kv_html = gera_html_elem.input(None, 'hidden', key, val, None, None)
      args_html += kv_html

  # O botão propriamente dito:
  estilo = """
                color: #fff !important;
                text-transform: uppercase;
                text-decoration: none;
                padding: 2px 5px 2px 5px;
                border-radius: 5px;
                display: inline-block;
                border: none;
                transition: all 0.4s ease 0s;
             """
  estilo += "background:" + cor_fundo + ";"
  html_cru = "<a style=\"" + estilo + "\" href=\"" + URL + "\">" + texto + "</a>"

  # Define o estilo:
  fam_fonte = "Courier"
  tam_fonte = "18px"
  html = gera_html_elem.bloco_texto(html_cru, "inline_block", fam_fonte, tam_fonte, "bold", "3px", "center", "#000000", '#eeeeee')
  return html
