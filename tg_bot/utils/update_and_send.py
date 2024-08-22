import schedule
import time
import telebot
import threading
import requests

API_TOKEN = '6834293981:AAFny0HppZ99uckh3zlpOsoXqSraBniRSPQ'
bot = telebot.TeleBot(API_TOKEN)


def job():
    try:
        print("начало респонсе")
        response = requests.put(f"http://selenium-app:8000/post_update_bd")
        response.raise_for_status()
        print("POST запрос успешен")

        response = requests.get(f"http://selenium-app:8000/bd_find_min")
        response.raise_for_status()
        print("GET запрос успешен")

        data = response.json()
        print("Ответ от сервера получен и распарсен:", data)

        for i in data:
            print(f"Отправка сообщения в чат {i['chat_id']} с суммой {i['money']}")
            bot.send_message(i["chat_id"], i["money"])
            print("Сообщение отправлено")

    except Exception as e:
        print(f"Ошибка в процессе выполнения job: {e}")


def run_scheduler():
    print("Планировщик запущен")
    schedule.every(60).minute.do(job)

    while True:
        print("Ожидание выполнения задачи")
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
