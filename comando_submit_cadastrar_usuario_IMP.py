# Implementação do módulo {comando_submit_cadastrar_usuario}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import gera_html_pag
from utils_testes import erro_prog, mostra

def processa(ses, args):
  # !!! Precisa extrair dados do formulário {args} e montar um dicionário como {cria} quer. !!! 
  # !!! Precisa fazer certas consistências também !!!
  usr = usuario.cria(args)

  conteudo = ""

  # Verifica se o usuário foi criado corretamente 
  # e retorna uma página de acordo com o resultado:
  if type(usr) is ObjUsuario:
    conteudo = gera_html_pag.mostra_usuario(usr)
  else:
    erro = "Erro ao gerar novo usuário"
    conteudo = gera_html_pag.mensagem_de_erro(erro)
  return conteudo
