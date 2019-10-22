import sessao
import compra
import usuario
import gera_html_pag

def processa(ses, args):
    if ses == None:
        return gera_html_pag.entrar(ses)

    cpr = sessao.obtem_carrinho(ses)
    usr_ses = sessao.obtem_usuario(ses)
    usr_cpr = compra.obtem_cliente(cpr)
    
    if (usuario.obtem_identificador(usr_ses) != usuario.obtem_identificador(usr_cpr)):
        return gera_html_pag.mensagem_de_erro(ses, "Usuário do carrinho inválido")

    id_compra = args['id_compra']
    novo_endereco = args['endereco']
    novo_cep = args['CEP']

    compra.muda_atributos(cpr, { 'endereco' : novo_endereco, 'CEP' : novo_cep })
    nova_cpr = compra.busca_por_identificador(id_compra)

    return gera_html_pag.mostra_compra(ses, nova_cpr)