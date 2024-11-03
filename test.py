from pyspark import SparkContext
import sys

if __name__ == "__main__":
    sc = SparkContext(appName="RDD_Examples")
    my_list = sc.parallelize([1, 2, 3, 4, 5])
    my_other_list = sc.parallelize([x for x in range(0, 1)])
    # tweets = sc.textFile("hdfs:///user/cbw/a1_tweets.txt") # load data from HDFS
    words = sc.textFile("hdfs://localhost:9000/test/test.txt") # load data from HDFS
    print(words.collect())