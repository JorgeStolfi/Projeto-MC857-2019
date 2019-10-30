# Implementação do módulo {comando_fazer_login}.

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
  
  ses_nova = ses # Caso o login falhe.
  if id_usuario != None:
    usr = usuario.busca_por_identificador(id_usuario)
    atrs_usr = usuario.obtem_atributos(usr)
    if atrs_usr["senha"] == senha:
      cookie = secrets.token_urlsafe(32)
      # !!! (MAIS TARDE) Deveria buscar nas compras deste usuário as compras abertas; se tiver, pedir para ele escolher. !!!
      carrinho = define_carrinho(usr, id_usuario)
      ses_nova = sessao.cria(usr, cookie, carrinho)
      pag = gera_html_pag.principal(ses_nova)
    else:
      pag = gera_html_pag.mensagem_de_erro(None, "Senha incorreta")
  else:
    pag = gera_html_pag.mensagem_de_erro(None, "Usuário " + email + " não está cadastrado")
  return pag, ses_nova

#Essa funcao busca por compras em aberto, se tiver alguma nessa condicao, entao tal compra sera usada como carrinho, caso contrario, o carrinho sera vazio.
def define_carrinho(usr, id_usuario):
    lista_id_compras = compra.busca_por_usuario(id_usuario)
    if not lista_id_compras:
        return compra.cria(usr)
    else:
        for id_compra in lista_id_compras:
            obj_compra = compra.busca_por_identificador(id_compra)
            if compra.obtem_status(obj_compra) == 'aberto':
                return obj_compra
    return compra.cria(usr)
