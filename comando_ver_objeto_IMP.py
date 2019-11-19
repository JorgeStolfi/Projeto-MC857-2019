# Implementação do módulo {comando_ver_objeto}.

# Interfaces do projeto usadas por esta implementação:
import usuario
import sessao
import compra
import produto
import gera_html_pag

# Outros módulos usados por esta implementação:
import secrets

def processa(ses, args):
  id_objeto = args['id_objeto']
  id_objeto = id_objeto.split('-')
  type_objeto = id_objeto[0]
  id_objeto = id_objeto[1]
  
  if type_objeto == "P":
    id_produto = args['id_objeto']
    # Considerando prod como objeto da classe Produto
    prod = produto.busca_por_identificador(id_produto)
    atrs_produto = produto.obtem_atributos(prod)
    if ('quantidade' in args) and ('quantidade' in atrs_produto):
      # No maximo a maior quantidade disponivel para o produto
      qtd = min(float(args['quantidade']), float(atrs_produto['estoque']))
    else:
      qtd = 1.0
    pag = gera_html_pag.mostra_produto(ses, None, prod, qtd, None)
    return pag
  
  elif type_objeto == "C":
    id_compra = args['id_objeto']
    # Considerando cpr como objeto da classe Compra
    cpr = compra.busca_por_identificador(id_compra)
    pag = gera_html_pag.mostra_compra(ses,cpr, None)
    return pag

  elif type_objeto == "U":
    id_usuario = args['id_objeto']
    # Considerando usr como objeto da classe Usuário
    erros = []
    usr = usuario.busca_por_identificador(id_usuario)
    if(usr == None):
      erros.append("Usuário não encontrado")
    else:
      erros = None
      args = usuario.obtem_atributos(usr)

    pag = gera_html_pag.alterar_usuario(ses,id_usuario, args, erros)
    return pag

  elif type_objeto == "S":
    id_sessao = args['id_objeto']
    pag = gera_html_pag.mostra_sessao(ses, None)
    return pag
