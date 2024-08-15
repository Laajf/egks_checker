def find_card_info(card_number, data):
    for entry in data:
        if entry["number_card"] == card_number:
            return entry
    return False


def remove_leading_zero(s):
    if s.startswith("0"):
        return s[1:]
    return s