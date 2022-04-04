from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext, SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.sql.types import *
from pyspark.ml.feature import *

sc = SparkContext()
spark = SparkSession(sc)
sqlContext = SQLContext(sc)

COLUMN = [
    StructField('f1', FloatType(), True),
    StructField('f2', FloatType(), True),
    StructField('f3', FloatType(), True),
    StructField('f4', FloatType(), True),
    StructField('f5', FloatType(), True),
    StructField('f6', FloatType(), True),
    StructField('f7', FloatType(), True),
    StructField('f8', FloatType(), True),
    StructField('target', FloatType(), True),
]

def predict(df_train, df_test):
    # TODO: Train random forest classifier

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use

    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    return []


def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # TODO: Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map( lambda f: [float(e) for e in f.split(',')] )

    # TODO: Create dataframe from the RDD
    df_train = spark.createDataFrame(rdd_train, StructType(COLUMN))
    df_train.show()

    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Convert text file lines into an RDD we can use later
    rdd_test = raw_test_data.map( lambda f: [float(e) for e in f.split(',')] )

    # TODO:Create dataframe from RDD
    df_test = spark.createDataFrame(rdd_test, StructType(COLUMN[:-1]))
    df_test.show()

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()
