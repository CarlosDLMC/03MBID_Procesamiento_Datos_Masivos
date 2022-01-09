#!/usr/bin/python

import sys

''' 
Reducer de clientes con compras superiores a 1500 euros
Creado por Carlos de la Morena
'''

for line in sys.stdin:
    line = line.strip()
    name, money = line.split('\t', 1)
    money = int(money)

    if money > 1000:
        print(name)