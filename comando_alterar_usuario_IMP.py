# Implementação do módulo {comando_alterar_usuario}.

import gera_html_pag
import usuario; from usuario import ObjUsuario
import sessao
from utils_testes import erro_prog, mostra
from valida_campo import ErroAtrib
import re
import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):
  
  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses == None:
    # Não deveria acontecer:
    erro_prog("alteração de conta só é permitida se usuário estiver logado")
  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses != None
  admin = usuario.obtem_atributos(usr_ses)['administrador']
  
  # Determina o usuário a alterar:
  if not 'id_usuario' in args:
    # Não deveria acontecer:
    erro_prog("falta campo 'id_usuario'")
  id_usuario = args['id_usuario'];
  usr_alt = usuario.busca_por_identificador(id_usuario);

  if usr_alt == None: 
    # Não deveria ocorrer:
    erro_prog('usuario inexistente')
  assert usuario.obtem_identificador(usr_alt) == id_usuario # Paranóia.
      
  if not admin and (usr_alt != usr_ses):
    # Não deveria ocorrer:
    erro_prog('operação não permitida para este usuário')
    
  # Remove campo {id_usuario}, não mais necessário:
  del args['id_usuario']
  
  try:
    usuario.confere_e_elimina_conf_senha(args)
    usuario.muda_atributos(usr_alt, args)
    pag = gera_html_pag.principal(ses, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    id_usuario = usuario.obtem_identificador(usr_alt)
    pag = gera_html_pag.alterar_usuario(ses, id_usuario, args, erros)

  return pag
