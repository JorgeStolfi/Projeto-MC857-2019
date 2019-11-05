import frete_IMP

def calcula(cep,peso,volume):
    """
    Retorna o custo do frete {F*(A + Bvolume + Cpeso)}, onde os coeficientes
     {A}, {B}, e {C} são fixos e {F} depende dos dois primeiros 
     dígitos do CEP, definido por um dicionário.
    """
    return frete_IMP.calcula(cep,peso,volume)