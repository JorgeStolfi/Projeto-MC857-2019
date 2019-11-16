# Implementação do módulo {comando_finalizar_compra_IMP}

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
  print("\n----\n\n\nprocessa args: \n" + str(args) + "\n\n\n---\n")
  if ses == None:
    # O usuário não está logado. Exibe a tela de login:
    return gera_html_pag.entrar(ses, None)

  cliente = sessao.obtem_usuario(ses)
      
  if not sessao.aberta(ses):
    # Isto não deveria acontecer:
    erro_prog("carrinho fechado?")
     
  # Localiza a compra {cpr}:
  id_compra = args['id_compra'][0]
  cpr = compra.busca_por_identificador(id_compra)
  # !!! Deveria verificar se {ses} e {cpr} pertencem ao mesmo usuário !!!
  compra.fecha_compra(cpr)

  if cpr == sessao.obtem_carrinho(ses):
    # Cria um novo carrinho vazio para esta sessão:
    novo_carr = compra.cria(cliente)
    sessao.muda_atributos(ses, { 'carrinho': novo_carr })

  # Mostra a compra que foi fechada:
  pag = gera_html_pag.mostra_compra(ses, cpr, None)
  return pag
