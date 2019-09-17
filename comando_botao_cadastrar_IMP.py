# Implementação do módulo {comando_botao_cadastrar}.

import gera_html_form
import tabela_generica

def processa():
  conteudo_cadastro = gera_html_form.cadastrar_usuario()
  cadastro = tabela_generica.acrescenta("usuarios", conteudo_cadastro)
  return cadastro
