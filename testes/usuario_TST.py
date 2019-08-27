import usuario

"""
Estrategia de teste

1. cria() TODO depende da base
    (a) sem atributos 
    (c) com atributos total

2. obtem_identificador TODO depende da base
    (a) antes de cria() => None
    (b) apos cria()

3. muda_atributos TODO depende da base
    (a) email ou cpf repetidos
    (b) sem elementos repetidos
"""

# Teste cria()
usr1_atrs = {"nome":"Joao Silva", "senha":"1234", "CPF":"91919191", \
            "endereco": "Rua 1, N 100", "telefone": "19 9999-9999", 
            "nascDt": "2001-01-01", "email": "joao@gmail.com"}
usr2_atrs = {"nome":"Maria Souza", "senha":"4321", "CPF":"82828282", \
            "endereco": "Rua 1, N 50", "telefone": "19 9999999", \
            "nascDt": "2002-02-02", , "email": "maria@gmail.com"}
usr3_atrs = {}
usr4_atrs = {"nome":"Muda Atributo", "senha":"4321", "CPF":"111111111", \
            "endereco": "Rua 1, N 50", "telefone": "19 9999999", \
            "nascDt": "2002-02-02", , "email": "muda@gmail.com"}

usr1 = usuario.cria(usr1_atrs)
usr2 = usuario.cria(usr2_atrs)
usr3 = usuario.cria(usr3_atrs)

print(usr1_atrs = usr1.obtem_atributos())
print(usr2_atrs = usr2.obtem_atributos())
print(usr3_atrs = usr3.obtem_atributos())

# Teste muda_atributos
usr2.muda_atributos(usr1) # Não deveria mudar os atributos

print(usr2_atrs = usr2.obtem_atributos())

usr2.muda_atributos(usr4) # Deveria assumir os valores do usr4

print(usr4_atrs = usr2.obtem_atributos())
