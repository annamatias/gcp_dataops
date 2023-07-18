# Databricks notebook source
# MAGIC %md
# MAGIC # Ingestão de Dados ELT
# MAGIC > Conjunto de dados de previsão de risco de doenças cardiovasculares

# COMMAND ----------

display(dbutils.fs)

# COMMAND ----------

display(dbutils.fs.ls("/"))

# COMMAND ----------

# DBTITLE 1,Leitura dos dados
df = spark.read.format("csv").option("header", True).load("/tmp/cardiovascular-diseases-risk.csv")

# COMMAND ----------

df.display()

# COMMAND ----------

df.select("General_Health").distinct().display()

# COMMAND ----------

# DBTITLE 1,Alterando nome da coluna (o Delta Table não aceita caracteres especiais em nome de colunas)
df.printSchema()

# COMMAND ----------

df = df.withColumnRenamed("Height_(cm)", "Height_cm").withColumnRenamed("Weight_(kg)", "Weight_kg")

# COMMAND ----------

# DBTITLE 1,Armazenamento de dados com Delta Table
df.write.format("delta").mode("overwrite").option("mergeSchema", "true").partitionBy("General_Health").save("/hospital/rw/cardiovascular_diseases/")

# COMMAND ----------

# MAGIC %md
# MAGIC # Visualização de dados

# COMMAND ----------


