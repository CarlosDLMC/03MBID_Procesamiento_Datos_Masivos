#!/usr/bin/python

'''
Programa realizado por Jesus Moran
Este programa contiene un defecto que tienen que encontrar los alumnos
'''

import sys

subproblema = None
conteoGastos = {}

for claveValor in sys.stdin:
    cliente, gasto, conteo = claveValor.strip().split("\t", 3)

    if subproblema == None:
        subproblema = cliente


    if subproblema == cliente:
	if gasto not in conteoGastos:
		conteoGastos[gasto] = 0	
	conteoGasto = int(conteoGastos[gasto]) + int(conteo)
	conteoGastos.update({gasto:conteoGasto})
	

    else:	
	for gasto in conteoGastos:
		gastoCliente = conteoGastos[gasto]
		print("%s\t%s\t%s" % (subproblema, gasto, gastoCliente))
        
        subproblema = cliente
	conteoGastos = {gasto:conteo}


for gasto in conteoGastos:
	gastoCliente = conteoGastos[gasto]
	print("%s\t%s\t%s" % (subproblema, gasto, gastoCliente))
