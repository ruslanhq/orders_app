FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 8000
EXPOSE 8001

RUN chmod +x /app/entrypoint_store_app.sh
RUN chmod +x /app/entrypoint_warehouse_app.sh

WORKDIR /app

