
import utils_testes
import utils_testes_AUX; from utils_testes_AUX import ObjTeste, obj1, obj1_ind, obj1_id, obj1_atrs
import sys
from utils_testes import erro_prog, mostra

# ----------------------------------------------------------------------
sys.stderr.write("testando {utils_testes.mostra}\n")
for p in range(10):
  utils_testes.mostra(2*p, ("indentado por %d" % (2*p)))
  
# ----------------------------------------------------------------------
sys.stderr.write("testando {utils_testes.verifica_objeto}\n") 

sys.stderr.write("verificando objeto %s\n" % "obj1") 
utils_testes.verifica_objeto(utils_testes_AUX, ObjTeste, obj1, obj1_ind, obj1_id, obj1_atrs)
sys.stderr.write("\n")

# ----------------------------------------------------------------------
sys.stderr.write("testando {utils_testes.formata_dict}\n")

d1 = { 'coisa': 100, 'treco': 200, 'lhufas': [ 10, 100 ], 'picas': { 'sim': 100, 'nao': 200, 'bah': 123 } }
fd1 = utils_testes.formata_dict(d1);
sys.stderr.write("d1 formatado\n%s\n" % fd1)

