#!/usr/bin/python

'''
Programa realizado por Jesus Moran
Este programa contiene un defecto que tienen que encontrar los alumnos
'''

import sys

for linea in sys.stdin:
	linea = linea.strip()
	cliente,gasto = linea.split("\t", 1)
	print("%s\t%s\t%s" % (cliente, gasto, 1))
