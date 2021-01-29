# PySpark

# show schema
spk_df.printSchema()

# lazy evaluation (nothing calculated)
# spk_df.groupBy('Col1').mean('Col2')

# shows calcualuated result
# spk_df.groupBy('Col1').mean('Col2').show()

