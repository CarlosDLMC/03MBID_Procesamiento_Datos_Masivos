import sys
import os
from pyspark.sql import SparkSession

''' 
Programa creado por Carlos de la Morena
Este programa devuelve la categoría de vídeos más visitada y el número 
total de visitas de la misma.
El comando que he usado en local para ejecutar este programa ha sido:
spark-submit CategoriaDeVideosMasVista.py 0222 resultados
'''

spark = SparkSession.builder.appName('miWordCount').getOrCreate()

entrada = sys.argv[1]
files = os.listdir(entrada)
files.remove("log.txt")
files = [entrada + "/" + file for file in files]
salida = sys.argv[2]

datosEntrada = spark.sparkContext.textFile(",".join(files))
categorias = datosEntrada.filter(lambda line: line.count("\t") > 2)
categorias = categorias.map(lambda line: line.split("\t")[3])
categorias = categorias.map(lambda word: (word, 1))
categorias = categorias.reduceByKey(lambda total, next: total + next)
categorias = categorias.reduce(lambda maximo, next: maximo if maximo[1] > next[1] else next)
most_popular = spark.sparkContext.parallelize([categorias]).map(lambda line: f"{line[0]};{line[1]}")

most_popular.saveAsTextFile(salida)