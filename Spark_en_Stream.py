from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

def sumar(line):
    total = 0
    for i in line.split(";"):
        total += int(i)
    return total

sc = SparkContext(appName="streamingShit")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 2)

input_stream = ssc.socketTextStream("localhost", 9999)
nuevo_stream = input_stream.map(sumar)

nuevo_stream.pprint()

ssc.start()
ssc.awaitTermination()