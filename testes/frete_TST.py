import frete
import sys
import utils_testes

def verifica_calcula(cep,peso,volume):
    sys.stderr.write("Testanado calcula em frete")
    clc_frt = frete.calcula(cep,peso,volume)
    if clc_frt != frt_esp:
        utils_testes.aviso_prog("Retornou " + str(clc_frt) + ", deveria ter retornado " + str(frt_esp),True )


#teste
frt_esp = 12.35
verifica_calcula(13083872,2,4)
