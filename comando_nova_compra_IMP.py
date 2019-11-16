# Implementação do módulo {comando_finalizar_compra_IMP}

# Interfaces do projeto importadas por esta implementação:
import gera_html_pag
import compra
import sessao
import usuario
from utils_testes import erro_prog, mostra

# Outros módulos importados por esta implementação:
import sys

def processa(ses, args):
  sys.stderr.write("finalizando compra!\n")
  if ses == None:
    # O usuário não está logado. Exibe a tela de login:
    return gera_html_pag.entrar(ses, None)

  cliente = sessao.obtem_usuario(ses)
      
  if not sessao.aberta(ses):
    # Isto não deveria acontecer:
    erro_prog("carrinho fechado?")
     
  # Cria um novo carrinho vazio para esta sessão:
  cpr = compra.cria(cliente)
  sessao.muda_atributos(ses, { 'carrinho': cpr })
  usr = sessao.obtem_usuario(ses)
  idents = compra.busca_por_usuario(usuario.obtem_identificador(usr))
  pag = gera_html_pag.lista_de_compras(ses, idents, None)
  return pag
