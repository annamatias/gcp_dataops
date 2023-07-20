import shutil
import unittest
import logging
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from src.hospital.ingestion_cardiovascular_diseases_risk import read_csv, rename_columns, save_delta


class PySparkTest(unittest.TestCase):

    @classmethod
    def suppress_py4j_logging(cls):
        logger = logging.getLogger("py4j")
        logger.setLevel(logging.WARN)

    @classmethod
    def create_testing_pyspark_session(cls):
        builder = SparkSession.builder \
            .appName("Testes Pyspark") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        spark = configure_spark_with_delta_pip(builder).getOrCreate()
        return spark

    @classmethod
    def setUpClass(cls):
        cls.suppress_py4j_logging()
        cls.spark = cls.create_testing_pyspark_session()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(
            "gcp_dataops/tests/storage_test")
        cls.spark.stop()

    @staticmethod
    def dataframe_mock(spark):
        schema = StructType([
            StructField("General_Health", StringType(), True),
            StructField("Checkup", StringType(), True),
            StructField("Exercise", StringType(), True),
            StructField("Heart_Disease", StringType(), True),
            StructField("Skin_Cancer", StringType(), True),
            StructField("Other_Cancer", StringType(), True),
            StructField("Depression", StringType(), True),
            StructField("Diabetes", StringType(), True),
            StructField("Arthritis", StringType(), True),
            StructField("Sex", StringType(), True),
            StructField("Age_Category", StringType(), True),
            StructField("Height_cm", DoubleType(), True),
            StructField("Weight_kg", DoubleType(), True),
            StructField("BMI", DoubleType(), True),
            StructField("Smoking_History", StringType(), True),
            StructField("Alcohol_Consumption", DoubleType(), True),
            StructField("Fruit_Consumption", DoubleType(), True),
            StructField("Green_Vegetables_Consumption", DoubleType(), True),
            StructField("FriedPotato_Consumption", DoubleType(), True)
        ])

        data = [
            ("Excellent", "Within the past 2 years", "Yes", "No", "No", "No", "No", "No",
             "No", "Female", "70-74", 152.0, 52.16, 22.46, "No", 0.0, 30.0, 4.0, 0.0),
            ("Excellent", "Within the past year", "Yes", "No", "No", "No", "No", "No",
             "Yes", "Male", "70-74", 191.0, 112.49, 31.0, "No", 0.0, 30.0, 10.0, 15.0)
        ]

        return spark.createDataFrame(data, schema)

    def test_read_csv(self):
        df = read_csv(self.spark)
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), 308854)

    def test_rename_columns(self):
        data = PySparkTest.dataframe_mock(self.spark)
        renamed_df = rename_columns(data)
        self.assertListEqual(renamed_df.columns, ["General_Health", "Checkup", "Exercise", "Heart_Disease", "Skin_Cancer", "Other_Cancer", "Depression", "Diabetes", "Arthritis", "Sex",
                             "Age_Category", "Height_cm", "Weight_kg", "BMI", "Smoking_History", "Alcohol_Consumption", "Fruit_Consumption", "Green_Vegetables_Consumption", "FriedPotato_Consumption"])

    def test_save_delta(self):
        data = PySparkTest.dataframe_mock(self.spark)
        path = "tests/storage_test"
        save_delta(data, path)

    def test_fail_read_csv(self):
        path = ""
        with self.assertRaises(Exception):
            read_csv(self.spark, path)

    def test_fail_rename_columns(self):
        data = PySparkTest.dataframe_mock(self.spark)
        # Modificando a coluna "Weight_kg" para ser uma string
        df_invalid = data.withColumn(
            "Weight_kg", data["Weight_kg"].cast(StringType()))

        # Espera-se que essa operação cause um erro, pois a coluna "Weight_kg" é uma string em vez de um tipo numérico
        with self.assertRaises(Exception):
            rename_columns(df_invalid)

    def test_fail_save_delta(self):
        schema = StructType([
            StructField("Name", StringType(), True),
            StructField("Height", IntegerType(), True),
            StructField("Weight", DoubleType(), True)
        ])
        data = [("Alice", 170, 60.5)]
        df = self.spark.createDataFrame(data, schema)

        with self.assertRaises(Exception):
            save_delta(df)


if __name__ == '__main__':
    unittest.main()
