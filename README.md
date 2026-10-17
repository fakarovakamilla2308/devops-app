# DevOps App — Python Flask with CI/CD & Monitoring

Веб-приложение на базе **Python Flask** с автоматизированным CI/CD пайплайном через **GitHub Actions** и системой мониторинга на базе **Prometheus** и **Grafana**.

## Ссылки для проверки
* **Работающее приложение:** http://201.24.55.131:5000/
* **Health Check:** http://201.24.55.131:5000/health
* **Мониторинг Grafana:** http://201.24.55.131:3000/ (доступен в режиме просмотра без авторизации)
* **Исходный код:** https://github.com/fakarovakamilla2308/devops-app

## Стек технологий
* **Backend:** Python, Flask, `psutil`
* **Контейнеризация:** Docker, Docker Compose
* **CI/CD:** GitHub Actions (автодеплой на VPS по SSH)
* **Мониторинг:** Prometheus + Grafana
