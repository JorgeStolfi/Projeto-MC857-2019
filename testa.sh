#! /bin/bash

# Uso: "testa.sh {MODULO}"
# Executa "testes/{MODULO}_TST.py" e manda a saída "stdsaida" para testes/saida/{MODULO}.html

modulo="$1"; shift  # 

echo "=== testando módulo ${modulo} ============================="
rm -fv testes/saida/${modulo}.html testes/saida/${modulo}.*.html 
export PYTHONPATH=".:testes:..:/usr/lib/python3.6/site-packages/sos/plugins" ; \
  python3 testes/${modulo}_TST.py > testes/saida/${modulo}.html
echo "======================================================================"
