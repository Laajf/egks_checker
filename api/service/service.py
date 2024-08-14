from ..utils.get_data import get_data_money
from api.utils.text_to_json import text_to_json
from api.repository.repository import postgresql
class get_data:
    @staticmethod
    def get_money_data(number_card):
        text_card = get_data_money(number_card)

        return text_card

    @staticmethod
    def create_new_user(number_card):
        print("вызвалось")
        text_card = get_data_money(number_card)
        dictionary = text_to_json(text_card)
        return postgresql.bd_update(dictionary)

    @staticmethod
    def bd_read():
        return postgresql.bd_read()



