# Implementação do módulo {comando_subm_cadastrar}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import gera_html_pag

def processa(sessao, args):
  usr = usuario.cria(args)

  conteudo = ""

  #verifica se o usuário foi criado corretamente 
  #e retorna uma página de acordo com o resultado
  if type(usr) is ObjUsuario:
    conteudo = gera_html_pag.mostra_usuario(usr)
  else:
    erro = "Erro ao gerar novo usuário"
    conteudo = gera_html_pag.generica(erro)
  return conteudo
