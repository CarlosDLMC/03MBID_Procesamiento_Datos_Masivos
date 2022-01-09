#!/usr/bin/python

'''
Programa realizado por Jesus Moran
Este programa contiene un defecto que tienen que encontrar los alumnos
'''

import sys

subproblema = None
gastoMasFrecuente = None
conteoGastoMasFrecuente = None


for claveValor in sys.stdin:
    cliente, gasto, conteo = claveValor.strip().split("\t", 2)

    if subproblema == None:
        subproblema = cliente
	gastoMasFrecuente = gasto
	conteoGastoMasFrecuente = conteo

    if subproblema == cliente:
	if conteo > conteoGastoMasFrecuente:
		gastoMasFrecuente = gasto
		conteoGastoMasFrecuente = conteo	

    else:
	print("%s\t%s" % (subproblema, gastoMasFrecuente))

        subproblema = cliente
	gastoMasFrecuente = gasto
	conteoGastoMasFrecuente = conteo


print("%s\t%s" % (subproblema, gastoMasFrecuente))
