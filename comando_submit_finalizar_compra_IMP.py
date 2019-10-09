# Implementação do módulo {comando_submit_finalizar_compra_IMP}

# Interfaces do projeto importadas por esta implementação:
import gera_html_pag
import compra
import produto
import sessao
from utils_testes import erro_prog, mostra

# Outros módulos importados por esta implementação:
import sys

def processa(ses, args):
  sys.stderr.write("finalizando compra!\n")
  # Se a sessão for None, exibe a tela de login
  if ses == None or not(sessao.aberta(ses)):
      return gera_html_pag.entrar(ses)

  # Fecha o carrinho corrente:
  id_compra = args['id_compra']
  cpr = compra.busca_por_identificador(id_compra)
  compra.fecha_compra(cpr)

  # Cria um novo carrinho vazio para esta sessão:
  cliente = sessao.obtem_usuario(ses)
  novo_carr = compra.cria(cliente)
  sessao.muda_atributos(ses, { 'carrinho': novo_carr })

  # Mostra a compra que foi fechada:
  return gera_html_pag.mostra_compra(ses, cpr)
