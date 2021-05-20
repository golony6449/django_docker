From python:3.8.10

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

COPY . /app
WORKDIR /app

ENTRYPOINT "/app/entrypoint.sh"