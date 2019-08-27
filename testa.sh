#! /bin/bash

# Uso: "testa.sh {MODULO}"
# Executa "testes/{MODULO}_TST.py" e manda a saída "stdsaida" para testes/saida/{MODULO}.txt

modulo="$1"; shift  # 

export PYTHONPATH=".:testes:/usr/lib/python3.6/site-packages/sos/plugins" ; testes/${modulo}_TST.py > testes/saida/${modulo}.txt
