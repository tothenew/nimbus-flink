![nimbus logo](/docs/images/nimbus_logo.png)

# Nimbus-Flink : No Code Data Ingestion Framework using Flink
[Apache Flink](https://nightlies.apache.org/flink/flink-docs-master/api/python/) is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.
Learn more about Flink at https://flink.apache.org/


## Basic Features

![flow diagram]/docs/images/flow_diagram.png)

Nimbus-Flink enables users to ingest data from multiple sources into different destinations without the need of writing any script.
User just has to provide details of source and destination in easily configurable json files and Nimbus-Flink will do the rest.

# Getting Started

## Prerequisite

* Java 8 or 11 (sudo apt-get install openjdk-8-jdk)
* PyFlink 1.17.0 (pip install apache-flink==1.17.0)
#### For Mysql connection required jars
* [JDBC connector jar](https://mvnrepository.com/artifact/org.apache.flink/flink-connector-jdbc)
* [MySql connector jar](https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.31/)
* [Mysql-java-connector jar](https://mvnrepository.com/artifact/mysql/mysql-connector-java/6.0.3)
* [Flink-sql-connector-sql-server jar](https://mvnrepository.com/artifact/com.ververica/flink-sql-connector-sqlserver-cdc)
#### For Postgresql connection required jars
* Connector: [JDBC](https://mvnrepository.com/artifact/org.apache.flink/flink-connector-jdbc)
* Jar should be in lib folder of pyflink : [postgres-sql-jar](https://mvnrepository.com/artifact/org.postgresql/postgresql/42.5.4) 
#### For S3 connection required jars:
* [s3-fs-presto jar](https://mvnrepository.com/artifact/org.apache.flink/flink-s3-fs-presto)
* While establishing connection between the Pyflink and S3 bucket make sure you have define these configurations in the pyflink's config.yaml.

  Go to the cd flink-1.17.0/conf - - - -> open flink.conf.yaml file present in that folder and provide the 

  AWS ACCESS KEY AND AWS SECRET KEY:

  S3_bucket connection details:

  Fs.s3.awsaccesskey : " "   
  Fs.s3.awssecretkey : " "

#### For Hadoop connection required jars:
* [Hadoop-shaded-jar](https://repo.maven.apache.org/maven2/org/apache/flink/flink-shaded-hadoop-2-uber/2.4.1-10.0/)


## Cloning Nimbus-Flink
```
https://github.com/tothenew/nimbus-flink.git
```

## Important Points to Consider before Configuring 
* Path for hdfs **hdfs://host:port/target-directory-name/**. 
* Target directory must be present in the hdfs.
* Target directory must have all the permissions.
* While Ingesting data to the s3 bucket make sure that your account and s3 bucket both are in the same region.
* All the jar files should be in the lib folder of PyFlink but s3-fs-presto should also resides with its own name folder within the plugins folder of PyFlink.

## Configuring Nimbus-Flink

* Create the config.json file from config.json.template present in [ingestion_templates](flink/ingestion_templates) folder.
* Refer to the template files inside [ingestion_templates](flink/ingestion_templates) folder and edit the file according to your source and destination. For example if your source is mysql and destination is hdfs, edit and configure the **mysql_to_hdfs.json.template** to create **mysql_to_hdfs.json** file.

## Running Nimbus-Flink
After having all the setup and configuring json templates according to you requirements run this command on the terminal (pycharm-terminal)

```
python main.py <path_to_json_file>
```
