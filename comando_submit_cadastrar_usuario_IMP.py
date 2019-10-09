# Implementação do módulo {comando_submit_cadastrar_usuario}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import gera_html_pag
from utils_testes import erro_prog, mostra
import re
#{'celular': '165156165165', 'cpf': '651651651651', 'endereco': 'av rua da casa', 'confSenha': '123456', 'cep': '6156-561', 'email': 'lucianocps9@gmail.com', 'telefone': '651561651561', 'nome': 'Luciano', 'senha': '123456', 'estado': 'AP'}

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):
  erro = ''

  if 'nome' not in args:
    erro = msg_campo_obrigatorio('Nome')
  elif 'email' not in args:
    erro = msg_campo_obrigatorio('Email')
  elif 'CPF' not in args:
    erro = msg_campo_obrigatorio('CPF')
  elif 'telefone' not in args:
    erro = msg_campo_obrigatorio('Telefone')
  elif 'celular' not in args:
    erro = msg_campo_obrigatorio('Celular')
  elif 'endereco' not in args:
    erro = msg_campo_obrigatorio('Endereço')
  elif 'senha' not in args:
    erro = msg_campo_obrigatorio('Senha')
  elif 'confSenha' not in args:
    erro = msg_campo_obrigatorio('Confirmação da senha')
  elif args['confSenha'] != args['senha']:
    erro = 'A senha e confirmação de senha não são iguais.'
  elif re.match('(.*)(@)(.*)(\.com)', args['email']):
    erro = 'O e-mail não é valido.'
  elif len(args['senha']) < 8:
    erro = 'A senha é muito pequena'

  # Remove o campo confSenha, não mais necessário
  args.pop('confSenha', None)

  # !!! Precisa extrair dados do formulário {args} e montar um dicionário como {cria} quer. !!! 
  if not erro:
    usr = None
  else:
    usr = usuario.cria(args)

  conteudo = ""

  # Verifica se o usuário foi criado corretamente 
  # e retorna uma página de acordo com o resultado:
  if type(usr) is ObjUsuario:
    conteudo = gera_html_pag.mostra_usuario(ses, usr)
  else:
    erro = "Erro ao gerar novo usuário"
    conteudo = gera_html_pag.mensagem_de_erro(ses, erro)
  return conteudo
