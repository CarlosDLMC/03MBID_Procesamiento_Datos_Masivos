#!/usr/bin/python

import sys

''' 
Mapper de Cliente y dinero gastado
Creado por Carlos de la Morena Coco
El programa se puede ejecutar con el siguiente comando:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file mapper.py -mapper ./mapper.py -file combiner.py -combiner combiner.py -file reducer.py -reducer ./reducer.py -input clientes.txt -output clientes_que_gastan_mas_de_1000_euros
'''

for line in sys.stdin:
    line = line.strip()
    name, money = line.split(';', 1)
    print('%s\t%s' % (name, money))