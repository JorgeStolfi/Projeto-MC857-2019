# Funções úteis para testes.

import utils_testes_IMP

# MENSAGENS DE DIAGNÓSTICO

def erro_prog(mens):
  """Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o arquivo e linha da chamada
  e a palavra " ** erro: ", e aborta a execução com {assert False}.
  
  Esta função deve ser chamada apenas para informar erros do programa. 
  Erros em dados fornecidos pelo usuário (cliente ou administrador) devem ser enviados ao
  browser na forma de uma página HTML com a mensagem de erro (vide {gera_html_pag.mensagem_de_erro})."""
  utils_testes_IMP.erro_prog(mens)

def aviso_prog(mens, grave):
  """Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o arquivo e linha da chamada.
  Se {grave} for {True}, insere também a palavra " ** erro: ", senão insere palavra " !! aviso: ".
  Não aborta a execução e não retorna nada.  
  
  Esta função deve ser chamada apenas para depuração do programa. 
  Avisos destinados ao usuário (cliente ou administrador) devem ser enviados ao browser na forma
  de uma página HTML com a mensagem de erro (vide {gera_html_pag.mensagem_de_erro})."""
  utils_testes_IMP.aviso_prog(mens, grave)

def mostra(ind,mens):
  """Escreve a mensagem {mens} na saída {sys.stderr}, indentada de {ind} colunas.
  Útil para imprimir variáveis internas no diagnóstico de programas"""
  utils_testes_IMP.mostra(ind,mens)
  
# VERIFICAÇÃO BÁSICA DE OBJETOS

def verifica_objeto(modulo, tipo, obj, indice, ident, atrs):
  """Faz testes de consistência básicos de um objeto {obj} de classe {tipo}, 
  que deve ser uma das classes principais do sistems, como {ObjUsuario}, {ObjProduto}, etc.;
  dados o indice esperado {indice} na tabela correspondente da base de dados, o
  identificador esperado {ident}, e os atributos esperados {atrs}.
  
  
  Especifcamente, verifica as funções {obtem_indice(obj)}, {obtem_identificador(obj)},
  {obtem_atributos(obj)}, {busca_por_indice(indice)} e {busca_por_identificador(ident)}
  do {modulo} dado.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return utils_testes_IMP.verifica_objeto(modulo, tipo, obj, indice, ident, atrs)

# FORMATAÇÃO DE DADOS PARA DIAGNÓSTICO

def formata_dict(dados):
  """Esta função de depuração recebe um dicionário {dados}
  e devolve um string é um fragmento HTML5 que mostra esses
  dados em formato relativamente legível (JSON com quebras de
  linha e indentação)."""
  return utils_testes_IMP.formata_dict(dados)
