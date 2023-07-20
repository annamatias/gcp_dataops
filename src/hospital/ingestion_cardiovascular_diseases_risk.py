# import pprint
import logging
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip


def setup_session():
    builder = SparkSession.builder.appName("Ingestão Cardio") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    return spark


def read_csv(spark, path="gcp_dataops/data_source/cardiovascular-diseases-risk.csv"):
    logging.info("Realizando leitura arquivo csv")
    df = spark.read.format("csv").option("header", True).load(path)
    # pprint.pprint(df.show(10, False))
    return df


def rename_columns(df):
    logging.info("Renomeando colunas")
    return df.withColumnRenamed("Height_(cm)", "Height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")


def save_delta(df, path_save="gcp_dataops/storage/hospital/rw/cardiovascular_diseases/"):
    logging.info("Armazenando dados de forma particionada no storage cloud")
    df.write.format("delta").mode("overwrite").option("mergeSchema", "true").partitionBy(
        "General_Health").save(path_save)


def main():
    spark = setup_session()
    df = read_csv(spark)
    df = rename_columns(df)
    save_delta(df)
    spark.stop()


if __name__ == '__main__':
    main()
