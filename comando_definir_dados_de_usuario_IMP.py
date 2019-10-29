# Implementação do módulo {comando_definir_dados_de_usuario}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import gera_html_pag
from utils_testes import erro_prog, mostra
import re
#{'celular': '165156165165', 'cpf': '651651651651', 'endereco': 'av rua da casa', 'confSenha': '123456', 'cep': '6156-561', 'email': 'lucianocps9@gmail.com', 'telefone': '651561651561', 'nome': 'Luciano', 'senha': '123456', 'estado': 'AP'}

import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):
  erro = ''

  # Validação dos campos
  if 'nome' not in args:
    erro = msg_campo_obrigatorio('Nome')
  elif 'email' not in args:
    erro = msg_campo_obrigatorio('Email')
  elif 'CPF' not in args:
    erro = msg_campo_obrigatorio('CPF')
  elif 'endereco' not in args:
    erro = msg_campo_obrigatorio('Endereço')
  elif 'CEP' not in args:
    erro = msg_campo_obrigatorio('CEP')
  elif 'telefone' not in args:
    erro = msg_campo_obrigatorio('Telefone')
  elif 'senha' not in args:
    erro = msg_campo_obrigatorio('Senha')
  elif len(args['senha']) < 8:
    erro = 'A senha é muito pequena'
  elif len(args['senha']) > 24:
    erro = 'A senha é muito grande'
  elif len(args['CPF']) < 14:
    erro = 'O CPF é muito pequeno'
  elif len(args['CPF']) > 15:
    erro = 'O CPF é muito grande'
  elif len(args['nome']) < 1 or len(args['nome']) > 60:
    erro = 'O tamanho do nome deve ser entre 1 e 60 caracteres'  
  elif len(args['email']) < 6 or len(args['email']) > 60:
    erro = 'O tamanho do email deve ser entre 6 e 60 caracteres'  
  elif len(args['endereco']) < 10 or len(args['endereco']) > 180:
    erro = 'O tamanho do endereco deve ser entre 10 e 180 caracteres'  
  elif len(args['documento']) < 6 or len(args['documento']) > 24:
    erro = 'O tamanho do documento deve ser entre 6 e 24 caracteres'  
  elif len(args['telefone']) < 9 or len(args['telefone']) > 40:
    erro = 'O tamanho do telefone deve ser entre 9 e 40 caracteres'  

  # Converte bit de administrador para bool:
  if 'administrador' in args:
    args['administrador'] = True
  else:
    args['administrador'] = False
    
  if not erro:
    usr = usuario.cria(args)
  else:
    usr = None
    sys.stderr.write("err:" + erro)

  # Verifica se o usuário foi criado corretamente 
  # e retorna uma página de acordo com o resultado:
  if type(usr) is ObjUsuario:
    pag = gera_html_pag.mostra_usuario(ses, usr)
  else:
    err = "Erro ao gerar novo usuário: " + erro
    pag = gera_html_pag.mensagem_de_erro(ses, err)
  return pag
