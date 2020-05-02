import os
import random
import re
import string
import sys

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as fn


APP_NAME = os.getenv('APP_NAME', 'count-letters')


def generate_text(lines=100, words=1000):
    text = []
    letters = list(string.ascii_lowercase)
    for _ in range(lines):
        line = []
        for _ in range(words):
            word_size = random.randint(1, 10)
            word = ''.join([
                random.choice(string.ascii_lowercase) for _ in range(word_size)
            ])
            line.append(word)
        text.append(' '.join(line))
    return '\n'.join(text)


def run_job(spark):
    text = generate_text()
    lines = spark.sparkContext.parallelize(text).map(lambda r: r[0])
    letters = lines.flatMap(
        lambda r: [c for c in r]
    ).map(
        lambda c: (c, 1)
    ).reduceByKey(lambda a, b: a + b)
    df = letters.toDF()
    df.orderBy('_2', ascending=False).limit(10).show()
    spark.stop()


if __name__ == '__main__':
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()
    run_job(spark)
