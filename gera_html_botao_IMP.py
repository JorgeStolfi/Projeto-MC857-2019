# Implementação do módulo {gera_html_botao}.

#####Funções <button>#####

def botao_simples(texto, URL, cor_fundo):
  tam_fonte = "18px"
  fam_fonte = "Courier"
  return \
    "<span style=\"\n" + \
    "  display: inline-block;\n" + \
    "  font-family:" + fam_fonte + ";\n" + \
    "  font-size:" + tam_fonte + ";\n" + \
    "  padding: 5px;\n" + \
    "  background-color:" + cor_fundo + ";\n" + \
    "  text-align: center;\n" + \
    "\">\n" + \
    "  <button\n" + \
    "    type=\"button\"\n" + \
    "    onclick=\"location.href='" + URL + "'\"\n" + \
    "  >" + texto + "</button>\n" + \
    "</span>"

def botao_inicio():
  texto = "Inicio"
  cor_fundo = "#fff888"
  caminho = '/'
  return botao_simples(texto, caminho, cor_fundo)

def botao_carrinho():
  texto = "Carrinho"
  cor_fundo = "#fff888"
  caminho = '/carrinho'
  return botao_simples(texto, caminho, cor_fundo)

def menu_entrar():
  texto = "Entrar"
  cor_fundo = "#fff888"
  return botao_simples(texto, "menu_entrar", cor_fundo)

def menu_sair():
  texto = "Sair"
  cor_fundo = "#fff888"
  return botao_simples(texto, "menu_sair", cor_fundo)

def menu_cadastrar():
  texto = "Cadastrar"
  cor_fundo = "#fff888"
  return botao_simples(texto, "menu_cadastrar", cor_fundo)

#####Funções <submit>#####

def botao_submit(texto, URL, cor_fundo):
  """Função INTERNA para as demais funções de botões "<input type=submit>". 
  Retorna HTML do botão <submit> com texto e cor de fundo especificados."""
  return \
    "<span style=\"background-color:" + cor_fundo + ";text-align: center;\">\n" + \
    "  <input type=\"submit\" formaction=\"" + URL + "\" value=\"" + texto + "\">" + \
    "</span>"

def submit_ver_produto():
  texto = "Ver"
  cor_fundo = "#f8ff88"
  return botao_submit(texto, "submit_ver_produto", cor_fundo)

def submit_comprar_produto():
  texto = "Comprar"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_comprar_produto", cor_fundo)

def submit_buscar_produtos():
  texto = "Buscar"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_buscar_produtos", cor_fundo)

def submit_cadastrar_usuario():
  texto = "Cadastrar"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_cadastrar_usuario", cor_fundo)

def submit_entrar():
  texto = "Entrar"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_entrar", cor_fundo)

def submit_sair():
  texto = "Sair"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_sair", cor_fundo)
