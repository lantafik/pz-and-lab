from flask import Flask, render_template, request, redirect
import os
import threading
import pymysql
from bot import start_bot

# Конфигурация базы данных
db_config = {
    'host': 'mysql.j1007852.myjino.ru',
    'port': 3306,
    'user': 'j1007852',
    'password': 'el|N#2}-F8',
    'database': 'j1007852_lr1_bg'
}

# Flask-приложение
app = Flask(__name__)

FILE_PATH = "йоу.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_commands')
def view_commands():
    commands = [
        "/start - Запуск бота",
        "/help - Список команд",
        "/start_timer - Запуск таймера"
    ]
    return render_template('index.html', commands=commands)

@app.route('/view_random_messages')
def view_random_messages():
    if not os.path.exists(FILE_PATH):
        random_messages = []
    else:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            random_messages = file.readlines()
    return render_template('index.html', random_messages=[msg.strip() for msg in random_messages])

@app.route('/add_random_message', methods=['POST'])
def add_random_message():
    message = request.form['random_message']
    with open(FILE_PATH, 'a', encoding='utf-8') as file:
        file.write(f"{message}\n")
    return redirect('/view_random_messages')


def run_flask():
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    # Запускаем Telegram-бота в отдельном потоке
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    # Запускаем Flask-приложение
    run_flask()
