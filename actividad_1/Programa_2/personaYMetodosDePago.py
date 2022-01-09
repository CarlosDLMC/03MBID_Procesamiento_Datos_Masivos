from pyspark.sql import SparkSession

''' 
Programa creado por Carlos de la Morena
Este programa devuelve las personas que hayan gastado más de 1500 euros con tarjeta de crédito
con un único pago y la cantidad de esos pagos.
Este programa se puede ejecutar desde la IDE o con el comando:
spark-submit personaYMetodosDePago.py
'''

# inicializacion
spark = SparkSession.builder.appName('personaYMetodosDePago').getOrCreate()

entrada = "personas_y_pagos.txt"
salida1 = "comprasCreditoMayorDe1500"
salida2 = "comprasCreditoMenorDe1500"

datosEntrada = spark.sparkContext.textFile(entrada)

usuarios_pagos = datosEntrada.map(lambda linea: linea.split(";", 2))
usuarios_pagos = usuarios_pagos.map(lambda array: (array[0], (0, 0)) if array[1] != "Tarjeta de crédito" else (array[0], (1, 0) if int(array[2]) > 1500 else (0, 1))) # Izquierda - más de 1500, Derecha - menos
usuarios_pagos = usuarios_pagos.reduceByKey(lambda count, next: (count[0] + next[0], count[1] + next[1]))
usuarios_pagos_credito_mayor_1500 = usuarios_pagos.map(lambda array: f"{array[0]};{array[1][0]}")
usuarios_pagos_credito_menor_1500 = usuarios_pagos.map(lambda array: f"{array[0]};{array[1][1]}")

usuarios_pagos_credito_mayor_1500.saveAsTextFile(salida1)
usuarios_pagos_credito_menor_1500.saveAsTextFile(salida2)