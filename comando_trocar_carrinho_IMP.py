# Implementação do módulo {comando_trocar_carrinho}.

import compra
import comando_ver_carrinho
import sessao
import gera_html_pag
import usuario

def processa(ses, args):
  if 'id_compra' not in args:
    return gera_html_pag.mensagem_de_erro(ses, "O identificador do novo carrinho não foi enviado.")

  if ses == None:
    return gera_html_pag.mensagem_de_erro(ses, "Usuário não está logado.")

  # Localiza a compra {cpr}:
  id_compra = args['id_compra']
  novo_carr = compra.busca_por_identificador(id_compra)
  if novo_carr == None:
    pag = gera_html_pag.mensagem_de_erro(ses, "O carrinho escolhido não existe.")
    return pag

  usuario_da_compra = compra.obtem_cliente(novo_carr)
  if usuario_da_compra == None:
    pag = gera_html_pag.mensagem_de_erro(ses, "A carrinho não possui um usuário associado a ele.")
    return pag

  usuario_da_sessao = sessao.obtem_usuario(ses)
  if usuario_da_sessao == None:
    pag = gera_html_pag.mensagem_de_erro(ses, "A sessao não possui um usuário associada a ela.")
    return pag

  if usuario_da_sessao != usuario_da_compra:
    pag = gera_html_pag.mensagem_de_erro(ses, "O carrinho não esta atribuído ao cliente da sessão.")
    return pag

  sessao.muda_atributos(ses, {'carrinho': novo_carr})

  pag = gera_html_pag.mostra_carrinho(ses, None)
  return pag
