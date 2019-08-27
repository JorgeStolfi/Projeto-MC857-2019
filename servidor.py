#! /usr/bin/python3

# Servidor do projeto MC857.

# Este script é o daemon servidor HTTP do website do projeto de MC857.

# O daemon é um programa python que roda sem parar no comutador local 
# ou no computador host do projeto, escutando na porta internet 8081. 
# Ao receber um comando HTTP (GET, POST, ou HEAD) enviado por 
# um usuário,  ele chama outros módulos do projeto para 
# criar uma página HTML5 com a resposta aproriada, e 
# envia a mesma de volta para o usuário.

# Implementação desta interface:
import servidor_IMP

def dispara():
  """Esta função inicia a execução do servidor."""
  servidor_IMP.dispara()

# Programa principal do servidor:
dispara()
