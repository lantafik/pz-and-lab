import time
import telebot
import threading
import random
import os
from datetime import datetime
from pathlib import Path

# Инициализация бота с токеном
bot = telebot.TeleBot("8140304603:AAGi9IYLvtGfoByI_FtZRrNvP8M7EDt3_dA")

# Путь к директории для сохранения истории
history_folder = "chat_history"

# Создаем папку для истории, если она не существует
if not os.path.exists(history_folder):
    os.makedirs(history_folder)


# Функция для записи сообщения в файл
def save_message_to_file(user_id, username, text):
    # Формируем имя файла по текущей дате
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_name = os.path.join(history_folder, f"history_{current_date}.txt")

    # Форматируем строку сообщения
    timestamp = datetime.now().strftime("%H:%M:%S")
    message_line = f"[{timestamp}] {username} (ID: {user_id}): {text}\n"

    # Записываем сообщение в файл
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(message_line)


# Словарь для случайного сообщения при запуске
messages_dict = {
    1: "Привет!",
    2: "Добро пожаловать!",
    3: "Хорошего дня!",
    4: "Давайте начнем!",
    5: "Удачи!"
}

# Файл для случайных сообщений по таймеру
file_path = 'йоу.txt'


# Команда 1: Список команд
@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = (
        "/start - Запуск бота, отправка случайного приветственного сообщения.\n"
        "/start_timer - Запуск периодической отправки случайного сообщения из файла.\n"
        "/game - Начать простую игру со стоп-словом 'стоп'.\n"
        "/help - Вывод списка команд и их описание."
    )
    bot.reply_to(message, help_text)


@bot.message_handler(commands=['history'])
def help_message(message):
    folder_path = Path('chat_history/')
    files = [file for file in folder_path.iterdir() if file.is_file()]
    if not files:
        bot.reply_to(message, "История переписки не найдена.")
        return
    latest_file = max(files, key=lambda file: file.stat().st_mtime)
    with open(latest_file, 'rb') as file:
        bot.send_document(message.chat.id, file)


# Команда 2: Отправка случайного приветствия
@bot.message_handler(commands=['start'])
def start_message(message):
    random_message = random.choice(list(messages_dict.values()))
    bot.reply_to(message, random_message)

    # Сохраняем сообщение в файл
    save_message_to_file(message.from_user.id, message.from_user.username or "Unknown", random_message)


# Функция для периодической отправки случайных сообщений
def send_random_message_periodically(chat_id, interval=10):
    while True:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines).strip()
                bot.send_message(chat_id, random_line)
                # Сохраняем сообщение в файл
                save_message_to_file(chat_id, "Bot", random_line)
        time.sleep(interval)


@bot.message_handler(commands=['start_timer'])
def start_timer_message(message):
    chat_id = message.chat.id
    interval = 10  # секунды, можно изменить
    threading.Thread(target=send_random_message_periodically, args=(chat_id, interval), daemon=True).start()


# Команда 3: Простая игра со стоп-словом
@bot.message_handler(commands=['game'])
def start_game(message):
    bot.send_message(message.chat.id, "Игра началась! Пишите что угодно. Напишите 'стоп', чтобы завершить игру.")


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    username = message.from_user.username or "Unknown"
    text = message.text

    # Сохраняем сообщение в файл
    save_message_to_file(user_id, username, text)

    if text.lower() == 'стоп':
        bot.reply_to(message, "Игра завершена! Спасибо за участие.")
    else:
        bot.reply_to(message, f"Вы сказали: {text}")


# Запуск бота
bot.polling()
