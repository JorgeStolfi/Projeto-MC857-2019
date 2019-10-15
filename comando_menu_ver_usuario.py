# Este módulo processa a seleção pelo usuário de um usuario numa página 
# com uma lista de vários usuarios, a fim de ver a descrição detalhada
# do mesmo.

import comando_menu_ver_usuario_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário apertou um botão 
    "Minha conta" ou equivalente no menu geral.
    
    Ela devolve uma página HTML com um formulário
    semelhante ao formulário de cadastrar usuário, mas
    com os campos já preenchidos (menos a senha) e 
    aditáveis (menos email e CPF).
    No fundo da página deve haver um botão "Alterar"
    em vez de "Cadastrar". 
    
    O usuário é o dono da sessão {ses}, que não pode ser {None}
    (isto é, o usuário precisa estar logado)."""
    return comando_menu_ver_usuario_IMP.processa(ses, args)
