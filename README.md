# This repository is for Data Engineering Zoomcamp week 5 homework

In this week we were working with Spark. We went through the installation, explored the batch processing, PySpark, RDD and DataFrames, SQL, transformations and actions.

## Installation

Here's a step-by-step guide to installing Spark locally on your macOS system:

Install Java 
Spark requires Java, so ensure you have Java Development Kit (JDK) installed on your machine. You can download and install the latest JDK from the Oracle website or use a package manager like Homebrew:

brew install openjdk@11

After installation, you need to set the JAVA_HOME environment variable to point to the JDK installation directory in your .bash_profile or .zshrc file:


export JAVA_HOME=/usr/local/Cellar/openjdk@11/11.0.22
export PATH=”$JAVA_HOME/bin:$PATH”

Then, reload the shell configuration:

source ~/.bash_profile  # or source ~/.zshrc if you're using zsh

## Download Spark 

Visit the [Apache Spark website](https://spark.apache.org/downloads.html) and download the pre-built version of Spark for the latest stable release. Choose the latest version of Spark built for Hadoop 3.2 and later. Once downloaded, unzip the file to a location of your choice.

Set the SPARK_HOME environment variable to point to the directory where Spark is installed. You can add this to your .bash_profile or .zshrc file:

export SPARK_HOME=/usr/local/Cellar/apache-spark/3.5.0/libexec  # Adjust path as per your installation
export PATH=”$SPARK_HOME/bin:$PATH”

Again, don't forget to reload the shell configuration after making changes.

## Test Installation 

Open a terminal window and run the following command to ensure Spark is installed correctly:

spark-shell

This will launch the Spark shell, and you should see the Spark logo and a Scala prompt (scala>). You can type :q to exit the shell.

To run PySpark, we first need to add it to PYTHONPATH:

export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"

export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip pyspark.zip"


