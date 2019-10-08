#! /usr/bin/python3

import tabela_generica

def testa_comando_cadastrar_usuario(conteudo_cadastro):
  return tabela_generica.busca_por_semelhanca("usuarios", conteudo_cadastro)
