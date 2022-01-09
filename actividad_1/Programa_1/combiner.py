#!/usr/bin/python

import sys

''' 
Combiner de clientes con compras superiores a 1500 euros
Creado por Carlos de la Morena
'''


current_client = ''
current_money = 0
client = ''

for line in sys.stdin:
    line = line.strip()
    client, money = line.split('\t', 1)
    money = int(money)

    if current_client == client:
        current_money += money
    else:
        if current_client:
            print('%s\t%s' % (current_client, current_money))
        current_client, current_money = client, money
# print(f"{current_client}\t{current_money}")
print('%s\t%s' % (current_client, current_money))