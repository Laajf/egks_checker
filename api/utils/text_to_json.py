import re
import json

def text_to_json(text):
    # Определение шаблонов для поиска
    patterns = {
        "ticket_number": r"Номер\s(\d+)",
        "series": r"серия\s(\d+)",
        "valid_until": r"Действует\sпо\s([\d.]+)",
        "balance": r"Остаток\s([\d.]+)\sр\."
    }

    # Поиск данных по шаблонам
    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            result[key] = match.group(1)
        else:
            result[key] = None

    return result