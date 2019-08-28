import base_sessoes_IMP

def valida_busca_por_indice(base):
    sessao = Sessao.cria()
    id = base.acrescenta(sessao)
    resultado = base.busca_por_indice(id)
    if sessao != resultado:
        print("O resultado esperado era " + str(sessao) + " mas foi retornado " + str(resultado))
    else:
        print("Foi retornado o resultado esperado")

def valida_acrescenta(base):
    ultimo = base.indice_inserido()
    sessao = Sessao.cria()
    novo = base.acrescenta(sessao)
    if novo <= ultimo:
        print("O ID inserido esta incorreto")
    else:
        print("A entrada inserida está correta")

def valida_atualiza(base):
    ultimo = base.indice_inserido()
    ultima_sessao = base.busca_por_indice(ultimo)
    aberta = ultima_sessao.aberta()
    if aberta == True:
        ultima_sessao.logout()
    else:
        ultima_sessao.login(Usuario())
    nova_aberta = ultima_sessao.aberta()
    base.atualiza(ultima_sessao)

    resultado = base.busca_por_indice(ultimo)
    if resultado.aberta() != nova_aberta:
        print("O resultado esperado esta errado")
    else:
        print("O resultado espera está correto")


