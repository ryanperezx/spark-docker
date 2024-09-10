FROM bitnami/spark:3.5.2
RUN ./sbin/start-master.sh

WORKDIR /opt/bitnami/spark
USER root
COPY jobs /jobs
RUN ["chmod", "+x", "/jobs/submit_jobs.sh"]