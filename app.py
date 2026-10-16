from datetime import datetime, timedelta
from flask import Flask, render_template_string, jsonify
import psutil

app = Flask(__name__)

visit_timestamps = []
APP_TITLE = "Интерактивное DevOps-приложение"

@app.route('/')
def index():
    global visit_timestamps
    now = datetime.now()
    visit_timestamps.append(now)
    one_hour_ago = now - timedelta(hours=1)
    visit_timestamps = [t for t in visit_timestamps if t > one_hour_ago]
    visits_last_hour = len(visit_timestamps)
    
    memory = psutil.virtual_memory()
    cpu_percent = psutil.cpu_percent(interval=0.1)
    
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f9; color: #333; text-align: center; padding-top: 50px; }
            .card { background: white; max-width: 500px; margin: 0 auto; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            button { background: #007bff; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 4px; cursor: pointer; }
            button:hover { background: #0056b3; }
            .metrics { background: #e9ecef; padding: 10px; margin-top: 20px; border-radius: 4px; text-align: left; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{{ title }}</h1>
            <p>Статус: <b>Работает отлично!</b></p>
            <p>Нажми кнопку, чтобы проверить интерактивность:</p>
            <button onclick="alert('Привет! Кнопка работает, интерфейс живой.')">Кликни меня</button>
            
            <div class="metrics">
                <h3>📊 Метрики и мониторинг:</h3>
                <p><b>Посещений за последний час:</b> {{ visits }}</p>
                <p><b>Доступно RAM:</b> {{ memory.available // (1024*1024) }} MB (всего {{ memory.total // (1024*1024) }} MB)</p>
                <p><b>Загрузка CPU:</b> {{ cpu }}%</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(
        html_template, 
        title=APP_TITLE, 
        visits=visits_last_hour, 
        memory=memory, 
        cpu=cpu_percent
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
