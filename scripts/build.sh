#!/bin/bash
set -e

echo "=== Шаг 1: Создание архива-артефакта ==="
mkdir -p ./artifacts
ARCHIVE_NAME="./artifacts/app-artifact-$(date +%Y%m%d_%H%M%S).tar.gz"
tar -czf "$ARCHIVE_NAME" app/ Dockerfile
echo "Артефакт успешно создан: $ARCHIVE_NAME"

echo "=== Шаг 2: Сборка Docker-образа ==="
docker build -t devops-app:latest .
echo "Docker-образ успешно собран!"
