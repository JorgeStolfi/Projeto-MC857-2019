# Implementação do módulo {comando_trocar_carrinho}.

import gera_html_pag
import produto
import compra
import re
import sessao
import usuario
import itens_de_compras
import sys

def filtra_compras_do_cliente(cliente, compras_com_produto):
  compras_do_cliente = []
  for cpr in compras_com_produto:
    if usuario.obtem_identificador(compra.obtem_atributos(cpr)['cliente']) == usuario.obtem_identificador(cliente):
      compras_do_cliente.append(cpr)
  return compras_do_cliente

def processa(ses, args):
  if 'id_produto' not in args:
    # Não deveria acontecer, mas...
    return gera_html_pag.mensagem_de_erro(ses, "O identificador do produto não foi enviado.")
  
  if not re.match('(P-)([0-9]{8})', args['id_produto']):
    # Não deveria acontecer, mas...
    return gera_html_pag.mensagem_de_erro(ses, "O identificador P-{NNNNNNNN} do produto é invalido.")
  
  if produto.busca_por_identificador(args['id_produto']) == None:
    # Não deveria acontecer, mas...
    return gera_html_pag.mensagem_de_erro(ses, "Este identificador não esta atrelado a nenhum produto.")
  
  ids_compras = itens_de_compras.busca_por_produto(args['id_produto'])
  usuario_da_sessao = (sessao.obtem_usuario(ses) if ses != None else None)

  if usuario_da_sessao == None:
    # Não deveria acontecer, mas...
    return gera_html_pag.mensagem_de_erro(ses, "A sessão não esta atrelada a nenhum usuário.")

  if usuario.obtem_atributos(usuario_da_sessao)['administrador'] == False:
    # Mostra só as compras do usuário logado que incluem o produto:
    ids_compras = filtra_compras_do_cliente(usuario_da_sessao, ids_compras)

  pag = gera_html_pag.lista_de_compras(ses, ids_compras, None)
  return pag
