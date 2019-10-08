# Implementação do módulo {comando_submit_entrar}.

# Interfaces do projeto usadas por esta implementação:
import usuario
import sessao
import compra
import gera_html_pag

# Outros módulos usados por esta implementação:
import secrets

def processa(ses, dados):
  if ses != None:
    # Não deveria acontecer, mas por via das dúvidas:
    return gera_html_pag.mensagem_de_erro(None, "Favor sair da sessão corrente primeiro")
  email = dados['email']
  senha = dados['senha'] 
  id_usuario = usuario.busca_por_email(email)
  if id_usuario != None:
    usr = usuario.busca_por_identificador(id_usuario)
    atrs_usr = usuario.obtem_atributos(usr)
    if atrs_usr["senha"] == senha:
      cookie = secrets.token_urlsafe(32) 
      # !!! (MAIS TARDE) Deveria buscar nas compras deste usuário as compras abertas; se tiver, pedir para ele escolher. !!!
      carrinho = compra.cria(usr)
      ses_nova = sessao.cria(usr, cookie, carrinho)
      return gera_html_pag.principal(ses_nova)
    else:
      return gera_html_pag.mensagem_de_erro(None, "Senha incorreta")
  else:
    return gera_html_pag.mensagem_de_erro(None, "Usuário " + email + " não está cadastrado")
