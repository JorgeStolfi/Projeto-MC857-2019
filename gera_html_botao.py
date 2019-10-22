# -*- coding: utf-8 -*-

# Interface do módulo {gera_html_botao}.

# As funções desta interface retornam cadeias de caracteres que são
# fragmentos de código HTML5 que definem elementos do tipo "<button>" ou
# "<input type=submit>", para uso em várias páginas.

# Implementação desta interface:
import gera_html_botao_IMP

def simples(texto, URL, args, cor_fundo):
  """Função que gera um botão genérico de tipo "<button>", com o {texto} e
  {cor_fundo} especificados. 
  
  Quando clicado, o botão emite um comando HTTP 'GET' para o {URL} dado.
  
  Se {args} não for {None}, deve ser um dicionário cujas chaves e
  valores são acrescentadas ao {URL} no formato
  "?{chave1}={valor1}&{chave2}={valor2}...". Por enquanto, as chaves e
  valores devem ser cadeias só com letras ASCII, dígitos, pontos,
  hífens, e underscores."""
  return gera_html_botao_IMP.simples(texto, URL, args, cor_fundo)

def submit(texto, URL, args, cor_fundo):
  """Função que gera um botões "<input type=submit>" com o {texto} 
  e a {cor_fundo} especificados, para uso dentro de um formulário HTML "<form>...</form>".  
  
  Quando clicado, o botão emite um comando HTTP 'POST' para o {URL} dado, com as
  informações nos campos do formulário.
  
  Se {args} não for {None}, deve ser um dicionário cujas chaves e
  valores são acrescentadas como campos 'hidden' junto ao 
  botão propriamente dito. Por enquanto, as chaves e
  valores devem ser cadeias só com letras ASCII, dígitos, pontos,
  hífens, e underscores."""
  return gera_html_botao_IMP.submit(texto, URL, args, cor_fundo)
