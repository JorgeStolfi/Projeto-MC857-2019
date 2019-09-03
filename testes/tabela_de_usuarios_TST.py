#! /usr/bin/python3

#Testes do módulo {tabela_de_usuarios}
import tabela_de_usuarios
import base_sql
import identificador
import sys

# Conexao com a base de dados:
bas = base_sql.conecta("DB",None,None)

sys.stderr.write("Testando tabela_de_usuarios.py ...\n")

# Cria a tabela:
tabela_de_usuarios.cria_tabela(bas)

#Teste acrescenta
atrs = {
  "nome": "Josefino da Silva", 
  "senha": "12345", 
  "email": "fino@gmail.com", 
  "CPF": "123.456.789-00", 
  "endereco": "Rua Coronel General, 123\nVila Buracão\nCampinas, SP", 
  "CEP": "13083-418", 
  "telefone": "+55(19)9 9876-5432"
}
uid = tabela_de_usuarios.acrescenta(bas,atrs)
sys.stderr.write("acrescenta: uid = " + str(uid) + "\n")

res = tabela_de_usuarios.busca_por_identificador(bas,uid)
sys.stderr.write("busca_por_identificador: res = " + str(res) + "\n")

em = "fino@gmail.com"
res = tabela_de_usuarios.busca_por_email(bas,em)
sys.stderr.write("busca_por_email: res = " + str(res) + "\n")

CPF = "123.456.789-00"
res = tabela_de_usuarios.busca_por_CPF(bas,CPF)
sys.stderr.write("busca_por_CF: res = " + str(res) + "\n")

atrs_novo = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
tabela_de_usuarios.atualiza(bas,uid,atrs_novo)
sys.stderr.write("atualiza()\n")
res = tabela_de_usuarios.busca_por_identificador(bas,uid)
sys.stderr.write("busca_por_identificador: res = " + str(res) + "\n")

