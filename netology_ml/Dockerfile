FROM continuumio/miniconda3:latest
WORKDIR /app
COPY 1.sh /app/1.sh
RUN chmod +x /app/1.sh
RUN apt-get update && apt-get install -y bash  # Установка bash
RUN pip install mlflow boto3 pymysql
CMD ["/bin/bash", "/app/1.sh"]