# Spark-docker
This repository demonstrates how to set up Apache Spark in a Docker environment, running in Standalone Cluster Mode. Additionally, it outlines how to connect Spark to a Kafka cluster for real-time data streaming and processing. 

This setup provides a seamless way to experiment with distributed data processing using Spark and Kafka, entirely in Dockerized environments.

My kafka setup can be found in this [repository.](https://github.com/ryanperezx/kafka-docker)

To submit pre-created spark jobs, generate an interactive shell into spark-master container
> docker exec -it <container> sh  
cd jobs  
./submit_jobs.sh

This submits the spark jobs ending in .py extensions.