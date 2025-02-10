# Домашнее задание: Docker и микросервисная архитектура

## Описание задания

Цель задания — закрепить знания по технологии контейнеризации Docker. Мы создадим Docker-образ, который будет основан на образе `continuumio/miniconda3:latest`, и настроим простой контейнер с установкой Python-пакетов и запуском скрипта.

### Шаги выполнения задания

1. **Создание Dockerfile**:
   - Мы использовали образ `continuumio/miniconda3:latest` как базовый.
   - Установили рабочую директорию в `/app`.
   - Копировали файл `1.sh` в контейнер и присвоили ему права на выполнение.
   - Установили необходимые пакеты через `pip`: `mlflow`, `boto3`, и `pymysql`.
   - Добавили команду для запуска скрипта `1.sh`.

2. **Содержимое Dockerfile**:

```Dockerfile
FROM continuumio/miniconda3:latest
WORKDIR /app
COPY 1.sh /app/1.sh
RUN chmod +x /app/1.sh
RUN pip install mlflow boto3 pymysql
CMD ["/bin/bash", "/app/1.sh"]