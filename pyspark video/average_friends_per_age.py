from pyspark import SparkConf, SparkContext
import collections

def get_age_and_friends(line):
    line = line.split(',')
    return (int(line[0]), int(line[1]))

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile('users.txt')
age_friends = lines.map(get_age_and_friends)
counted = age_friends.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
averages = counted.mapValues(lambda x: x[0] / x[1])

results = collections.OrderedDict(averages.collect())
for k, v in results.items():
    print(f"Edad: {k}, media de amigos: {v}")