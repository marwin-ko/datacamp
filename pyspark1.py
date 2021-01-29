# PySpark

# show schema
spk_df.printSchema()

# lazy evaluation (nothing calculated)
# spk_df.groupBy('Col1').mean('Col2')

# shows calcualuated result
# spk_df.groupBy('Col1').mean('Col2').show()


# example of standalone script
from pyspark.sql import SparkSession
if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    spk_df = (spark
        .read
        .csv("./data.csv",
             header=True,
             inferSchema=True,
             escape='"'))

    spk_df = (spk_df
        .withColumn("Height",
                    spk_df.Height.cast("integer")))

    print(spk_df
        .groupBy('Year')
        .mean('Height')
        .orderBy('Year')
        .show())
# end of script



