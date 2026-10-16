#!/bin/bash
set -e

CONTAINER_NAME="devops_app_container"
PORT=5000

echo "=== Остановка старой версии контейнера (если есть) ==="
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "=== Запуск нового контейнера из собранного образа ==="
docker run -d \
  --name $CONTAINER_NAME \
  -p $PORT:5000 \
  --restart always \
  devops-app:latest

echo "Деплой завершен успешно!"
echo "Приложение запущено и доступно на порту $PORT."
