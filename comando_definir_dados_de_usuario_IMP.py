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
  elif 'CEP' not in args:
    erro = msg_campo_obrigatorio('CEP')
  elif 'telefone' not in args:
    erro = msg_campo_obrigatorio('Telefone')
  elif 'senha' not in args:
    erro = msg_campo_obrigatorio('Senha')
  elif len(args['senha']) < 8:
    erro = 'A senha é muito pequena'
  elif 'rua_numero' not in args:
    erro = msg_campo_obrigatorio('Rua e Número')
  elif 'bairro' not in args:
    erro = msg_campo_obrigatorio('Bairro')
  elif 'cidade_estado' not in args:
    erro = msg_campo_obrigatorio('Cidade e Estado')
  else
    # Adiciona o campo endereco formatado como 'Rua, número\nBairro\nCidade, UF'
    args['endereco'] = args['rua_numero'] + '\n' + args['bairro'] + '\n' + args['cidade_estado']
    args.pop('rua_numero', None)
    args.pop('bairro', None)
    args.pop('cidade_estado', None)

  # Remove o campos, não mais necessários
  args.pop('conf_senha', None)
  
  # Converte bit de administrador para bool:
  args['administrador'] = ('administrador' in args)

  if not erro:
    usr = None
    
  if 'id_usario' in args:
    del args['id_usuario']
  
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
    pag = gera_html_pag.mensagem_de_erro(ses, erro)
  return pag
