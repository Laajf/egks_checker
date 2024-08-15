from ..utils.get_data import get_data_money
from api.utils.text_to_json import text_to_json
from api.repository.repository import postgresql
from ..utils.in_text import find_card_info,remove_leading_zero
class get_data:
    @staticmethod
    def get_money_data(number_card):
        data = postgresql.bd_read()
        print(f"данные {data}")
        card_info = find_card_info(remove_leading_zero(number_card), data)
        if card_info is False:
            print("это")
            text_card = get_data_money(number_card)
            dictionary = text_to_json(text_card)
            postgresql.bd_create(dictionary)
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
    def bd_read():
        return postgresql.bd_read()



