Programa escrito por Carlos de la Morena Coco el 8 de enero de 2022.

El programa consta de 3 partes:
-El mapper: de cada línea obtiene un par clave - valor
-El combiner: calcula el dinero total gastado por cada cliente
-El reducer: muestra los clientes que hayan gastado más de 1000 euros

El comando para correr este programa es el siguiente:
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -file mapper.py -mapper ./mapper.py -file combiner.py -combiner combiner.py -file reducer.py -reducer ./reducer.py -input clientes.txt -output clientes_que_gastan_mas_de_1000_euros