#! /usr/bin/python3
# Teste do módulo {tabelas}

import base_sql
import tabelas
import sys

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

sys.stderr.write("Abrindo as tabelas...\n")
tabelas.inicializa_todas(False)

# !!! Testar obtem_indice, obtem_obj
