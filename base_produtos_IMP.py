#!/usr/bin/python3

#Pedro Henrique Barcha Correia (PedroBarcha)
#158338
#Última Atualização: 20/08

#Implementação da base de produtos, conforme descrita na interface base_produtos.py

###	IMPORTANTE ###
#Conforme conversado não participarei das aulas dos dias 20 e 27, devido à intervenção cirúrgica, portanto fiz algumas suposições no código
##################

#Supondo que vamos usar pymysql
import pymysql

def conecta():
	host = "127.0.0.1"
	user = "root"
	db = "mysql"

	try:
		#conecta à base de dados
		conexao_mysql = pymysql.connect(host=host, unix_socket='/tmp/mysql.sock', user=user, passwd=None, db=db)

		print("SUCESSO em estabelecer conexao com o banco de dados!")
		return conexao_mysql
	
	except:
		print("FALHA ao estabelecer conexao com o banco de dados!")
		return None


def desconecta(conexao_mysql):
	conexao_mysql.cursor().close()
	conexao_mysql.close()
	

def busca_por_nome(nome, conexao_mysql):
	try:
		#executa busca no banco de dados
		cursor_mysql = conexao_mysql.cursor()
		cursor_mysql.execute("SELECT nome FROM produto")
		produtos_econtrados = cursor_mysql.fetchone()


		print("Produtos encontrados: "+produtos_econtrados)
		return produtos_econtrados

	finally:
		#fecha conexao com o banco de dados
		desconecta(conexao_mysql)

def busca_por_id(id, conexao_mysql):
	try:
		#executa busca no banco de dados
		cursor_mysql = conexao_mysql.cursor()
		cursor_mysql.execute("SELECT id FROM produto")
		produtos_econtrados = cursor_mysql.fetchone()

		print("Produtos encontrados: "+produtos_econtrados)
		return produtos_econtrados
	
	finally:
		#fecha conexao com o banco de dados
		desconecta(conexao_mysql)
