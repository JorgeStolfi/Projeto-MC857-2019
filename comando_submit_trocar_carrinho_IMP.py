# Implementação do módulo {comando_submit_trocar_carrinho}.

import compra
import comando_menu_ver_carrinho
import sessao
import gera_html_pag
import usuario

def processa(ses, args):
  if 'id_compra' not in args:
    return gera_html_pag.mensagem_de_erro(ses, "O identificador do novo carrinho não foi enviado.")

  # Localiza a compra {cpr}:
  id_compra = args['id_compra']
  novo_carr = compra.busca_por_identificador(id_compra)
  if novo_carr == None:
    return gera_html_pag.mensagem_de_erro(ses, "O carrinho escolhido não existe.")

  usuario_da_compra = compra.obtem_cliente(novo_carr)
  if usuario_da_compra == None:
    return gera_html_pag.mensagem_de_erro(ses, "A carrinho não possui um usuário associado a ele.")

  usuario_da_sessao = sessao.obtem_usuario(ses)
  if usuario_da_sessao == None:
    return gera_html_pag.mensagem_de_erro(ses, "A sessao não possui um usuário associada a ela.")

  if usuario.obtem_identificador(usuario_da_sessao) != usuario.obtem_identificador(usuario_da_compra):
    return gera_html_pag.mensagem_de_erro(ses, "O carrinho não esta atribuído ao cliente da sessão.")

  sessao.muda_atributos(ses, {'carrinho': novo_carr})

  return comando_menu_ver_carrinho.processa(ses, args)
