#!/bin/bash

# Define the folder containing your Spark job files
JOB_FOLDER="/opt/bitnami/spark/jobs"

# Loop through each file in the folder
for file in "$JOB_FOLDER"/*.py; do
    echo "Submitting Spark job: $file"
    if [[ "$file" == *"kafka"* ]]; then
        spark-submit --master spark://spark-master:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2 "$file"
    else
        spark-submit --master spark://spark-master:7077 "$file" 
    fi
done