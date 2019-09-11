#módulo para testar comando_botao_sair.py
import sys
sys.path.append('/home/cc2016/ra173711/mc857/data/173711')
import sessao
import usuario
import comando_botao_sair

objeto_usuario = usuario.cria({"nome":"Jose","senha":"1234","email":"jose@einrot.com","CPF":"212.343.542-56","endereco":"Av Paulista","CEP":"04567-345","telefone":"(11)32444709"})
objeto_sessao = sessao(objeto_usuario)

resultado = comando_botao_sair.processa(objeto_sessao)

f = open("comando_botao_sair", "w")
f.write(resultado)
f.close()