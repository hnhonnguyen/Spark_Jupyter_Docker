from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from delta import configure_spark_with_delta_pip
import uuid 


import warnings
warnings.filterwarnings('ignore')
def create_spark():
    app_name = uuid.uuid1().hex
    builder = (SparkSession.builder
   .master("spark://spark:7077")
   .config("spark.driver.bindAddress", "dev")
   .config("spark.driver.host", "dev")
   .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
   .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
   .appName(app_name)
   )
    
    my_packages = ["org.apache.hadoop:hadoop-aws:3.3.4", "org.postgresql:postgresql:42.6.0", "com.microsoft.sqlserver:mssql-jdbc:11.2.2.jre17"]
    spark = configure_spark_with_delta_pip(builder, my_packages).getOrCreate()

    
    spark.sparkContext.setLogLevel("WARN")
    s3accessKeyAws = "minioadmin"
    s3secretKeyAws = "minioadmin"
    connectionTimeOut = "30"
    s3endPointLoc = "nginx:9000"
    
    spark.sparkContext._jsc.hadoopConfiguration().set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    spark.sparkContext._jsc.hadoopConfiguration().set("spark.hadoop.fs.s3a.path.style.access", "true")
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", s3endPointLoc)
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", s3accessKeyAws)
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", s3secretKeyAws)
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.multipart.size", "104857600")
    
    return spark