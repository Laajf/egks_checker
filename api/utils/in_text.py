import re

def find_card_info(card_number, data):
    for entry in data:
        if entry["number_card"] == card_number:
            return entry
    return False


def remove_leading_zero(s):
    if s.startswith("0"):
        return s[1:]
    return s


def extract_amount(text):
    """
    Извлекает сумму в формате 'XXX.XX р' из текстовой строки.

    :param text: Исходная текстовая строка.
    :return: Сумма в формате 'XXX.XX р' или None, если сумма не найдена.
    """
    # Регулярное выражение для поиска суммы
    pattern = r'\d+\.\d+ р'

    # Поиск совпадений
    match = re.search(pattern, text)

    if match:
        # Если совпадение найдено, возвращаем его
        return match.group()
    else:
        # Если совпадение не найдено, возвращаем None
        return None

def remove_non_digits(s):
    # Сохраняем только цифры и точку в строке
    return re.sub(r'[^\d.]', '', s)