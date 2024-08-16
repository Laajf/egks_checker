import telebot
import requests

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6834293981:AAFny0HppZ99uckh3zlpOsoXqSraBniRSPQ'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    chat_id = message.chat.id
    response_message = (
        "Здравствуйте! Я ваш помощник для проверки баланса на карте EGKS.\n\n"
        "Вот как вы можете использовать меня:\n\n"
        "1. Отправьте команду `/egkks <номер_карты>`, чтобы узнать, сколько денег осталось на вашей карте.\n"
        "2. Я напомню вам, если денег на карте будет недостаточно.\n\n"
        "Просто следуйте инструкциям, и я помогу вам следить за состоянием вашего счета.\n\n"
        "Если у вас возникнут вопросы, не стесняйтесь спрашивать!"
    )
    bot.reply_to(message, response_message)


@bot.message_handler(commands=['egkks'])
def handle_ekks_command(message):
    # Получаем текст команды
    command_text = message.text

    # Извлекаем число из текста команды
    try:
        _, number = command_text.split()
        chat_id = message.chat.id
        response_message = f"Команда принята! Ваш chat ID: {chat_id}, число: {number}"
        bot.reply_to(message, response_message)
        response = requests.get(f"http://selenium-app:8000/get_data_card/{str(number)}")
        response = response.json()
        if "money" in response:
            print(f"Вот запрос которого мы заслужили: {response['money']}")
            response = "у вас осталось(также вы занесены в бд и вам будут приходить сообщения если у вас буде баланс " \
                       "меньше 48 рублей)" + response['money']
            bot.reply_to(message, response)
        else:
            response_if_money = ""
            response = "у вас осталось(также вы занесены в бд и вам будут приходить сообщения если у вас буде баланс " \
                       "меньше 48 рублей)" + response_if_money
            bot.reply_to(message, response)
    except ValueError:
        response_message = "Команда неправильного формата. Используйте: /ekks <число>"
        bot.reply_to(message, response_message)


bot.polling()
