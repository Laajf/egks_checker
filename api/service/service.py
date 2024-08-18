from ..utils.get_data import get_data_money
from api.utils.text_to_json import text_to_json
from api.repository.repository import postgresql
from ..utils.in_text import find_card_info,remove_leading_zero,extract_amount,remove_non_digits

class get_data:
    @staticmethod
    def get_money_data(number_card, chat_id):
        data = postgresql.bd_read()
        print(f"данные {data}")
        card_info = find_card_info(remove_leading_zero(number_card), data)
        if card_info is False:
            print("это")
            text_card = get_data_money(number_card)
            dictionary = text_to_json(text_card)
            postgresql.bd_create(dictionary, chat_id)
            return text_card
        else:
            print("не это")
            return card_info


    @staticmethod
    def create_new_user(number_card):
        print("вызвалось")
        text_card = get_data_money(number_card)
        dictionary = text_to_json(text_card)
        return postgresql.bd_create(dictionary)

    @staticmethod
    def bd_find_min_money():
        data = postgresql.bd_read()
        print(f"вот данные {data}")
        min_money = []
        for i in data:
            if float(remove_non_digits(i["money"])) < 48:
                min_money.append(i)
        print(f"должники {min_money}")
        return min_money

    @staticmethod
    def bd_read():
        return postgresql.bd_read()

    @staticmethod
    def data_update_bd():
        print("начало апдейта")
        data = postgresql.bd_read()
        for i in data:
            i["money"] = extract_amount(str(get_data_money("0"+i["number_card"])))
        print("аптейт закончен")
        return data

    @staticmethod
    def delete_data():
        return postgresql.bd_delete()


