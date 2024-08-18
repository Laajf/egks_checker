import schedule
import time
import telebot
import threading
import requests

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6834293981:AAFny0HppZ99uckh3zlpOsoXqSraBniRSPQ'
bot = telebot.TeleBot(API_TOKEN)


def job():
    print("начало респонсе")
    response = requests.get(f"http://selenium-app:8000/bd_find_min/")

    # Проверяем успешность запроса
    response.raise_for_status()

    # Парсим ответ как JSON
    data = response.json()  # Это список или словарь, в зависимости от ответа сервера

    # Проходимся по каждому элементу списка
    for i in data:
        # Отправляем сообщение в чат
        bot.send_message(i["chat_id"], i["money"])  # Используем send_message для отправки по chat_id

    print(data)


def run_scheduler():
    # Планируем выполнение задачи каждую минуту
    print("план выполнения")
    schedule.every(1).minute.do(job)

    while True:
        print("начало")
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # Запускаем планировщик в отдельном потоке
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
