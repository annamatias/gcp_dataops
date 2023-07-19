from databricks.connect import DatabricksSession
import logging
import pprint


def setup_session():
    logging.info("Iniciando sessão no Databricks")
    return DatabricksSession.builder.getOrCreate()


def read_csv(spark):
    logging.info("Realizando leitura arquivo csv")
    df = spark.read.format("csv").option("header", True).load(
        "/tmp/cardiovascular-diseases-risk.csv")
    pprint(df.show(10, False))
    return df


def rename_columns(df):
    logging.info("Renomeando colunas")
    return df.withColumnRenamed("Height_(cm)", "Height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")


def save_delta(df):
    logging.info("Armazenando dados de forma particionada no storage cloud")
    df.write.format("delta").mode("overwrite").option("mergeSchema", "true").partitionBy("General_Health").save("/hospital/rw/cardiovascular_diseases/")


def main():
    spark = setup_session()
    df = read_csv(spark)
    df = rename_columns(df)
    save_delta(df)
