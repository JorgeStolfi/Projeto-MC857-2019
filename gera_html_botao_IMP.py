# Implementação do módulo {gera_html_botao}.

# Interfaces do projeto usados por este módulo: 
import gera_html_elem

# Outros módulos usados por este módulo:

# !!! Melhorar a aparência dos botões. !!!
# !!! Reduzir o tamanho dos botões para economizar espaço da tela. !!!

# BOTÕES DE TIPO <button>

def principal():
  texto = "Principal"
  cor_fundo = "#fff888"
  return botao_simples(texto, "principal", cor_fundo)

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

def menu_carrinho():
  texto = "Carrinho"
  cor_fundo = "#fff888"
  return botao_simples(texto, "menu_carrinho", cor_fundo)

def erro_ok():
  texto = "OK"
  cor_fundo = "#44ff44"
  return botao_simples(texto, "", cor_fundo)

# BOTÕES DE TIPO <submit>

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

def submit_excluir_produto():
  texto = "Excluir"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_excluir_produto", cor_fundo)

def submit_cadastrar_usuario():
  texto = "Cadastrar"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_cadastrar_usuario", cor_fundo)

def submit_entrar():
  texto = "Entrar"
  cor_fundo = "#fff888"
  return botao_submit(texto, "submit_entrar", cor_fundo)

# FUNÇÕES INTERNAS

def botao_simples(texto, URL, cor_fundo):
  """Função INTERNA que gera um botão genérico de tipo "<button>",
  com o {texto} e {cor_fundo} especificados.  Quando clicado,
  o botão emite um comando HTTP 'GET' para o {URL} dado."""
  
  # O botão propriamente dito:
  html_cru = "<button type=\"button\" onclick=\"location.href='" + URL + "'\">" + texto + "</button>"
  
  # Define o estilo:
  fam_fonte = "Courier"
  tam_fonte = "18px"
  html = gera_html_elem.bloco_texto(html_cru, "inline_block", fam_fonte, tam_fonte, "bold", "5px", "center", "#000000", "#eeeeee")
  return html

def botao_submit(texto, URL, cor_fundo):
  """Função INTERNA que gera um botões "<input type=submit>"
  com o {texto} e a {cor_fundo} especificados.  Quando clicado,
  o botão emite um comando HTTP 'POST' para o {URL} dado."""
  
  # O botão propriamente dito:
  html_cru = "<input type=\"submit\" formaction=\"" + URL + "\" value=\"" + texto + "\">"
  
  # Define o estilo:
  fam_fonte = "Courier"
  tam_fonte = "18px"
  html = gera_html_elem.bloco_texto(html_cru, "inline_block", fam_fonte, tam_fonte, "bold", "3px", "center", "#000000", cor_fundo)
  return html
