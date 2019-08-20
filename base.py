#!/usr/bin/python3

#Guilherme Luis Domingues (guilhermeluisdomingues)
#155619
#Ultima Atualizacao: 20/08

# Funcao para criar e executar queries

# Esta funcao deve executar a query solicitada

# Implementacao desta interface:
import base_IMP

def conecta():
  """Devolve uma conexao com a base. Se houver algum erro, devolve {None}."""
  return base_IMP.conecta()

def executa_query(query):
  """Devolve o resultado da query executada. Se não houver algo que satisfaz essa busca, devolve {None}."""
  return base_IMP.executa_query(query)