#Essa classe é usada para simular o comportamento de uma referência de um banco de dados.
import base_sql
import identificador
import sys # Para depuração.

def cria_tabela(bas):
    cmd = "CREATE  TABLE usuarios (" + \
    " indice int(8) NOT NULL AUTO_INCREMENT," + \
    " nome varchar(60) NOT NULL," + \
    " senha varchar(12) NOT NULL," + \
    " email varchar(60) NOT NULL," + \
    " CPF char(14) NOT NULL," + \
    " endereco varchar(180) NOT NULL," + \
    " CEP char(9) NOT NULL," + \
    " telefone varchar(24) NOT NULL," + \
    " PRIMARY KEY indice" + \
    ")"
    bas.executa_comando(cmd);

def acrescenta(bas,atrs):
    nomes = "nome,senha,email,CPF,endereco,CEP,telefone"
    valores = \
      atrs["nome"] + ", " + \
      atrs["senha"] + ", " + \
      atrs["email"] + ", " + \
      atrs["CPF"] + ", " + \
      atrs["endereco"] + ", " + \
      atrs["CEP"] + ", " + \
      atrs["telefone"]
    cmd = "INSERT INTO usuarios (" + nomes + ") VALUES (" + valores + ");"
    bas.executa_comando(cmd)
    ind = bas.indice_inserido()
    id_usuario = identificador.de_indice("U", ind)
    return id_usuario

def busca_por_identificador(bas,id_usuario):
    ind = identificador.para_indice("U", id_usuario)
    cmd = "SELECT nome,senha,email,CPF,endereco,CEP,telefone FROM usuarios WHERE indice = " + str(ind)
    res = bas.executa_comando(cmd)
    sys.stderr.write("res = " + str(res) + "\n")
    ind = 12345 # Temporário para teste.
    return res

def busca_por_email(bas,em):
    cmd = "SELECT indice FROM usuarios WHERE email = " + em
    res = bas.executa_comando(cmd)
    sys.stderr.write("res = " + str(res) + "\n")
    ind = 12345 # Temporário para teste.
    id_usuario = identificador.de_indice("U", ind)
    return id_usuario

def busca_por_CPF(bas,CPF):
    cmd = "SELECT indice FROM usuarios WHERE CPF = " + CPF
    res = bas.executa_comando(cmd)
    sys.stderr.write("res = " + str(res) + "\n")
    ind = 12345 # Temporário para teste.
    id_usuario = identificador.de_indice("U", ind)
    return id_usuario

def atualiza(bas,id_usuario,atrs):
    ind = identificador.para_indice("U", id_usuario)
    pares = ""
    for ch in ('nome', 'senha', 'email', 'CPF', 'endereco', 'CEP', 'telefone'):
       if ch in atrs:
         if pares != "": pares = pares + ", "
         pares = pares + ch + " = " + atrs[ch]
    cmd="UPDATE usuarios SET " + pares + " WHERE indice = " + str(ind)
    bas.executa_comando(cmd)
